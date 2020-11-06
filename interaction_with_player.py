from random import choice
"""
module that contains functions to interact with user
""" 
def start_intro():
    print("Today u r having very important test , Let's start.")

def game_round():
    number_types = ['ulam', 'prime', 'happy']
    num_type = choice(number_types)
    print(f'Please, choose the {num_type} from the following:')