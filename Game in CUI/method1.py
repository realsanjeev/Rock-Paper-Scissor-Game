"""
This module implements a simple Rock Paper Scissors game.
It prompts the user to choose rock, paper, or scissors,
generates a random choice for the computer,
and determines the winner based on the standard rules of the game. 
"""
import random

GAME_OPTION = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissor"
}
print("******Welcome to Rock Paper Scissor Game******")
print('''Rules for winning Game:
    1. Rock Vs Scissor => Rock(w)
    2. Rock Vs Paper => Paper(w)
    3. Scissor Vs Paper => Scissor(w)
    ''')

while True:
    USER_GUESS = input("Your Choice Rock (r) Papoer (p) scisssor(s)? ")
    if USER_GUESS.lower() not in ['r', 'p', 's']:
        print(f"Invalid error. Kerword {USER_GUESS} doesnot exist")
    else:
        break

# computer guess
comp = random.randint(0, 2)
# decode computer choice into that of user. 'r', 'p', 's'
if comp == 0:
    COMP_GUESS = 'r'
elif comp == 1:
    COMP_GUESS = 'p'
else:
    COMP_GUESS = 's'

print(f"Computer choice is '{GAME_OPTION[COMP_GUESS]}' \
and  Your choice is '{GAME_OPTION[USER_GUESS]}'")

if USER_GUESS == 'r':
    if COMP_GUESS == 'r':
        print(".... Game is tie ....")
    elif COMP_GUESS == 'p':
        print("---- You lose ----")
    else:
        print("++++ You Win ++++")

if USER_GUESS == 'p':
    if COMP_GUESS == 'p':
        print(".... Game is tie ....")
    elif COMP_GUESS == 's':
        print("---- You lose ----")
    else:
        print("++++ You Win ++++")

if USER_GUESS == 's':
    if COMP_GUESS == 's':
        print(".... Game is tie ....")
    elif COMP_GUESS == 'r':
        print("---- You lose ----")
    else:
        print("++++ You Win ++++")

print ("******Game Ends******")
