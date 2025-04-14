let userScore = 0;
let computerScore = 0;
const userScore_span = document.getElementById("user-score");
const computerScore_span = document.getElementById("computer-score");

const result = document.querySelector('.result');
const finalEvaluation = document.querySelector('.Final-Result');

const rock = document.getElementById('rock');
const paper = document.getElementById('paper');
const scissors = document.getElementById('scissors');

// Convert string to title case
function titleCase(str) {
    str = str.toLowerCase().split(' ');
    for (let i = 0; i < str.length; i++) {
        str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1);
    }
    return str.join(' ');
}

function getComputerChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    const randomNumber = Math.floor(Math.random() * 3);
    return choices[randomNumber];
}

function win(userChoice, computerChoice) {
    const smallUserWord = '<span class="small-label">User</span>';
    const smallComputerWord = '<span class="small-label">Computer</span>';

    userScore++;
    userScore_span.innerHTML = userScore;
    result.innerHTML = `${titleCase(userChoice)}${smallUserWord} beats ${titleCase(computerChoice)}${smallComputerWord}. <br>You Win!`;

    document.getElementById(userChoice).classList.add('green-glow');
    document.getElementById(computerChoice).classList.add('red-glow');

    setTimeout(() => {
        document.getElementById(userChoice).classList.remove('green-glow');
        document.getElementById(computerChoice).classList.remove('red-glow');
    }, 1000);

    document.getElementById("action-message").innerHTML = "Make Your move"; // Reset message
}

function lose(userChoice, computerChoice) {
    const smallUserWord = '<span class="small-label">User</span>';
    const smallComputerWord = '<span class="small-label">Computer</span>';

    computerScore++;
    computerScore_span.innerHTML = computerScore;
    result.innerHTML = `${titleCase(userChoice)}${smallUserWord} loses to ${titleCase(computerChoice)}${smallComputerWord}. <br>You Lose.`;

    document.getElementById(userChoice).classList.add('red-glow');
    document.getElementById(computerChoice).classList.add('green-glow');

    setTimeout(() => {
        document.getElementById(userChoice).classList.remove('red-glow');
        document.getElementById(computerChoice).classList.remove('green-glow');
    }, 1000);

    document.getElementById("action-message").innerHTML = "Make Your move"; // Reset message
}

function draw(userChoice, computerChoice) {
    const smallUserWord = '<span class="small-label">User</span>';
    const smallComputerWord = '<span class="small-label">Computer</span>';

    result.innerHTML = `${titleCase(userChoice)}${smallUserWord} equals ${titleCase(computerChoice)}${smallComputerWord}. <br>It's a Draw.`;

    document.getElementById(userChoice).classList.add('gray-glow');
    document.getElementById(computerChoice).classList.add('gray-glow');

    setTimeout(() => {
        document.getElementById(userChoice).classList.remove('gray-glow');
        document.getElementById(computerChoice).classList.remove('gray-glow');
    }, 1000);

    document.getElementById("action-message").innerHTML = "Make Your move";
}

function game(userChoice) {
    const computerChoice = getComputerChoice();
    switch (userChoice + computerChoice) {
        case 'rockscissors':
        case 'paperrock':
        case 'scissorspaper':
            win(userChoice, computerChoice);
            break;
        case 'rockpaper':
        case 'paperscissors':
        case 'scissorsrock':
            lose(userChoice, computerChoice);
            break;
        case 'rockrock':
        case 'paperpaper':
        case 'scissorsscissors':
            draw(userChoice, computerChoice);
            break;
    }
}

function main() {
    rock.addEventListener('click', () => game('rock'));
    paper.addEventListener('click', () => game('paper'));
    scissors.addEventListener('click', () => game('scissors'));
}

main();
