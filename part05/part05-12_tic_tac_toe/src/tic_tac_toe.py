# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    if (y >= 0 and y <= 2) and (x >= 0 and x <= 2):
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
        else:
            return False
    return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)
