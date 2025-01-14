import pygame
from logic import print_board, draw_pieces, play_checkmate_sound, play_check_sound
from logic import board
from dimens import sc_wd, sc_ht, sq_size, col1, col2
from player_cont import handle_click, display_checkmate_message
from ai_logic import ai_move

#Screen
pygame.init()
screen = pygame.display.set_mode((sc_wd, sc_ht))
pygame.display.set_caption('CDBK Chess')

#Draw Chessboard
def draw_board():
    for row in range(8):
        for col in range(8):
            color = col1 if (row+col)%2 == 0 else col2
            pygame.draw.rect(screen, color, (col*sq_size, row*sq_size, sq_size, sq_size))
            
#Main Loop
def main():
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN and board.turn:
                handle_click(pygame.mouse.get_pos(), board, screen)
                
        if not board.turn:
            ai_move(board)
        
        if board.is_check() and not board.is_checkmate():
            play_check_sound()
        
        if board.is_checkmate():
            victor = "Black" if board.turn else "White"
            play_checkmate_sound(victor)
            display_checkmate_message(victor, screen)
            flag = False
        
        draw_board()
        draw_pieces(board, screen)
        pygame.display.flip()

    pygame.quit()
    
if __name__ == '__main__':
    main()