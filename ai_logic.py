import chess
import chess.svg
from dimens import PIECES_VALUE

def evaluate_board(board):
    val = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_values = PIECES_VALUE[piece.piece_type]
            if piece.color == chess.WHITE:
                val += piece_values
            else:
                val -= piece_values
    return val

def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    
    if is_maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Prune the branch
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Prune the branch
        return min_eval

def find_best_move(board, depth):
    best_move = None
    best_value = float('-inf') if board.turn == chess.WHITE else float('inf')

    for move in board.legal_moves:
        board.push(move)
        board_value = minimax_alpha_beta(board, depth - 1, float('-inf'), float('inf'), not board.turn)
        board.pop()

        if board.turn == chess.WHITE and board_value > best_value:
            best_value = board_value
            best_move = move
        elif board.turn == chess.BLACK and board_value < best_value:
            best_value = board_value
            best_move = move

    return best_move

def ai_move(board):
    if not board.turn:  # Ensure it's AI's turn
        best_move = find_best_move(board, depth=3)

        if best_move and best_move in board.legal_moves:  # Validate move
            board.push(best_move)
        else:
            print(f"AI generated an invalid move: {best_move}")
            print(f"Legal moves: {[str(m) for m in board.legal_moves]}")
