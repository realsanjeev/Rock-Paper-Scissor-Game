import pygame
import socket

from game import Game
from connection import Network
from button_handler import Button

pygame.init()
pygame.font.init()

# WINDOW INFO
WIDTH = 650
HEIGHT = 600
WIN_POS_Y = 20
ICON_PATH = "./assets/images/icon.png"
FONT_PATH = "./assets/fonts/iosevka-regular.ttf"
ICON = pygame.image.load(ICON_PATH)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")
pygame.display.set_icon(ICON)

# Define buttons before use
buttons = [
    Button('Rock', 50, 500, (90, 90, 255)),
    Button('Scissors', 250, 500, (255, 90, 90)),
    Button('Paper', 450, 500, (90, 255, 90))
]

def redraw_window(win, game, player):
    '''
    Redraw Window GUI
    '''
    win.fill((24,24,24)) # color 0x181818
    color_revealed = (255, 255, 255)
    color_locked = (255, 215, 0)
    color_waiting = (150, 150, 150)

    if not game.connection():
        font = pygame.font.SysFont('comicsans', 70)
        text = font.render('Waiting for player...!', 1, (0, 200, 255))
        # Calculate the position to center the text
        text_x = (WIDTH - text.get_width()) // 2
        text_y = (HEIGHT - text.get_height()) // 2
        win.blit(text, (text_x, text_y))
    else:
        font = pygame.font.SysFont('comicsans', 50)
        your_move_text = font.render('Your Move', 1, (0, 255, 255))
        opponent_text = font.render('Opponent', 1, (0, 255, 255))

        your_move_x = (WIDTH // 4) - (your_move_text.get_width() // 2)
        opponent_x = (3 * WIDTH // 4) - (opponent_text.get_width() // 2)

        win.blit(your_move_text, (your_move_x, 200))
        win.blit(opponent_text, (opponent_x, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.action():
            text1 = font.render(move1, 1, color_revealed)
            text2 = font.render(move2, 1, color_revealed)
        else:
            if game.p1_action and player == 0:
                text1 = font.render(move1, 1, color_revealed)
            elif game.p1_action:
                text1 = font.render('Locked In!', 1, color_locked)
            else:
                text1 = font.render('Waiting....', 1, color_waiting)

            if game.p2_action and player == 1:
                text2 = font.render(move2, 1, color_revealed)
            elif game.p2_action:
                text2 = font.render('Locked In!', 1, color_locked)
            else:
                text2 = font.render('Waiting...', 1, color_waiting)

        text1_x = (WIDTH // 4) - (text1.get_width() // 2)
        text2_x = (3 * WIDTH // 4) - (text2.get_width() // 2)

        if player == 1:
            win.blit(text2, (text1_x, 350))
            win.blit(text1, (text2_x, 350))
        else:
            win.blit(text1, (text1_x, 350))
            win.blit(text2, (text2_x, 350))

        for btn in buttons:
            btn.draw(win)

    pygame.display.update()

def main():
    '''
    Main game function
    '''
    session = True
    clock = pygame.time.Clock()
    network = Network()
    
    player = int(network.getid())
    pygame.display.set_caption(f"Player: {player}")

    while session:
        clock.tick(60)
        try:
            game = network.send('get')
        except socket.error as err:
            session = False
            print(f"[ERROR]: Couldn't get game from socket due to: {err}")
            break

        if game.action():
            redraw_window(win, game, player)
            pygame.time.delay(600)
            font = pygame.font.SysFont('comicsans', 45)
            winner = game.winner()

            try:
                game = network.send('reset')
            except socket.error as err:
                session = False
                print(f"Couldn't send `reset` to the socket due to: {err}")
                break

            if winner == -1:
                text = font.render('Round not completed', 1, (255, 0, 128))
            elif winner == 2:
                text = font.render('Tie Game!!!', 1, (255, 0, 0))
            elif winner == player:
                text = font.render('You won!!!', 1, (255, 180, 0))
            else:
                text = font.render('You Lost!', 1, (255, 0, 0))

            win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(3000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                session = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in buttons:
                    if btn.click(pos) and game.connection():
                        if player == 0:
                            if not game.p1_action:
                                network.send(btn.text)
                        else:
                            if not game.p2_action:
                                network.send(btn.text)

        redraw_window(win, game, player)

def menu_screen():
    '''
    Menu screen function
    '''
    session = True
    clock = pygame.time.Clock()

    while session:
        clock.tick(50)
        win.fill((24, 24, 24))
        font = pygame.font.SysFont('comicsans', 75)
        intro_text = "Click to Play "
        text = font.render(intro_text, 1, (255, 0, 0))
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                session = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                session = False
    main()

while True:
    menu_screen()
