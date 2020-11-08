"""
This module contains main function (one iteration of game)
and a script to run the game
"""

import D_bug_generate_grid
import D_bug_interaction_with_player
from D_bug_number_type import user_number_type as check_type


def one_iteration(num_of_lives: int, num_of_iterations: int) -> bool:
    """
    Implements one iteration of the game (one guess of the user)

    This function assembles all the modules necessary for the game
    and combines them in main to run the game
    """

    if num_of_iterations[0] == 9:
        D_bug_interaction_with_player.victory_output()
        return False

    range_of_nums = D_bug_generate_grid.level_of_dif(num_of_iterations[0])
    type_of_num = D_bug_interaction_with_player.form_num()
    grid = D_bug_generate_grid.generate_grid(range_of_nums, type_of_num)
    print(grid)
    try:
        num_of_user = D_bug_interaction_with_player.user_num()
    except EOFError:
        print('You lost... You were so close...')
        return None

    if num_of_user:
        if check_type(num_of_user, type_of_num) and num_of_user in grid:
            num_of_iterations[0] += 1
            D_bug_interaction_with_player.congrats_output()
        else:
            num_of_lives[0] -= 1
            D_bug_interaction_with_player.mistake_output(num_of_lives)
            # breaks the execution of the function, if the number of lives == 0
            if num_of_lives[0] <= 0:
                return False
        return True
    return False


if __name__ == '__main__':

    D_bug_interaction_with_player.start_intro()
    num_of_lives_in_game = [3]
    num_of_iterations_of_game = [0]

    while True:
        if not one_iteration(num_of_lives_in_game, num_of_iterations_of_game):
            break
