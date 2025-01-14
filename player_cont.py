import chess
import pygame
from dimens import sq_size

selected_square = None

def handle_click(pos, board, screen):
    global selected_square
    col, row = pos[0] // sq_size, pos[1] // sq_size
    square = chess.square(col, 7 - row)

    if board.turn:
        if selected_square is None:
            piece = board.piece_at(square)
            if piece and piece.color == chess.WHITE:
                selected_square = square
        else:
            try:
                move = chess.Move(from_square=selected_square, to_square=square)

                if move in board.legal_moves:
                    board.push(move)
                else:
                    print("Illegal move!")
                selected_square = None
            except Exception as e:
                print(f"Invalid move: {e}")
                selected_square = None

def display_checkmate_message(victor, screen):
    font = pygame.font.Font(None, 74)
    text = f"Checkmate! {victor} wins!"
    message = font.render(text, True, (255, 0, 0))
    quit_text = font.render("Press Q to Quit", True, (0, 255, 0))

    screen.fill((0, 0, 0))
    screen.blit(message, (50, 300))
    screen.blit(quit_text, (50, 400))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return