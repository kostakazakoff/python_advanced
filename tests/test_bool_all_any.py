gamepad = [[str(r), str(r + 1), str(r + 2)] for r in range(1, 10, 3)]

full = all([all([col in 'XO' for col in row]) for row in gamepad])

[print(*x) for x in gamepad]
print()
print(full)
