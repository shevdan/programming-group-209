import generate_grid
import number_type
from random import choice
from number_type import user_number_type as check_type

def main():
    pass



if __name__ == '__main__':
    print('blabla (Introduction)')
    # mode = input('What play mode do you want to try?')
    # TODO: asks the user what level of difficilty (range_of_numbers)
    # TODO: decide_mode()
    # TODO: game_mode: limited number of errors, infinite mode
    correct_nums = []
    num_of_lives = 3
    while True:
        # level_of_difficulty = input('What level of dif do u want to play? ')
        # range_of_nums = lev_of_dif(level_of_difficulty)
        grid = generate_grid.generate_grid(0, 20)
        number_types = ['ulam', 'prime', 'lucky']
        print(grid)
        type_of_num = choice(number_types)
        print(f'Input {type_of_num}')
        try:
            num_of_user = int(input('Enter your number'))
        except ValueError:
            break
        user_nums = []
        if num_of_user:
            if check_type(num_of_user, type_of_num):
                print('yeah')
                correct_nums.append(num_of_user)
            else:
                num_of_lives -= 1
                if num_of_lives <= 0:
                    print('You lost and gonna die in poverty')
                    break
        
        else:
            break

    print(correct_nums)
    # results()
