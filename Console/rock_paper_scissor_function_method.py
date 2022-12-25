'''import random for COMP_GUESS'''
import random

def get_game_info():
    '''
    print game info
    '''
    print("Welcome To Rock Paper Scissor")
    print('''Rules for winning Game:
    1. Rock Vs Scissor => Rock(w)
    2. Rock Vs Paper => Paper(w)
    3. Scissor Vs Paper => Scissor(w)
    ''')

def get_user_input():
    '''
    input user choice
    user_guess: output param
    '''
    flag = False
    print('-'*40)
    while flag is False:
        user_guess = input("Your turn Rock (r) Paper (p) scisssor(s)? ")
        user_guess = user_guess.lower()
        if user_guess == 'r' or user_guess == 'p' or user_guess == 's':
            return user_guess
        else:
            print("Please input valid key")

def generate_compinput():
    '''
    computer choice
    computer_guess: output param
    '''
    comp = random.randint(1,3)

    # computer choice in string value
    if comp == 0:
        comp_guess = 'r'
    elif comp == 1:
        comp_guess = 'p'
    else:
        comp_guess = 's'
    return comp_guess

def get_player_guess(c_in, u_in):
    '''
    printing player and computer choice
    '''
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


def get_game_result(c_in,u_in):
    '''
    print result
    '''
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
    get_game_info()
    while True:
        COMP_INPUT = generate_compinput()
        user_input = get_user_input()
        get_player_guess(COMP_INPUT, user_input)
        get_game_result(COMP_INPUT, user_input)
        retry = input('Do you want to play again(Y/N)?: ').lower()
        if retry !='y':
            exit()
