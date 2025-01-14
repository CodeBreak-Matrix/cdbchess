import pygame
import chess
import chess.svg
from dynam import resource_path
from dimens import sc_wd , sc_ht , sq_size, PIECE_IMAGE_MAP

board = chess.Board()

def print_board():
    print(board)

def draw_pieces(board, screen):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_symbol = piece.symbol()
            image_filename = PIECE_IMAGE_MAP[piece_symbol]
            piece_image = pygame.image.load(resource_path(f"images/{image_filename}"))
            piece_image = pygame.transform.scale(piece_image, (sq_size, sq_size))
            col = chess.square_file(square)
            row = chess.square_rank(square)
            screen.blit(piece_image, (col*sq_size, (7 - row)*sq_size))
            
def play_checkmate_sound(winner):
    try:
        if winner == "White":
            audio_path = resource_path("audio/win_jingle.mp3")
        elif winner == "Black":
            audio_path = resource_path("audio/loss_jingle.mp3")
        else:
            raise ValueError("Invalid winner. Must be 'White' or 'Black'.")
        
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error playing sound: {e}")

def play_check_sound():
    try:
        audio_path = resource_path("audio/check_jingle.mp3")
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error playing check sound: {e}")

if __name__ == '__main__':
    print_board()