'''
Module that contains functions to interact with user.

It contains functions that print out into, information about
the state of game, loss or win.
'''

from random import choice
from time import sleep

def start_intro() -> str:
    '''
    Prints out the intro of the game.
    '''

    print("-" * 123)
    sleep(1)
    print('''You are about to pass a test that decides their fate.
The essence of this test is to select people to the highest class of society, \
where they will have unlimited opportunities.
Those who fail this test have no chance to change \
its result and are doomed to a mundane and gray life.''')
    sleep(1)
    print('-'*123)
    sleep(1)
    print('Prepare to start.')
    sleep(1)
    print('.'*123)
    sleep(1)
    print('Try your best.')
    sleep(1)
    print('-'*123)
    sleep(1)


def user_num() -> int:
    '''
    Tries to receive the input from user until it's a positive int number
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


def form_num() -> str:
    '''
    Randomly chooses the type of number user will look for.
    It can be 'ulam', 'prime' or 'lucky'.
    '''

    number_types = ['ulam', 'prime', 'lucky']
    num_type = choice(number_types)
    print(f'Please, choose the {num_type} number from the following:')

    return num_type

def congrats_output() -> str:
    '''
    Prints congratulations if the answer is right
    '''
    dif_congrats = ['Correct!','Exactly!','Right!']

    print(choice(dif_congrats))


def mistake_output(num_of_lives: int) -> str:
    '''
    Prints message that player makes a mistake
    if he did and number of remaining number of lives
    '''

    dif_mistakes = ['Not right!','Wrong!','Incorrect!']
    out = choice(dif_mistakes)
    print(out)
    if num_of_lives[0] > 1:
        print(f'U have {num_of_lives[0]} attempts left ')
    elif num_of_lives[0] == 0:
        sleep(1)
        print('-'*123)
        print('You lost and your future won\'t be good........')
    elif num_of_lives[0] == 1:
        print(f'U have {num_of_lives[0]} attempt left')

def victory_output() -> str:
    '''
    Prints victory message when player passed
    all 9 tests and returns False to stop the game
    '''

    print('Congratulations, you passed the test! \
Now your life will be filled with happiness')
