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

# Constants
IMAGE_DIR_PATH = glob.glob('images/*.PNG')
SIZE = (100, 100)
COMPUTER_WIN = 0
USER_WIN = 0

# Initialize main window
root = tk.Tk()
root.title('Rock Paper Scissors')
root.geometry('700x520')
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Set icon
try:
    small_icon = tk.PhotoImage(file="images/icons/icon-16.png")
    large_icon = tk.PhotoImage(file="images/icons/icon-32.png")
    root.iconphoto(True, large_icon)
except Exception as err:
    print(f"[ERROR]: Could not load icon: {err}")

# Fonts & Colors
HEADER_FONT = ("Arial", 28, "bold")
SUB_FONT = ("Arial", 14)
INFO_FONT = ("Arial", 16, "bold")
BG_COLOR = "#1e1e1e"
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#00bcd4"
WIN_COLOR = "#4caf50"
LOSE_COLOR = "#f44336"
DRAW_COLOR = "#ffc107"

# Layout frames
header_frame = tk.Frame(root, bg=BG_COLOR)
header_frame.pack(pady=10)

image_frame = tk.Frame(root, bg=BG_COLOR)
image_frame.pack(pady=20)

footer_frame = tk.Frame(root, bg=BG_COLOR)
footer_frame.pack(pady=10, fill='x')

# Header
tk.Label(header_frame, text='Rock Paper Scissors', font=HEADER_FONT,
         fg=ACCENT_COLOR, bg=BG_COLOR).pack()

score_board = tk.Label(header_frame, text='Computer: 0   User: 0',
                       font=INFO_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
score_board.pack(pady=5)

result_label = tk.Label(header_frame, text='', font=SUB_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
result_label.pack()

choice_label = tk.Label(header_frame, text='', font=SUB_FONT, fg="#cccccc", bg=BG_COLOR)
choice_label.pack()

# Rules label (always shown)
rules_text = (
    "🪨 Rock crushes Scissors\n"
    "📄 Paper covers Rock    \n"
    "✂️ Scissors cut Paper    "
)
rules_label = tk.Label(footer_frame, text=rules_text, font=SUB_FONT,
                       fg="#aaaaaa", bg=BG_COLOR, justify='center')
rules_label.pack(pady=10)

# Game logic
def computer_guess() -> str:
    return random.choice(['rock', 'paper', 'scissor'])

def score_board_update(user_score: int, computer_score: int):
    score_board.config(text=f'Computer: {computer_score}   User: {user_score}')
    if user_score > computer_score:
        score_board.config(fg=WIN_COLOR)
    elif user_score < computer_score:
        score_board.config(fg=LOSE_COLOR)
    else:
        score_board.config(fg=ACCENT_COLOR)

def who_win(user_guess: str):
    global USER_WIN, COMPUTER_WIN
    cpu_guess = computer_guess()

    # Determine result
    if user_guess == cpu_guess:
        result_label.config(text='It\'s a Draw!', fg=DRAW_COLOR)
    elif (user_guess == 'rock' and cpu_guess == 'paper') or \
         (user_guess == 'paper' and cpu_guess == 'scissor') or \
         (user_guess == 'scissor' and cpu_guess == 'rock'):
        COMPUTER_WIN += 1
        result_label.config(text='You Lost!', fg=LOSE_COLOR)
    else:
        USER_WIN += 1
        result_label.config(text='You Won!', fg=WIN_COLOR)

    score_board_update(USER_WIN, COMPUTER_WIN)
    choice_label.config(text=f'You chose: {user_guess.capitalize()}    |    Computer chose: {cpu_guess.capitalize()}')

# Image loader
def load_images(image_paths):
    img_objs = []
    for path in image_paths:
        image = Image.open(path)
        image.thumbnail(SIZE)
        img_objs.append(ImageTk.PhotoImage(image))
    return img_objs

# Load images and set buttons
imgs = load_images(IMAGE_DIR_PATH)

btn_config = {
    'activebackground': ACCENT_COLOR,
    'bg': BG_COLOR,
    'bd': 0
}

rock_btn = tk.Button(image_frame, image=imgs[1], command=lambda: who_win('rock'), **btn_config)
rock_btn.grid(row=0, column=0, padx=30)

paper_btn = tk.Button(image_frame, image=imgs[0], command=lambda: who_win('paper'), **btn_config)
paper_btn.grid(row=0, column=1, padx=30)

scissor_btn = tk.Button(image_frame, image=imgs[2], command=lambda: who_win('scissor'), **btn_config)
scissor_btn.grid(row=0, column=2, padx=30)

if __name__ == "__main__":
    root.mainloop()
