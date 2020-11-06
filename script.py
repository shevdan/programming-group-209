import generate_grid
import number_type
from random import choice
from number_type import user_number_type as check_type

def main():
    pass



if __name__ == '__main__':
    # gonna be changed for introduction func.
    print('blabla (Introduction)')

    correct_nums = []
    num_of_lives = 3
    num_of_iterations = 0
    while True:
        range_of_nums = generate_grid.level_of_dif(num_of_iterations)
        grid = generate_grid.generate_grid(range_of_nums)
        number_types = ['ulam', 'prime', 'lucky']
        print(grid)
        type_of_num = choice(number_types)
        print(f'Input {type_of_num}')
        try:
            num_of_user = int(input('Enter your number'))
        except ValueError:
            break
        user_nums = []
        num_of_iterations += 1
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
