'''
This module contains functions that implements generation of the game grid.

Function level_of_dif determines the range (which is the representation
of the level of difficulty which that will be increased thorough the test)
from which the numbers will be taken.

Function generate_grid generates grid, with a one specific number of needed
type and 9 more random numbers.
'''

from random import sample, randint, shuffle
from typing import List
from number_type import user_number_type as check

def level_of_dif(num_of_iterations):
    '''
    This functions determines the range
    from which the numbers will be taken.
    0 - 3 iterations : easy level of game: range of numbers [0, 20]
    4 - 6 iterations : medium level of game: range of numbers [20, 50]
    7 - 9 iterations : hard level of game: range of numbers [50, 100]
    '''

    range_of_nums = []
    if -1 < num_of_iterations < 4:
        range_of_nums = [10, 20]
    if 3 < num_of_iterations < 7:
        range_of_nums = [20, 50]
    if 6 < num_of_iterations < 10:
        range_of_nums = [50, 100]

    return range_of_nums


def generate_grid(range_of_nums: List[int], num_type: str) -> List[int]:
    '''
    This function generates the game grid, which consist of 10 numbers.

    Args : range_of_nums: a list of two ints, which represent the level of difficulty,
                which increases thorough the test.
            num_type: a string, which represents what type of num has to be present in
                the game grid.

    Returns: a list of 10 positive ints, which represents the game grid.

    Args are given by the other functions, therefore no exceptions should be rose.
    '''

    right_num = randint(range_of_nums[0], range_of_nums[1])

    # checks whether a num of desired type will be present in the grid.
    while not check(right_num, num_type):
        right_num = randint(range_of_nums[0], range_of_nums[1])

    range_of_generation = [i for i in range(range_of_nums[0], range_of_nums[1])]
    grid = sample(range_of_generation, 9)
    grid.append(right_num)
    shuffle(grid)


    return grid
