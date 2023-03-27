"""
This program allows the user to play Rock Paper Scissors against the computer.

The game is played as follows:
- The user is prompted to enter their choice of 'r' for rock, 'p' for paper, or 's' for scissors.
- The computer chooses a random option.
- The two choices are compared, and the winner is determined based on the following rules:
    1. Rock Vs Scissor => Rock(w)
    2. Rock Vs Paper => Paper(w)
    3. Scissor Vs Paper => Scissor(w)
- The result is displayed to the user.

The program continues to run until the user chooses to stop.

This program uses the following modules:
- random: generates random numbers for the computer's choice
- sys: allows for exiting the program

"""

import random
import sys

# loop the game until the user chooses to stop
while True:
    # print welcome message and game rules
    print("#"*40)
    print("******Welcome to Rock Paper Scissor Game******")
    print('''Rules for winning Game:
    1. Rock Vs Scissor => Rock(w)
    2. Rock Vs Paper => Paper(w)
    3. Scissor Vs Paper => Scissor(w)
    ''')

    # create a dictionary for the game options and a list of valid user choices
    game_option = {
        "r": "Rock",
        "p": "Paper",
        "s": "Scissor"
    }
    choice = ['r', 'p', 's']

    # prompt the user for their choice and validate input
    FLAG = False
    while FLAG is False:
        user_guess = input("Your turn Rock (r) Paper (p) scisssor(s)? ")
        user_guess = user_guess.lower()
        if user_guess in choice:
            FLAG = True
        else:
            print(f"Please input valid key. Keyword user={user_guess} is invalid")

    # generate a random computer choice
    comp = random.randint(0, 2)
    COMP_GUESS = choice[comp]

    # print the user and computer choices
    print("-"*40)
    print (f"Computer Guess is '{game_option[COMP_GUESS]}'")
    print (f"Your Guess is '{game_option[user_guess]}'")

    # determine the winner based on the choices and display the result
    if user_guess == COMP_GUESS:
        print(".... Game is tie ....")
    elif user_guess == 'r' and COMP_GUESS == 'p':
        print("---- You lose ----")
    elif user_guess == 'p' and COMP_GUESS == 's':
        print("---- You lose ----")
    elif user_guess == 's' and COMP_GUESS == 'r':
        print("---- You lose ----")
    else:
        print("++++ You Win! ++++")

    # print game ending message and prompt the user to play again
    print("-"*40)
    print("******Game Ends******")
    print("#"*40)
    replay = input('Do you want to try again(Y/N)?: ')
    if replay.lower() != 'y':
        print("Thank you for playing!")
        sys.exit()
