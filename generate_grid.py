from random import sample

def level_of_dif(num_of_iterations):
    '''
    This functions determines the range
    from which the numbers will be taken.

    0 - 3 iterations : easy level of game: range of numbers [0, 20]
    4 - 6 iterations : medium level of game: range of numbers [20, 50]
    7 - 9 iterations : hard level of game: range of numbers [50, 100]
    '''

    if -1 < num_of_iterations < 4:
        return [10, 20]
    if 3 < num_of_iterations < 7:
        return [20, 50]
    if 6 < num_of_iterations < 10:
        return [50, 100]


def generate_grid(range_of_nums) -> list:
    '''
    '''

    grid = sample([i for i in range(range_of_nums[0], range_of_nums[1])], 10)


    return grid
