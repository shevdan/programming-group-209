from random import sample

range_of_nums = [i for i in range(100)]


def generate_grid(from_num: int, to_num: int) -> list:
    grid = sample(range_of_nums, 10)

    return grid
