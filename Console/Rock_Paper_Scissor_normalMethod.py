from calendar import TUESDAY
import random

while (True):
    print("*******************************************")
    print("******Welcome to Rock Paper Scissor Game******")
    comp = random.randint(1,3)
    flag = False
    while (flag == False):
        userGuess = input("Your turn Rock (r) Paper (p) scisssor(s)? ")
        userGuess = userGuess.lower()
        if userGuess == 'r' or userGuess == 'p' or userGuess == 's':
            flag = True
        else:
            print("Please input valid key")

    if userGuess == 'r':
        userValue='Rock'
    elif userGuess == 'p':
        userValue = 'Paper'
    elif userGuess == 's':
        userValue = 'Scissor'

# computer choice in string value
    if comp == 0:
        compGuess = 'r'
        compValue = 'Rock'
    elif comp == 1:
        compGuess = 'p'
        compValue = 'Paper'
    else:
        compGuess = 's'
        compValue = 'Scissor'

    print (f'Computer has {compValue} and you have {userValue}')    

    if userGuess == compGuess:
        print("Game is tie")
    elif userGuess == 'r' and compGuess == 'p':
        print("You lose")
    elif userGuess == 'p' and compGuess == 's':
        print("You lose")
    elif userGuess == 's' and compGuess == 'r':
        print("You lose")
    else:
        print("you win!")

    print ("******Game Ends******")
    print ("Thank you for playing!")
    print("*******************************************")    

    replay=input('Do you want to try again(Y/N)?: ').lower()
    if replay!='y':
        exit()
