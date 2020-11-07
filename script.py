'''
This module contains main function (one iteration of game)
and ascript to run the game
'''

import generate_grid
import number_type
import interaction_with_player
from random import choice
from number_type import user_number_type as check_type

def one_iteration(num_of_lives, num_of_iterations):
    '''
    Implements one iteration of game (one guess of the user)
    '''
    interaction_with_player.victory_output() 

    range_of_nums = generate_grid.level_of_dif(num_of_iterations[0])
    grid = generate_grid.generate_grid(range_of_nums)
    type_of_num = interaction_with_player.form_num(grid)
    num_of_user = interaction_with_player.user_num()

    if num_of_user:
        if check_type(num_of_user, type_of_num) and num_of_user in grid:
            num_of_iterations[0] += 1
            interaction_with_player.congrats_output()
        else:
            num_of_lives[0] -= 1
            interaction_with_player.mistake_output(num_of_lives)
            # breaks the execution of the function, if the number of lives == 0
            if num_of_lives[0] <= 0:
                return False
        return True
    
    return False


if __name__ == '__main__':

    interaction_with_player.start_intro()
    num_of_lives = [3]
    num_of_iterations = [0]

    while True:
        if not one_iteration(num_of_lives, num_of_iterations):
            break
