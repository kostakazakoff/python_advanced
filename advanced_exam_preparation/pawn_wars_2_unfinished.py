def pawn_capture():
    global chessboard, pawn
    for diagonal in pawn[0]['Attack diagonals']:
        target_r, target_c = r + diagonal[0], c + diagonal[1]
        
        if 0 <= target_r < 8 and 0 <= target_c < 8 and chessboard[target_r][target_c] == pawn[1]['Color']:
            print(f"Game over! {pawn[0]['Color']} win, capture on {col_marks[target_c]}{8 - target_r}.")
            return True


def pawn_at_and():
    global r, c, chessboard, pawn
    chessboard[r][c] = '-'
    r += pawn[0]['Move']

    if r == pawn[0]['End of board']:
        print(f"Game over! {pawn[0]['Color']} pawn is promoted to a queen at {col_marks[c]}{8 - r}.")
        return True

    chessboard[r][c] = pawn[0]['Color']
    pawn[0]['Position'][0] = r


pawn = [
    {'Color': 'White', 'Position': [0, 0], 'End of board': 0, 'Attack diagonals': ((1, 1), (-1, -1)), 'Move': -1},
    {'Color': 'Black', 'Position': [0, 0], 'End of board': 7, 'Attack diagonals': ((1, 1), (1, -1)), 'Move': 1}
]
col_marks = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
chessboard = []

for row in range(8):
    rank = input().split()

    if 'w' in rank:
        pawn[0]['Position'][0], pawn[0]['Position'][1] = row, rank.index('w')
        rank[rank.index('w')] = 'White'

    if 'b' in rank:
        pawn[1]['Position'][0], pawn[1]['Position'][1] = row, rank.index('b')
        rank[rank.index('b')] = 'Black'

    chessboard.append(rank)

while True:
    r, c = pawn[0]['Position'][0], pawn[0]['Position'][1]

    if pawn_capture():
        break

    if pawn_at_and():
        break

    pawn[0], pawn[1] = pawn[1], pawn[0]