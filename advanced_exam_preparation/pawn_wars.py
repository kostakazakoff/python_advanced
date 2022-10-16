def player_moves():
    global r, c, color, chessboard, players
    chessboard[r][c] = '-'
    if color == 'White':
        player_step = r - 1
        end_of_board = 0
        diags_of_attack = ((r - 1, c + 1), (r - 1, c - 1))
    else:
        player_step = r + 1
        end_of_board = 7
        diags_of_attack = ((r + 1, c + 1), (r + 1, c -1))
    return end_of_board, diags_of_attack, player_step


players = {'White': [0, 0], 'Black': [0, 0]}
col_marks = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
turn = ['White', 'Black']
chessboard = []

for row in range(8):
    rank = input().split()
    if 'w' in rank:
        players['White'][0], players['White'][1] = row, rank.index('w')
        rank[rank.index('w')] = 'White'
    if 'b' in rank:
        players['Black'][0], players['Black'][1] = row, rank.index('b')
        rank[rank.index('b')] = 'Black'
    chessboard.append(rank)

while True:
    r, c = players[turn[0]][0], players[turn[0]][1]
    color = turn[0]
    oponent_color = turn[1]
    end, diag_attack, step = player_moves()

    if r == end:
        print(f"Game over! {color} pawn is promoted to a queen at {col_marks[c]}{8 - r}.")
        break

    for d in diag_attack:
        if 0 <= d[0] < 8 and 0 <= d[1] < 8 and chessboard[d[0]][d[1]] == oponent_color:
            print(f"Game over! {color} win, capture on {col_marks[d[1]]}{8 - d[0]}.")
            exit()

    players[color][0] = step
    chessboard[step][c] = color

    turn[0], turn[1] = turn[1], turn[0]