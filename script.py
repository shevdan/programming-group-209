import generate_grid
import number_type
import interaction_with_player
from random import choice
from number_type import user_number_type as check_type

def main():
    pass



if __name__ == '__main__':
    interaction_with_player.start_intro()

    correct_nums = []
    num_of_lives = 3
    num_of_iterations = 0
    while True:
        range_of_nums = generate_grid.level_of_dif(num_of_iterations)
        grid = generate_grid.generate_grid(range_of_nums)
        
        type_of_num = interaction_with_player.form_num(grid)
        num_of_user = interaction_with_player.user_num()


        user_nums = []
        num_of_iterations += 1 # цей рядок мб мав би бути після першого іфа
        if num_of_user:
            if check_type(num_of_user, type_of_num):
                interaction_with_player.congrats_output()
                correct_nums.append(num_of_user)
            else:
                num_of_lives -= 1
                if num_of_lives <= 0:
                    interaction_with_player.mistake_output(num_of_lives)
                    break
        else:
            break

    print(correct_nums)
