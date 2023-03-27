"""
A simple Rock Paper Scissors game.

This module implements a simple command-line game of Rock Paper Scissors.
The game prompts the user to choose rock, paper, or scissors,
generates a random choice for the computer, and
determines the winner based on the standard rules of the game.

Functions:
- get_game_info(): prints game info
- get_user_input(): prompts the user to input their choice (rock, paper, or scissors)
- generate_comp_input(): generates a random choice for the computer
- get_player_guess(c_in, u_in): prints the player's and computer's choices
- get_game_result(c_in, u_in): determines the winner of the game and prints the result
"""

import random
import sys

def get_game_info():
    """
    Display the welcome message and rules for playing Rock Paper Scissors game.
    """
    print("******Welcome to Rock Paper Scissor Game******")
    print('''Rules for winning Game:
    1. Rock Vs Scissor => Rock(w)
    2. Rock Vs Paper => Paper(w)
    3. Scissor Vs Paper => Scissor(w)
    ''')

def get_user_input():
    """
    Prompt the user for their choice of Rock (r), Paper (p), or Scissors (s) 
    and return the user's choice.

    Returns:
    user_guess (str): A string representing the user's choice of 
                    Rock (r), Paper (p), or Scissors (s).
    """
    flag = False
    print('-'*40)
    while flag is False:
        user_guess = input("Your turn Rock (r) Paper (p) scisssor(s)? ")
        user_guess = user_guess.lower()
        if user_guess in ['r', 'p', 's']:
            flag = True
        else:
            print(f"Please input valid key. Keyword user={user_guess} is invalid")
    return user_guess

def generate_comp_input():
    '''
    Generate a random choice for the computer between rock (r), paper (p), and scissors (s).
    
    Returns:
    comp_guess (str): The computer's choice represented as a string
    '''
    choice = ['r', 'p', 's']
    # generate a random computer choice
    comp = random.randint(0, 2)
    # computer choice in string value
    comp_guess = choice[comp]
    return comp_guess

def get_game_result(c_in, u_in):
    '''
    Prints the computer's and player's choices or guesses in a human-readable format, 
    along with the result of the game (win, lose, or tie).

    Parameters:
        c_in (str): The computer's guess, represented as 'r', 'p', or 's'.
        u_in (str): The user's guess, represented as 'r', 'p', or 's'.
        
    @'r' for rock 
    @'p' for paper 
    @'s' for scissors
    '''
    game_option = {
        "r": "Rock",
        "p": "Paper",
        "s": "Scissor"
    }
    print('-'*40)
    print(f"Computer Guess is '{game_option[c_in]}'\nYour Guess is '{game_option[u_in]}'")

    if u_in == 'r':
        if c_in == 's':
            print('++++ You Win ++++')
        elif c_in =='p':
            print('---- You lose ----')
    elif u_in =='s' and c_in =='p':
        print('++++ You Win ++++')
    else:
        print('.... Game is tie ....')
    print('-'*40)

if __name__=='__main__':
    get_game_info()
    while True:
        cpu_input = generate_comp_input()
        user_input = get_user_input()

        print('*'*40)
        print(f"user: {user_input} and computer: {cpu_input}")
        get_game_result(cpu_input, user_input)
        print('*'*40)

        retry = input('Do you want to play again(Y/N)?: ').lower()
        if retry.lower() !='y':
            sys.exit()
