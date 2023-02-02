'''import library for GUI'''
import glob
import random
import tkinter as tk
from PIL import Image, ImageTk

IMAGE_DIR_PATH = glob.glob('*/*.png')
SIZE = (100, 100)
COMPUTER_WIN = 0
USER_WIN = 0

root = tk.Tk()
root.geometry('685x475')
root.minsize(width=685, height=475)
root.maxsize(width=685, height=475)
root.title('Rock paper Scissor - GUI')
root.iconbitmap(bitmap='images/icon.ico')

# define frame for element adjustment
header_frame = tk.Frame(root)
header_frame.pack(fill='x')
image_frame = tk.Frame(root, background='gray')
image_frame.pack(expand=1, fill='both')
footer_frame = tk.Frame(root, background='gray')
footer_frame.pack(expand=1, fill='both')

HEADER_TEXT = 'Rock Paper Scissor - Game'
headerFont = ("Arial bold", 30)
header = tk.Label(header_frame,
                    text=HEADER_TEXT ,
                    font=headerFont,
                    bg='black', fg='White')
header.pack(fill='x')

score_board = tk.Label(header_frame, text='Computer:0  User:0',
                        bg='skyblue', fg='white',
                        font=('?', 15))
score_board.pack(fill='x')

result_game = tk.Label(header_frame, text='', fg='black',
                        bg='white', font=('?', 15))
result_game.pack(fill='x')

def computer_guess() -> str:
    '''
    Randomly generate computer guess

    Return:
        computer guess: str -> Literal['rock', 'paper', 'scissor']
    '''
    guess_num = random.randint(a=0, b=2)
    if guess_num == 0:
        return 'rock'
    elif guess_num == 1:
        return 'paper'
    else:
        return 'scissor'

def score_board_update(user_win_count: int, computer_win_count: int):
    '''
    Args:
        user_win_count: int -> count user win
        computer_win_count: int -> count computer win
    Result:
        Change config for score board
    '''
    if user_win_count == computer_win_count:
        score_board.config(text=f'Computer:{computer_win_count}  User:{user_win_count}')
    elif user_win_count > computer_win_count:
        score_board.config(text=f'Computer:{computer_win_count}  User:{user_win_count}',
                            bg='skyblue', fg='green')
    else:
        score_board.config(text=f'Computer:{computer_win_count}  User:{user_win_count}',
                            bg='skyblue', fg='red')

def who_win(user_guess: str):
    '''
    Args:
        user_guess: str -> given by user
    Return:
        change configure for result, score bord and hint label
    '''
    global USER_WIN, COMPUTER_WIN

    user_guess = user_guess.lower()
    cpu_guess = computer_guess().lower()
    print(f'Computer guess: {cpu_guess} and user guess: {user_guess}')

    if user_guess == cpu_guess:
        result_game.configure(text='Latest result: Game is Draw!!!!', fg='gray', bg='white')

    elif (user_guess == 'rock' and cpu_guess == 'paper') or\
    (user_guess == 'paper' and cpu_guess == 'scissor') or\
    (user_guess == 'scissor' and cpu_guess == 'rock'):
        USER_WIN += 1
        result_game.config(text='Latest result: You win the Game!!!!', bg='green', fg='white')
        print('*'*66)
    else:
        COMPUTER_WIN += 1
        result_game.config(text='Latest result: You Lose!!!!', bg='red', fg='white')
    score_board_update(USER_WIN, COMPUTER_WIN)
    hint_label.config(text=f'''
        User choice:    {user_guess.upper()}
        Computer choice: {cpu_guess.upper()}
        ''')
    hint_label.pack_configure(fill='x')

def image_file(images_path: list):
    '''
    Get image file ready for passing as argument in tkinker method

    Args:
        images_path: list -> list of paths for image
    Return:
        image file: list -> list of images
    '''
    imgs_lst = []
    for image_path in images_path:
        image = Image.open(image_path)
        image.thumbnail(SIZE)
        imgs_lst.append(ImageTk.PhotoImage(image))
    return imgs_lst

imgs = image_file(IMAGE_DIR_PATH)
rock_button = tk.Button(image_frame,
                        image=imgs[1],
                        activebackground='blue',
                        command=lambda: who_win('Rock'))
rock_button.pack(side='left', padx=50, pady=50, ipadx=15, ipady=25)

paper_button = tk.Button(image_frame,
                        image=imgs[0],
                        activebackground='blue',
                        command=lambda: who_win('Paper'))
paper_button.pack(side='left', padx=50, pady=50, ipadx=15, ipady=25)

scissor_button = tk.Button(image_frame,
                        image=imgs[2],
                        activebackground='blue',
                        command=lambda: who_win('Scissor'))
scissor_button.pack(side='left', padx=50, pady=50, ipadx=15, ipady=25)

hint_label = tk.Label(footer_frame,
                        text='Paper cover Rock.\nRock destroy Scissor.\nScissor cut paper',
                        font=('Arial bold', 25), fg='Gray')
hint_label.pack(side='bottom', fill='x')

if __name__=="__main__":
    root.mainloop()
