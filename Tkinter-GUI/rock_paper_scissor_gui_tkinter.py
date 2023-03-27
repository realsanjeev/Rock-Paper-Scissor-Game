"""
This module implements a GUI-based rock-paper-scissors game. The game allows the user to play
against the computer. The user can make their choice by clicking on one of the three buttons that
represent rock, paper, or scissors. The computer makes its choice randomly. The game keeps track
of the user's and the computer's wins and displays the current score on the GUI.

The module uses the following external libraries:
- glob
- random
- tkinter
- PIL

The module contains the following functions and classes:
- computer_guess() -> str
- score_board_update(user_win_count: int, computer_win_count: int) -> None
- who_win(user_guess: str)
- image_file(images_path: list)

The module has the following global constants:
- IMAGE_DIR_PATH: a list of image paths for the game buttons
- SIZE: a tuple representing the size for the thumbnail images
- COMPUTER_WIN: an integer representing the computer's win count
- USER_WIN: an integer representing the user's win count
- root: the main window for the GUI
- header_frame: a frame for the header
- image_frame: a frame for the images
- footer_frame: a frame for the footer
- HEADER_TEXT: a string representing the text for the header label
- headerFont: a tuple representing the font for the header label
- header: the header label
- score_board: the label for the score board
- result_game: the label for the game result
- imgs: a list of images for the game buttons
- rock_button: the button for the rock choice
- paper_button: the button for the paper choice
- scissor_button: the button for the scissors choice
"""

import glob
import random
import tkinter as tk
from PIL import Image, ImageTk

# Set path to directory containing images
IMAGE_DIR_PATH = glob.glob('*/*.png')

# Set size for thumbnail images
SIZE = (100, 100)

# Initialize counters for computer and user wins
COMPUTER_WIN = 0
USER_WIN = 0

# Create main window for GUI
root = tk.Tk()

# Set size and title for window
root.geometry('685x475')
root.minsize(width=685, height=475)
root.maxsize(width=685, height=475)
root.title('Rock paper Scissor - GUI')

# Set icon for window
root.iconbitmap(bitmap='images/icon.ico')

# Create frame for header
header_frame = tk.Frame(root)
header_frame.pack(fill='x')

# Create frame for images
image_frame = tk.Frame(root, background='gray')
image_frame.pack(expand=1, fill='both')

# Create frame for footer
footer_frame = tk.Frame(root, background='gray')
footer_frame.pack(expand=1, fill='both')

# Set text and font for header label
HEADER_TEXT = 'Rock Paper Scissor - Game'
headerFont = ("Arial bold", 30)
header = tk.Label(header_frame, text=HEADER_TEXT, font=headerFont, bg='black', fg='White')
header.pack(fill='x')

# Create label for score board
score_board = tk.Label(header_frame, text='Computer:0  User:0',
                       bg='skyblue', fg='white', font=('?', 15))
score_board.pack(fill='x')

# Create label for game results
result_game = tk.Label(header_frame, text='', fg='black',
                        bg='white', font=('?', 15))
result_game.pack(fill='x')

def computer_guess() -> str:
    """
    Randomly generate computer guess.
    
    Returns:
    -------
    str:
        A string representing the computer's guess.
        It can be one of the following: 'rock', 'paper', or 'scissor'.
    """

    guess_num = random.randint(a=0, b=2)
    if guess_num == 0:
        return 'rock'
    elif guess_num == 1:
        return 'paper'
    else:
        return 'scissor'

def score_board_update(user_win_count: int, computer_win_count: int) -> None:
    """
    Update the score board with the user and computer win counts.
    
    Args:
    -----
    user_win_count : int
        The number of times the user has won.
    computer_win_count : int
        The number of times the computer has won.
        
    Returns:
    -------
    None
    """

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
        COMPUTER_WIN += 1
        result_game.config(text='Latest result: You Lose!!!!', bg='red', fg='white')
    else:
        USER_WIN += 1
        result_game.config(text='Latest result: You win the Game!!!!', bg='green', fg='white')
        print('*'*66)
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
