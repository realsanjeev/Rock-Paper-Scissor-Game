import pygame
import socket

from game import Game
from connection import Network
from button_handler import Button

pygame.init()
pygame.font.init()

# MODERN COLOR PALETTE
COLORS = {
    'bg_dark': (15, 12, 41),           # Deep purple-blue background
    'bg_secondary': (26, 22, 64),      # Secondary background
    'accent_primary': (102, 126, 234), # Purple accent
    'accent_secondary': (118, 75, 162), # Deeper purple
    'text_primary': (255, 255, 255),   # White text
    'text_secondary': (184, 184, 209), # Light gray text
    'success': (79, 172, 254),         # Blue for wins
    'danger': (250, 112, 154),         # Pink for losses
    'warning': (255, 215, 0),          # Gold for locked
    'neutral': (150, 150, 150),        # Gray for waiting
    'tie': (255, 193, 7),              # Amber for tie
}

# WINDOW INFO
WIDTH = 700
HEIGHT = 650
ICON_PATH = "./assets/images/icon.png"
FONT_PATH = "./assets/fonts/iosevka-regular.ttf"

try:
    ICON = pygame.image.load(ICON_PATH)
except:
    ICON = None

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors Online")
if ICON:
    pygame.display.set_icon(ICON)

# Define modern buttons
buttons = [
    Button('Rock', 75, 520, COLORS['accent_primary'], '🪨'),
    Button('Paper', 275, 520, COLORS['success'], '📄'),
    Button('Scissors', 475, 520, COLORS['danger'], '✂️')
]

def draw_gradient_rect(surface, color1, color2, rect):
    """Draw a vertical gradient rectangle"""
    for i in range(rect.height):
        ratio = i / rect.height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        pygame.draw.line(surface, (r, g, b), 
                        (rect.x, rect.y + i), 
                        (rect.x + rect.width, rect.y + i))

def draw_card(surface, x, y, width, height, color, alpha=30):
    """Draw a modern card with glassmorphism effect"""
    # Create semi-transparent surface
    card_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    
    # Draw rounded rectangle background
    pygame.draw.rect(card_surface, (*color, alpha), (0, 0, width, height), border_radius=20)
    
    # Draw border
    pygame.draw.rect(card_surface, (*COLORS['text_secondary'], 50), (0, 0, width, height), 
                    width=2, border_radius=20)
    
    surface.blit(card_surface, (x, y))

def redraw_window(win, game, player):
    '''
    Redraw Window GUI with modern design
    '''
    # Draw gradient background
    draw_gradient_rect(win, COLORS['bg_dark'], COLORS['bg_secondary'], 
                      pygame.Rect(0, 0, WIDTH, HEIGHT))

    if not game.connection():
        # Waiting screen with modern design
        draw_card(win, WIDTH//2 - 250, HEIGHT//2 - 100, 500, 200, COLORS['accent_primary'], 40)
        
        # Try to load custom font, fallback to system font
        try:
            font_large = pygame.font.Font(FONT_PATH, 48)
        except:
            font_large = pygame.font.SysFont('Arial', 48, bold=True)
        
        try:
            font_small = pygame.font.Font(FONT_PATH, 20)
        except:
            font_small = pygame.font.SysFont('Arial', 20)
        
        text = font_large.render('Waiting for Opponent', True, COLORS['success'])
        text_x = (WIDTH - text.get_width()) // 2
        text_y = HEIGHT // 2 - 40
        win.blit(text, (text_x, text_y))
        
        # Animated dots
        import time
        dots = '.' * (int(time.time() * 2) % 4)
        subtext = font_small.render(f'Connecting{dots}', True, COLORS['text_secondary'])
        subtext_x = (WIDTH - subtext.get_width()) // 2
        win.blit(subtext, (subtext_x, text_y + 60))
        
    else:
        # Game screen
        try:
            font_title = pygame.font.Font(FONT_PATH, 56)
            font_label = pygame.font.Font(FONT_PATH, 32)
            font_move = pygame.font.Font(FONT_PATH, 48)
        except:
            font_title = pygame.font.SysFont('Arial', 56, bold=True)
            font_label = pygame.font.SysFont('Arial', 32, bold=True)
            font_move = pygame.font.SysFont('Arial', 48, bold=True)

        # Title
        title = font_title.render('Rock Paper Scissors', True, COLORS['accent_primary'])
        title_x = (WIDTH - title.get_width()) // 2
        win.blit(title, (title_x, 30))

        # Player labels with cards
        your_move_text = font_label.render('Your Move', True, COLORS['text_primary'])
        opponent_text = font_label.render('Opponent', True, COLORS['text_primary'])

        # Draw cards for player areas
        draw_card(win, 50, 150, 250, 280, COLORS['accent_primary'], 35)
        draw_card(win, 400, 150, 250, 280, COLORS['danger'], 35)

        # Position labels
        your_move_x = 175 - (your_move_text.get_width() // 2)
        opponent_x = 525 - (opponent_text.get_width() // 2)

        win.blit(your_move_text, (your_move_x, 180))
        win.blit(opponent_text, (opponent_x, 180))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        
        # Emoji mapping
        emoji_map = {
            'Rock': '🪨',
            'Paper': '📄',
            'Scissors': '✂️'
        }
        
        if game.action():
            # Both players have moved - reveal
            text1_str = f"{emoji_map.get(move1, '')} {move1}"
            text2_str = f"{emoji_map.get(move2, '')} {move2}"
            text1 = font_move.render(text1_str, True, COLORS['text_primary'])
            text2 = font_move.render(text2_str, True, COLORS['text_primary'])
        else:
            # Waiting for moves
            if game.p1_action and player == 0:
                text1_str = f"{emoji_map.get(move1, '')} {move1}"
                text1 = font_move.render(text1_str, True, COLORS['success'])
            elif game.p1_action:
                text1 = font_move.render('Locked In!', True, COLORS['warning'])
            else:
                text1 = font_move.render('Waiting...', True, COLORS['neutral'])

            if game.p2_action and player == 1:
                text2_str = f"{emoji_map.get(move2, '')} {move2}"
                text2 = font_move.render(text2_str, True, COLORS['success'])
            elif game.p2_action:
                text2 = font_move.render('Locked In!', True, COLORS['warning'])
            else:
                text2 = font_move.render('Waiting...', True, COLORS['neutral'])

        # Center text in cards
        text1_x = 175 - (text1.get_width() // 2)
        text2_x = 525 - (text2.get_width() // 2)

        if player == 1:
            win.blit(text2, (text1_x, 300))
            win.blit(text1, (text2_x, 300))
        else:
            win.blit(text1, (text1_x, 300))
            win.blit(text2, (text2_x, 300))

        # Draw modern buttons
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
    pygame.display.set_caption(f"Rock Paper Scissors - Player {player + 1}")

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
            
            try:
                font_result = pygame.font.Font(FONT_PATH, 52)
            except:
                font_result = pygame.font.SysFont('Arial', 52, bold=True)
            
            winner = game.winner()

            try:
                game = network.send('reset')
            except socket.error as err:
                session = False
                print(f"Couldn't send `reset` to the socket due to: {err}")
                break

            # Draw result overlay
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            win.blit(overlay, (0, 0))

            if winner == -1:
                text = font_result.render('Round Not Completed', True, COLORS['neutral'])
            elif winner == 2:
                text = font_result.render('🤝 Tie Game!', True, COLORS['tie'])
            elif winner == player:
                text = font_result.render('🎉 You Won!', True, COLORS['success'])
            else:
                text = font_result.render('😢 You Lost!', True, COLORS['danger'])

            # Draw result card
            card_width = text.get_width() + 80
            card_height = text.get_height() + 60
            card_x = (WIDTH - card_width) // 2
            card_y = (HEIGHT - card_height) // 2
            
            draw_card(win, card_x, card_y, card_width, card_height, 
                     COLORS['accent_primary'], 200)
            
            text_x = (WIDTH - text.get_width()) // 2
            text_y = (HEIGHT - text.get_height()) // 2
            win.blit(text, (text_x, text_y))
            
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
        
        # Update button hover effects
        mouse_pos = pygame.mouse.get_pos()
        for btn in buttons:
            btn.update_hover(mouse_pos)

        redraw_window(win, game, player)

def menu_screen():
    '''
    Modern menu screen
    '''
    session = True
    clock = pygame.time.Clock()

    while session:
        clock.tick(50)
        
        # Draw gradient background
        draw_gradient_rect(win, COLORS['bg_dark'], COLORS['bg_secondary'], 
                          pygame.Rect(0, 0, WIDTH, HEIGHT))
        
        try:
            font_title = pygame.font.Font(FONT_PATH, 72)
            font_subtitle = pygame.font.Font(FONT_PATH, 28)
        except:
            font_title = pygame.font.SysFont('Arial', 72, bold=True)
            font_subtitle = pygame.font.SysFont('Arial', 28)
        
        # Draw title card
        draw_card(win, WIDTH//2 - 300, HEIGHT//2 - 200, 600, 400, 
                 COLORS['accent_primary'], 40)
        
        title_text = "Rock Paper Scissors"
        text = font_title.render(title_text, True, COLORS['accent_primary'])
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 120))
        
        subtitle = font_subtitle.render("Online Multiplayer", True, COLORS['text_secondary'])
        win.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, HEIGHT // 2 - 40))
        
        # Animated prompt
        import time
        alpha = int((1 + pygame.math.Vector2(1, 0).rotate(time.time() * 180).x) * 127.5)
        prompt_surface = pygame.Surface((400, 60), pygame.SRCALPHA)
        
        prompt_text = font_subtitle.render("Click to Play", True, (*COLORS['success'], alpha))
        prompt_surface.blit(prompt_text, (200 - prompt_text.get_width() // 2, 15))
        win.blit(prompt_surface, (WIDTH // 2 - 200, HEIGHT // 2 + 60))
        
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
