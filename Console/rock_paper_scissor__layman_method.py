'''import random for COMP_GUESS'''
import random

print("******Welcome to Rock Paper Scissor Game******")
comp = random.randint(1,3)
while True:
    USER_GUESS = input("Your turn Rock (r) Papoer (p) scisssor(s)? ")
    if USER_GUESS.lower() == ['r', 'p', 's']:
        break

if comp == 0:
    COMP_GUESS = 'r'
elif comp == 1:
    COMP_GUESS = 'p'
else:
    COMP_GUESS = 's'

print (f'computer has {COMP_GUESS} and you have {USER_GUESS}')

if USER_GUESS == 'r':
    if COMP_GUESS == 'r':
        print("Game is tie")
    elif COMP_GUESS == 'p':
        print("You lose")
    else:
        print("You Win")

if USER_GUESS == 'p':
    if COMP_GUESS == 'p':
        print("Game is tie")
    elif COMP_GUESS == 's':
        print("You lose")
    else:
        print("You Win")

if USER_GUESS == 's':
    if COMP_GUESS == 's':
        print("Game is tie")
    elif COMP_GUESS == 'r':
        print("You lose")
    else:
        print("You Win")

print ("******Game Ends******")
