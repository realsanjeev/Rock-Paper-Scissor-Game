
# Rock Paper Scissor in GUI
This is a Python script that uses the Tkinter library to create a graphical user interface (GUI) for a game of rock-paper-scissors.
### Install dependencies:
```
pip install pillow
```
## Overview

1. Imports the necessary libraries: `glob`, `random`, `tkinter`, and `PIL`.
1. Defines some constants and variables, including the path to the images used for the game, the size of the images, and the scores for the computer and the user.
1. Creates the main window for the GUI and sets its properties (title, icon, and size).
1. Creates three frames for the GUI: a header frame, an image frame, and a footer frame.
1. Creates a label for the header frame to display the game's title, and another label to display the score.
1. Defines several functions:
    - `computer_guess()`: randomly generates the computer's guess for the game.
    - `score_board_update()`: updates the score board with the current scores.
    - `who_win()`: determines who won the game based on the user's input and the computer's guess, updates the score board, and displays the result and a hint.
    - `image_file()`: loads the images for the game and returns them as a list.
1. Loads the images for the game using the image_file() function and creates buttons for each of the choices (rock, paper, and scissors) using the images.
1. Creates a label for the footer frame to display a hint for the game.
1. Starts the main loop for the GUI.