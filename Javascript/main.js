let userScore = 0;
let computerScore = 0;
const userScore_span = document.getElementById("user-score");
const computerScore_span = document.getElementById("computer-score");
const resultMessage = document.getElementById('result-message');
const choicesDisplay = document.getElementById('choices-display');
const resetBtn = document.getElementById('reset-btn');

const rock = document.getElementById('rock');
const paper = document.getElementById('paper');
const scissors = document.getElementById('scissors');

// Convert string to title case
function titleCase(str) {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

// Get computer's random choice
function getComputerChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    const randomNumber = Math.floor(Math.random() * 3);
    return choices[randomNumber];
}

// Remove all glow classes
function removeAllGlows() {
    const choices = document.querySelectorAll('.choice');
    choices.forEach(choice => {
        choice.classList.remove('win-glow', 'lose-glow', 'draw-glow');
    });
}

// Update result message with animation
function updateResultMessage(message, resultType) {
    resultMessage.className = 'result-message';
    resultMessage.classList.add(resultType);
    resultMessage.innerHTML = `<p>${message}</p>`;
}

// Update choices display
function updateChoicesDisplay(userChoice, computerChoice) {
    const choiceEmojis = {
        'rock': '🪨',
        'paper': '📄',
        'scissors': '✂️'
    };
    
    choicesDisplay.innerHTML = `
        You chose ${choiceEmojis[userChoice]} <strong>${titleCase(userChoice)}</strong> 
        | Computer chose ${choiceEmojis[computerChoice]} <strong>${titleCase(computerChoice)}</strong>
    `;
}

// Animate score update
function animateScore(element) {
    element.style.transform = 'scale(1.3)';
    setTimeout(() => {
        element.style.transform = 'scale(1)';
    }, 300);
}

// Win scenario
function win(userChoice, computerChoice) {
    userScore++;
    userScore_span.innerHTML = userScore;
    animateScore(userScore_span);
    
    updateResultMessage('🎉 You Win! 🎉', 'win');
    updateChoicesDisplay(userChoice, computerChoice);

    document.getElementById(userChoice).classList.add('win-glow');
    document.getElementById(computerChoice).classList.add('lose-glow');

    setTimeout(removeAllGlows, 1000);
}

// Lose scenario
function lose(userChoice, computerChoice) {
    computerScore++;
    computerScore_span.innerHTML = computerScore;
    animateScore(computerScore_span);
    
    updateResultMessage('😢 You Lost!', 'lose');
    updateChoicesDisplay(userChoice, computerChoice);

    document.getElementById(userChoice).classList.add('lose-glow');
    document.getElementById(computerChoice).classList.add('win-glow');

    setTimeout(removeAllGlows, 1000);
}

// Draw scenario
function draw(userChoice, computerChoice) {
    updateResultMessage('🤝 It\'s a Draw!', 'draw');
    updateChoicesDisplay(userChoice, computerChoice);

    document.getElementById(userChoice).classList.add('draw-glow');
    document.getElementById(computerChoice).classList.add('draw-glow');

    setTimeout(removeAllGlows, 1000);
}

// Main game logic
function game(userChoice) {
    const computerChoice = getComputerChoice();
    
    // Determine winner using a cleaner approach
    const outcomes = {
        'rockscissors': 'win',
        'paperrock': 'win',
        'scissorspaper': 'win',
        'rockpaper': 'lose',
        'paperscissors': 'lose',
        'scissorsrock': 'lose'
    };
    
    const outcome = outcomes[userChoice + computerChoice];
    
    if (outcome === 'win') {
        win(userChoice, computerChoice);
    } else if (outcome === 'lose') {
        lose(userChoice, computerChoice);
    } else {
        draw(userChoice, computerChoice);
    }
}

// Reset game
function resetGame() {
    userScore = 0;
    computerScore = 0;
    userScore_span.innerHTML = userScore;
    computerScore_span.innerHTML = computerScore;
    
    resultMessage.className = 'result-message';
    resultMessage.innerHTML = '<p>Make your first move!</p>';
    choicesDisplay.innerHTML = '';
    
    removeAllGlows();
    
    // Add reset animation
    resetBtn.style.transform = 'scale(0.9)';
    setTimeout(() => {
        resetBtn.style.transform = 'scale(1)';
    }, 200);
}

// Add smooth transition to score values
userScore_span.style.transition = 'transform 0.3s ease';
computerScore_span.style.transition = 'transform 0.3s ease';

// Event listeners
function main() {
    rock.addEventListener('click', () => game('rock'));
    paper.addEventListener('click', () => game('paper'));
    scissors.addEventListener('click', () => game('scissors'));
    resetBtn.addEventListener('click', resetGame);
    
    // Add keyboard support
    document.addEventListener('keydown', (e) => {
        if (e.key === 'r' || e.key === 'R') game('rock');
        if (e.key === 'p' || e.key === 'P') game('paper');
        if (e.key === 's' || e.key === 'S') game('scissors');
        if (e.key === 'Escape') resetGame();
    });
}

main();
