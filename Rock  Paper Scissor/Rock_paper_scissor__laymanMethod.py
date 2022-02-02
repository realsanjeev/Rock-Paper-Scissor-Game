import random

print("******Welcome to Rock Paper Scissor Game******")
comp = random.randint(1,3)
userGuess = input("Your turn Rock (r) Papoer (p) scisssor(s)? ")

if comp == 0:
    compGuess = 'r'
elif comp == 1:
    compGuess = 'p'
else:
    compGuess = 's'

print (f'computer has {compGuess} and you have {userGuess}')    

if userGuess == 'r':
    if compGuess == 'r':
        print("Game is tie")
    elif compGuess == 'p':
        print("You lose")
    else:
        print("You Win")

if userGuess == 'p':
    if compGuess == 'p':
        print("Game is tie")
    elif compGuess == 's':
        print("You lose")
    else:
        print("You Win")

if userGuess == 's':
   if compGuess == 's':
       print("Game is tie")
   elif compGuess == 'r':
       print("You lose")
   else:
       print("You Win")
                  
print ("******Game Ends******")
