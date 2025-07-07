import math

PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def create_board():
    return [[EMPTY] * 3 for _ in range(3)]

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[row][i] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return -10 + depth
    if check_winner(board, PLAYER_O):
        return 10 - depth
    if all(cell != EMPTY for row in board for cell in row):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
    board = create_board()
    display_board(board)

    while True:
        try:
            x, y = map(int, input("Enter your move (row and column, 0-2): ").split())
            if board[x][y] == EMPTY:
                board[x][y] = PLAYER_X
            else:
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter two numbers (0-2), separated by a space.")
            continue

        display_board(board)
        if check_winner(board, PLAYER_X):
            print("You win!")
            break
        if all(cell != EMPTY for row in board for cell in row):
            print("It's a draw!")
            break

        print("AI is making a move...")
        move = find_best_move(board)
        if move:
            board[move[0]][move[1]] = PLAYER_O
            display_board(board)
            if check_winner(board, PLAYER_O):
                print("AI wins!")
                break
            if all(cell != EMPTY for row in board for cell in row):
                print("It's a draw!")
                break

if __name__ == "__main__":
    play_game()