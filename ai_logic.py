import time
import chess
import chess.svg
from dimens import PIECES_VALUE, piece_square_tables

transposition_table = {}

def evaluate_board(board):
    val = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_value = PIECES_VALUE[piece.piece_type]
            position_score = piece_square_tables[piece.piece_type][
                chess.square_rank(square) if piece.color == chess.WHITE else 7 - chess.square_rank(square)
            ]
            val += piece_value + position_score if piece.color == chess.WHITE else -(piece_value + position_score)
    return val

def iterative_deepening(board, max_depth, time_limit=2.0):
    start_time = time.time()
    best_move = None
    for depth in range(1, max_depth + 1):
        if time.time() - start_time > time_limit:
            break
        best_move = find_best_move(board, depth)
    return best_move

def quiescence_search(board, alpha, beta):
    stand_pat = evaluate_board(board)
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiescence_search(board, -beta, -alpha)
            board.pop()

            if score >= beta:
                return beta
            if score > alpha:
                alpha = score
    return alpha

def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing):
    board_fen = board.fen()
    if board_fen in transposition_table:
        return transposition_table[board_fen]

    if depth == 0 or board.is_game_over():
        return quiescence_search(board, alpha, beta)

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
        transposition_table[board_fen] = max_eval
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
        transposition_table[board_fen] = min_eval
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

def ai_move(board, max_depth=4, time_limit=2.0):
    if not board.turn:  # AI turn
        best_move = iterative_deepening(board, max_depth, time_limit)

        if best_move and best_move in board.legal_moves:  # Move legality check
            board.push(best_move)
        else:
            print(f"AI generated an invalid move: {best_move}")
            print(f"Legal moves: {[str(m) for m in board.legal_moves]}")
