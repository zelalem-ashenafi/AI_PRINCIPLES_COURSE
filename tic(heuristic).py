import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board(board):
    print('---------')
    for i in range(3):
        print('| ' + ' | '.join(board[i*3:(i+1)*3]) + ' |')
        print('---------')

def check_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions

def heuristic(board):
    winning_lines = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]

    score = 0

    for line in winning_lines:
        if line.count('X') == 3:
            score += 100
        elif line.count('X') == 2 and line.count(' ') == 1:
            score += 10
        elif line.count('X') == 1 and line.count(' ') == 2:
            score += 1
        if line.count('O') == 3:
            score -= 100
        elif line.count('O') == 2 and line.count(' ') == 1:
            score -= 10
        elif line.count('O') == 1 and line.count(' ') == 2:
            score -= 1

    return score

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return -100
    elif check_winner(board, 'X'):
        return 100
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            print(f"Move {i + 1}: Heuristic value {score}")
            if score > best_score:
                best_score = score
                move = i
    return move

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
            else:
                return move
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def main():
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player move
        move = player_move(board)
        board[move] = 'O'
        print_board(board)
        if check_winner(board, 'O'):
            print("You win!")
            break
        elif ' ' not in board:
            print("It's a tie!")
            break

        # AI move
        print("AI is making a move...")
        move = best_move(board)
        board[move] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("AI wins!")
            break
        elif ' ' not in board:
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
