from random import choice
"""
module that contains functions to interact with user
""" 
def start_intro():
    print("Today u r having very important test , Let's start.")

def lvl_of_difficuly():
    lvl = input("Choose the level of difficuly :\nEazy Medium Hard\n")
    if lvl == 'Eazy':
        return (0,20)
    elif lvl == 'Medium':
        return (21,50)
    elif lvl == 'Hard':
        return (51,100)
    else:
        print("Please , input correct level of difficulty:")
        lvl_of_difficuly()

def game_round():
    number_types = ['ulam', 'prime', 'happy']
    num_type = choice(number_types)
    print(f'Please, choose the {num_type} number from the following:')
