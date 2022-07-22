import random

def getGameInfo():
    print("Welcome To Rock Paper Scissor")
    print('''Rules for winning Game:
    1. Rock Vs Scissor => Rock(w)
    2. Rock Vs Paper => Paper(w)
    3. Scissor Vs Paper => Scissor(w)
    ''')

def getUserinput():
    flag = False
    print('-'*40)
    while (flag == False):
        userGuess = input("Your turn Rock (r) Paper (p) scisssor(s)? ")
        userGuess = userGuess.lower()
        if userGuess == 'r' or userGuess == 'p' or userGuess == 's':
            return userGuess
        else:
            print("Please input valid key")

def generateCompinput():
    comp = random.randint(1,3)

    # computer choice in string value
    if comp == 0:
        compGuess = 'r'
    elif comp == 1:
        compGuess = 'p'
    else:
        compGuess = 's'
    return compGuess

def getPlayerGuess(c_in, u_in):
    if c_in == 'r':
        c_val ='Rock'
    elif c_in == 's':
        c_val = 'Scissor'
    else:
        c_val = 'Paper'

    if u_in == 'r':
        u_val ='Rock'
    elif u_in == 's':
        u_val = 'Scissor'
    else:
        u_val = 'Paper'
    print('-'*40)
    print(f'Computer Guess is {c_val}\nYour Guess is {u_val}')


def getGameResult(c_in,u_in):
    if u_in == 'r':
        if c_in == 's':
            print('You Win')
        elif c_in =='p':
            print('You Lose')
    elif u_in =='s' and c_in =='p':
        print('You win')
    else:
        print('Game is Tie')
    print('-'*40)


if __name__=='__main__':
    getGameInfo()
    while (True):
        comp_input = generateCompinput()
        user_input = getUserinput()
        getPlayerGuess(comp_input, user_input)
        getGameResult(comp_input, user_input)
        retry = input('Do you want to play again(Y/N)?: ').lower()
        if retry !='y':
            exit()