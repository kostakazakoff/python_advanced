def numbers_searching(*args):
    numbers = [int(x) for x in args]
    smallest, biggest = min(numbers), max(numbers)
    sequence = [x for x in range(smallest, biggest + 1)]
    missing_number = list(set(sequence) - set(numbers))[0]
    duplicates = sorted(list(set([x for x in numbers if numbers.count(x) > 1])))
    return [missing_number, duplicates]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))