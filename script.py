import generate_grid
import number_type
from random import choice

if __name__ == '__main__':
    print('blabla (Introduction)')
    mode = input('What play mode do you want to try?')
    # TODO: asks the user what level of difficilty (range_of_numbers)
    # TODO: decide_mode()
    # TODO: game_mode: limited number of errors, infinite mode
    while True:
        grid = generate_grid.generate_grid(level_of_difficulty, game_mode)
        number_types = ['ulam', 'prime', 'happy']
        print(grid)
        type_of_num = choice(number_types)
        print(f'Input {type_of_num}')
        correct_nums = []
        num_of_user = input('Enter your number')
        if num_of_user:
            if check_type(type_of_num, num_of_user)
            correct_nums.append(num_of_user)
        else:
            break
            # ? result -= 1

    print(correct_nums)
    results()
