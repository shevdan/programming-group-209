"""
module that contains functions to interact with user
"""

import random
import time


def start_intro():
    '''
    Prints out the intro of the game.
    '''

    print("-" * 123)
    time.sleep(1)
    print("""You are above to pass a test that decides their fate.

The essence of this test is to select people to the highest class of society, \
where they will have unlimited opportunities.

Those who fail this test have no chance to change \
its result and are doomed to a mundane and gray life.""")
    time.sleep(1)
    print('-'*123)
    time.sleep(1)
    print('Prepare to start.')
    time.sleep(1)
    print('.'*123)
    time.sleep(1)
    print('Try your best.')
    time.sleep(1)
    print('-'*123)
    time.sleep(1)


def user_num() -> int:
    '''
    Receives the input from user until it's a positive int number
    '''

    user_number = -1
    while user_number <=0 and isinstance(user_number,int):
        try:
            user_number = int(input())
            if user_number<=0:
                print("Enter positive number:")
        except ValueError:
            print("This number is not int type, Please input correct number")

    return user_number

def form_num(grid: list) -> str:
    '''
    Randomly chooses the type of number user will look for
    '''

    number_types = ['ulam', 'prime', 'happy']
    num_type = random.choice(number_types)
    print(f'Please, choose the {num_type} number from the following:\n{grid}')
    return num_type


def congrats_output():
    '''
    Prints congratulations if the answer is right
    '''
    dif_congrats = ['Correct!','Exactly!','Right!']
    out = random.choice(dif_congrats)
    print(out)



def mistake_output(num_of_lives):
    '''
    Prints message that player makes a mistake if he did and number of remaining number of lives
    '''

    dif_mistakes = ['Not right!','Wrong!','Incorrect!']
    out = random.choice(dif_mistakes)
    print(out)
    if num_of_lives[0] > 1:
        print(f'U have {num_of_lives[0]} attempts left ')
    elif num_of_lives[0] == 0:
        time.sleep(2)
        print('-'*123)
        print('You lost and your future won\'t be good........')
    elif num_of_lives[0] == 1:
        print(f'U have {num_of_lives[0]} attempt left')
