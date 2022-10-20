tasks = [int(x) for x in input().split(', ')]
task_index_needed = int(input())
cycles = 0
complete = False

while tasks[task_index_needed] > 0:
    min_cycles = float('inf')
    for value in tasks:
        if value < min_cycles and value != 0:
            min_cycles = value

    for idx, value in enumerate(tasks):
        if value == 0:
            if idx == task_index_needed:
                complete = True
                break
            continue

        if value == min_cycles:
            cycles += value
            tasks[idx] = 0
        
        if complete: break

print(cycles)