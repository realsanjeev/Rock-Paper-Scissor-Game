'''import random for COMP_GUESS'''
import random

while True:
    print("*******************************************")
    print("******Welcome to Rock Paper Scissor Game******")
    comp = random.randint(1,3)
    FLAG = False
    while FLAG is False:
        user_guess = input("Your turn Rock (r) Paper (p) scisssor(s)? ")
        user_guess = user_guess.lower()
        if user_guess == 'r' or user_guess == 'p' or user_guess == 's':
            FLAG = True
        else:
            print("Please input valid key")

    if user_guess == 'r':
        USER_VALUE='Rock'
    elif user_guess == 'p':
        USER_VALUE = 'Paper'
    elif user_guess == 's':
        USER_VALUE = 'Scissor'

# computer choice in string value
    if comp == 0:
        COMP_GUESS = 'r'
        COMP_VALUE = 'Rock'
    elif comp == 1:
        COMP_GUESS = 'p'
        COMP_VALUE = 'Paper'
    else:
        COMP_GUESS = 's'
        COMP_VALUE = 'Scissor'

    print (f'Computer has {COMP_VALUE} and you have {USER_VALUE}')

    if user_guess == COMP_GUESS:
        print("Game is tie")
    elif user_guess == 'r' and COMP_GUESS == 'p':
        print("You lose")
    elif user_guess == 'p' and COMP_GUESS == 's':
        print("You lose")
    elif user_guess == 's' and COMP_GUESS == 'r':
        print("You lose")
    else:
        print("you win!")

    print ("******Game Ends******")
    print ("Thank you for playing!")
    print("*******************************************")

    replay=input('Do you want to try again(Y/N)?: ').lower()
    if replay!='y':
        exit()
