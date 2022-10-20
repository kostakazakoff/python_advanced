def numbers_searching(*args):
    numbers = [int(x) for x in args]
    smallest, biggest = min(numbers), max(numbers)
    


print(numbers_searching(1, 2, 4, 2, 5, 4))