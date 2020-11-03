from random import randrange

def generate_grid(from_num: int, to_num: int) -> list:
    grid = [randrange(from_num, to_num) for i in range(10)]

    return grid
