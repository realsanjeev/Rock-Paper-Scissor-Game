# Rock Paper Scissors Game
This is a simple web-based game of Rock, Paper, Scissors built using JavaScript. The game allows the user to select one of the three options and compete against the computer. The scores are updated based on the outcome of each round and the final winner is determined at the end of the game.

## How to run
1. Clone or download the repository.
```
git clone git@github.com:realsanjeev/Rock-Paper-Scissor-Game.git
```
2. Open the index.html file in your web browser.
3. Start playing the game!

## How to Play
1. Open the game in your web browser.
2. Click on the option you want to choose (rock, paper, or scissor).
3. The computer will make its choice and the result of the round will be displayed on the screen.
4. The scores will be updated based on the outcome of the round.
5. Play multiple rounds until one player reaches the winning score.
## Implementation Details
This game was implemented using HTML, CSS, and JavaScript. The following JavaScript functions were used:

- `titleCase(str)`: This function takes a string as input and converts it to title case.
- `getComputerChoice()`: This function generates a random choice for the computer.
- `win(userChoice, computerChoice)`: This function updates the score and displays the result of the round when the user wins.
- `lose(userChoice, computerChoice)`: This function updates the score and displays the result of the round when the user loses.
- `draw(userChoice, computerChoice)`: This function displays the result of the round when there is a draw.
- `game(userChoice)`: This function takes the user's choice and the computer's choice and determines the outcome of the round based on the rules of Rock, Paper, Scissors.
- `finalWinner()`: This function determines the final winner of the game based on the scores.


