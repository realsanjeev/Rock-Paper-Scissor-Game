let userScore = 0;
let computerScore = 0;
const userScore_span = document.getElementById("user-score");
const computerScore_span = document.getElementById("computer-score");

const scoreBoard = document.querySelector(".score-board");
const result = document.querySelector('.result');
// creating variable for choice
const rock = document.getElementById('rock');
const paper = document.getElementById('paper');
const scissor = document.getElementById('scissor');

function getComputerChoice(){
    const choices = ['rock','paper','scissor'];
    // making random choices using index which is randomly generated
    const randomNumber = Math.floor(Math.random() *3);
    return choices[randomNumber]
}

function win(userChoice, computerChoice) {
    // making subscript for better user interaction
    const smallUserWord = 'user'.fontsize(3).substring();
    const smallComputerWord = 'Computer'.fontsize(3).substring();

    userScore++;
    userScore_span.innerHTML = userScore;
    computerScore_span.innerHTML = computerScore;
    // result.innerHTML = userChoice + ' beats ' + computerChoice + ' You Win..';
    result.innerHTML = `${userChoice}${smallUserWord} beats ${computerChoice}${smallComputerWord}.
                      You Win..`;
    //   Adding Css Effect after user makes choice
    document.getElementById(userChoice).classList.add('green-glow')
    document.getElementById(computerChoice).classList.add('red-glow')
    // Removing effect after fixed settime
    setTimeout(function(){document.getElementById(userChoice).classList.remove('green-glow')}, 1000)
    setTimeout(function(){document.getElementById(computerChoice).classList.add('red-glow')}, 1000)
}

function lose(userChoice, computerChoice){
    const smallUserWord = 'user'.fontsize(3).substring();
    const smallComputerWord = 'Computer'.fontsize(3).substring();

    computerScore++;
    userScore_span.innerHTML = userScore;
    computerScore_span.innerHTML = computerScore;
    // Showing result in html page
    result.innerHTML = `${userChoice}${smallUserWord} loses to ${computerChoice}${smallComputerWord}.  You Lose..`;

    document.getElementById(computerChoice).classList.add('green-glow')
    document.getElementById(userChoice).classList.add('red-glow')

    setTimeout(function(){document.getElementById(computerChoice).classList.remove('green-glow')}, 1000)
    setTimeout(function(){document.getElementById(userChoice).classList.remove('red-glow')}, 1000)
}

function draw(userChoice, computerChoice){
    const smallUserWord = 'user'.fontsize(3).substring();
    const smallComputerWord = 'Computer'.fontsize(3).substring();
    result.innerHTML = `${userChoice}${smallUserWord} equals ${computerChoice}${smallComputerWord}.  Game is Draw.. `;
    
    document.getElementById(computerChoice).classList.add('gray-glow')
    document.getElementById(userChoice).classList.add('gray-glow')

    setTimeout(function(){document.getElementById(userChoice).classList.remove('gray-glow')}, 1000)
    setTimeout(function(){document.getElementById(userChoice).classList.remove('gray-glow')}, 1000)
}

function game(userChoice){
    const computerChoice = getComputerChoice();
    console.log('User choice => '+ userChoice)
    console.log('Computer choice =>' + computerChoice)
    switch (userChoice + computerChoice) {
        case 'rockscissor':
        case 'paperrock':
        case 'scissorpaper':
            win(userChoice, computerChoice);
            break;
        case 'rockpaper':
        case 'paperscissor':
        case 'scissorrock':
            lose(userChoice, computerChoice);
            break;
        case 'rockrock':
        case 'paperpaper':
        case 'scissorscissor':
            draw(userChoice, computerChoice);
            break;


    }
}

function main(){
    rock.addEventListener('click', function(){
        game('rock');
    })
    // function called and ddefined in another way
    paper.addEventListener('click', e => game('paper'));

    scissor.addEventListener('click', e => game('scissor') );
}

main();