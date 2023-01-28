'''import pygame library'''
import socket
import pygame
from connection import Network
from button_handler import Button

pygame.font.init()
# create window
WIDTH = 600
HEIGHT = 600

WIN_POS_Y = 0
WIN_POS_Y = 20

win = pygame.display.set_mode((WIDTH, HEIGHT), WIN_POS_Y, WIN_POS_Y)
pygame.display.set_caption("Client")

def redraw_window(win, game, player):
    '''
    Game window
    '''
    win.fill((128,128,128))

    if not game.connection():
        font = pygame.font.SysFont('comicsans', 80)
        text = font.render('Waiting for player...!', 1, (255,0,0), True)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont('comicsans', 50)
        text = font.render('Your move', 1, (0,255,255))
        win.blit(text, (80, 200))

        text = font.render('Opponent', 1, (0,255,255))
        win.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.action():
            text1 = font.render(move1, 1, (0,0,0))
            text2 = font.render(move2, 1, (0,0,0))
        else:
            if game.p1Action and player == 0:
                text1 = font.render(move1, 1, (0,0,0))
            elif game.p1Action:
                text1 = font.render('Locked In', 1, (0,0,0))
            else:
                text1 = font.render('Waiting....', 1, (0,0,0))

            if game.p2Action and player == 1:
                text2 = font.render(move2, 1, (0,0,0))
            elif game.p2Action:
                text2 = font.render('Locked in',1, (0,0,0))
            else:
                text2 = font.render('Waiting...',1, (0,0,0))

        if player == 1:
            win.blit(text2, (100,250))
            win.blit(text1, (400,350))
        else:
            win.blit(text1, (100,250))
            win.blit(text2, (400,350))

        for btn in buttons:
            btn.draw(win)

    pygame.display.update()

buttons = [
            Button('Rock',50,500,(0,0,0)),
            Button('Scissors',230,500,(250,0,0)),
            Button('Paper',450,500,(0,255,0))
            ]

def main():
    '''
    main function
    '''
    session = True
    clock = pygame.time.Clock()
    network = Network()
    player = int(network.getid())
    print ('You are a player', player)

    while session:
        clock.tick(60)
        try:
            game = network.send('get')
            print('='*20, game, '='*20)
        except socket.error as err:
            session = False
            print("couldn't get game", err)
            break

        if game.action():
            redraw_window(win, game, player)
            pygame.time.delay(600)
            try:
                game = network.send('reset')
            except socket.error as err:
                session = False
                print("Couldn't get game", err)
                break

            font = pygame.font.SysFont('comicsans', 45)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render('You won!', 1, (255,0,128))
            elif game.winner() == -1:
                text = font.render('Tie Game!', 1, (255,0,0))
            else:
                text = font.render('You Lost!', 1, (255,0,0))

            win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                session =False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in buttons:
                    if btn.click(pos) and game.connection():
                        if player == 0:
                            if not game.p1Action:
                                network.send(btn.text)
                        else:
                            if not game.p2Action:
                                network.send(btn.text)

        redraw_window(win, game, player)

def menu_screen():
    '''
    menu screen function
    '''
    session = True
    clock = pygame.time.Clock()

    while session:
        clock.tick(50)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont('comicsans',75)
        intro_text = '''
        Click to Play
        
        
        '''
        text = font.render(intro_text, 1, (255,0,0))
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                session = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                session = False
    main()

while True:
    menu_screen()
