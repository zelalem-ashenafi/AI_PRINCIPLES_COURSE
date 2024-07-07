import chess

def minimax_alpha_beta(position, depth, alpha, beta, maximizing_player):
    if depth == 0 or position.is_game_over():
        return evaluate_board(position)
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in position.legal_moves:
            position.push(move)
            eval = minimax_alpha_beta(position, depth-1, alpha, beta, False)
            position.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in position.legal_moves:
            position.push(move)
            eval = minimax_alpha_beta(position, depth-1, alpha, beta, True)
            position.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def evaluate_board(position):
    # Simplistic evaluation function for demonstration
    if position.is_checkmate():
        if position.turn:
            return -9999  # Black wins
        else:
            return 9999   # White wins
    elif position.is_stalemate() or position.is_insufficient_material():
        return 0
    else:
        material = sum(piece_value(piece) for piece in position.piece_map().values())
        return material

def piece_value(piece):
    values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    value = values[piece.piece_type]
    return value if piece.color == chess.WHITE else -value

# Example usage:
board = chess.Board()
depth = 3  
best_move = None
best_value = float('-inf')
for move in board.legal_moves:
    board.push(move)
    board_value = minimax_alpha_beta(board, depth-1, float('-inf'), float('inf'), False)
    board.pop()
    if board_value > best_value:
        best_value = board_value
        best_move = move

print("Best Move: ", best_move)
