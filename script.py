import generate_grid
import number_type

if __name__ == '__main__':
    print('blabla (Introduction)')
    mode = input('What play mode do you want to try?')
    #TODO: decide_mode()
    grid = generate_grid.generate_grid(0, 100)
    print(grid)
    correct_nums = []
    while True:
        num_of_user = input('Enter your number')
        if num_of_user:
            correct_nums.append(num_of_user)
            #if check_type():
            #    result += 1
        else:
            break
    print(correct_nums)
