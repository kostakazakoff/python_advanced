from math import floor


def step_to(direct: str):
    global field, r, c
    player_path.append([r, c])
    field[r][c] = 0
    if direct == 'up': r -= 1
    if direct == 'down': r += 1
    if direct == 'left': c -= 1
    if direct == 'right': c += 1
    r, c = r % SIZE, c % SIZE


SIZE = int(input())
field = []
player_path = []
coins = 0
won = True

for row in range(SIZE):
    line = [int(x) if x.isdigit() else x for x in input().split()]
    if 'P' in line:
        r, c = row, line.index('P')
        line[c] = 0
    field.append(line)

while coins < 100:
    step_to(input())

    if field[r][c] == 'X':
        coins = floor(coins * 0.5)
        won = False
        break

    coins += field[r][c]

else:
    player_path.append([r, c])
    print(f"You won! You've collected {coins} coins.")

if not won:
    player_path.append([r, c])
    print(f"Game over! You've collected {coins} coins.")

print('Your path:')
[print(x) for x in player_path]

