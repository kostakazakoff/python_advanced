from collections import deque


elves = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]
used_energy = 0
toys_count = 0
work_count = 0

while materials and elves:
    elf = elves.popleft()
    toy = materials[-1]
    energy, toys_maked, eat_cookie = 0, 0, 0

    if elf < 5:
        continue

    work_count += 1

    if work_count % 3 == 0:
        if elf < toy * 2:
            elf *= 2
            elves.append(elf)
            continue

        toys_maked = 2
        energy = toy * 2
        eat_cookie = 1

    else:
        if elf < toy:
            elf *= 2
            elves.append(elf)
            continue

        toys_maked = 1
        energy = toy
        eat_cookie = 1

    if work_count % 5 == 0:
        if toys_maked:
            toys_maked = 0
            eat_cookie = 0

    elf -= energy
    toys_count += toys_maked
    used_energy += energy
    elves.append(elf + eat_cookie)
    materials.pop()

print(f"Toys: {toys_count}")
print(f"Energy: {used_energy}")

if elves: print(f"Elves left: {', '.join([str(x) for x in elves])}")
if materials: print(f"Boxes left: {', '.join([str(x) for x in materials])}")
