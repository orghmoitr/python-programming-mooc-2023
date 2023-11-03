# Write your solution here

def who_won(game_board: list) -> int:
    player1_pieces = 0
    player2_pieces = 0
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 1:
                player1_pieces += 1
            elif game_board[i][j] == 2:
                player2_pieces += 1
            j += 1
        i += 1
    if player1_pieces > player2_pieces:
        return 1
    elif player2_pieces > player1_pieces:
        return 2
    else:
        return 0
