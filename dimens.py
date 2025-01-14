'''
This file contains the dimensions for the environment and the assets.
'''
import chess

#Screen Dimensions
sc_wd , sc_ht = 800, 800
sq_size = sc_wd // 8

#Colors
col1 = (169, 169, 169)
col2 = (255, 248, 240)

#Symbol to image mapping
PIECE_IMAGE_MAP = {
    "P": "white-pawn.png",
    "N": "white-knight.png",
    "B": "white-bishop.png",
    "R": "white-rook.png",
    "Q": "white-queen.png",
    "K": "white-king.png",
    "p": "black-pawn.png",
    "n": "black-knight.png",
    "b": "black-bishop.png",
    "r": "black-rook.png",
    "q": "black-queen.png",
    "k": "black-king.png"
}

#Piece values for AI
PIECES_VALUE = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 1000    #High value for king
}