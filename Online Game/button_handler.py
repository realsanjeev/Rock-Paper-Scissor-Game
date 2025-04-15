'''
Modern Button Handler with enhanced visual effects
'''
import pygame

class Button:
    '''
    Modern Button Handler with glassmorphism and hover effects
    '''
    def __init__(self, text, pos_x, pos_y, color, emoji=''):
        '''
        Args:
            text: str -> Text inside button
            pos_x: int -> X coordinate for button
            pos_y: int -> Y coordinate for button
            color: tuple -> RGB color of button
            emoji: str -> Emoji to display on button
        '''
        self.text = text
        self.emoji = emoji
        self.x = pos_x
        self.y = pos_y
        self.base_color = color
        self.color = color
        self.width = 140
        self.height = 90
        self.hovered = False
        self.hover_scale = 1.0
        self.target_scale = 1.0

    def draw(self, win):
        '''
        Draw modern button with glassmorphism effect
        '''
        # Smooth hover animation
        self.hover_scale += (self.target_scale - self.hover_scale) * 0.2
        
        # Calculate scaled dimensions
        scale = self.hover_scale
        scaled_width = int(self.width * scale)
        scaled_height = int(self.height * scale)
        scaled_x = self.x + (self.width - scaled_width) // 2
        scaled_y = self.y + (self.height - scaled_height) // 2
        
        # Create button surface with alpha for glassmorphism
        button_surface = pygame.Surface((scaled_width, scaled_height), pygame.SRCALPHA)
        
        # Draw semi-transparent background
        if self.hovered:
            alpha = 180
            border_width = 3
        else:
            alpha = 120
            border_width = 2
        
        # Rounded rectangle background
        pygame.draw.rect(button_surface, (*self.color, alpha), 
                        (0, 0, scaled_width, scaled_height), 
                        border_radius=15)
        
        # Border with glow effect
        border_color = tuple(min(c + 40, 255) for c in self.color)
        pygame.draw.rect(button_surface, (*border_color, 200), 
                        (0, 0, scaled_width, scaled_height), 
                        width=border_width, border_radius=15)
        
        win.blit(button_surface, (scaled_x, scaled_y))
        
        # Draw text and emoji
        try:
            font_emoji = pygame.font.SysFont('Segoe UI Emoji', 32)
            font_text = pygame.font.SysFont('Arial', 18, bold=True)
        except:
            font_emoji = pygame.font.SysFont('Arial', 32)
            font_text = pygame.font.SysFont('Arial', 18, bold=True)
        
        # Emoji
        if self.emoji:
            emoji_render = font_emoji.render(self.emoji, True, (255, 255, 255))
            emoji_x = scaled_x + (scaled_width - emoji_render.get_width()) // 2
            emoji_y = scaled_y + 15
            win.blit(emoji_render, (emoji_x, emoji_y))
        
        # Text
        text_render = font_text.render(self.text, True, (255, 255, 255))
        text_x = scaled_x + (scaled_width - text_render.get_width()) // 2
        text_y = scaled_y + scaled_height - 30
        win.blit(text_render, (text_x, text_y))

    def click(self, pos):
        '''
        Return True if button is clicked and update hover state
        '''
        pos_x = pos[0]
        pos_y = pos[1]
        
        # Check if mouse is over button
        is_over = (self.x <= pos_x <= self.x + self.width) and \
                  (self.y <= pos_y <= self.y + self.height)
        
        # Update hover state
        if is_over:
            self.hovered = True
            self.target_scale = 1.1
            return True
        else:
            self.hovered = False
            self.target_scale = 1.0
            return False
    
    def update_hover(self, pos):
        '''
        Update hover state without clicking
        '''
        pos_x = pos[0]
        pos_y = pos[1]
        
        is_over = (self.x <= pos_x <= self.x + self.width) and \
                  (self.y <= pos_y <= self.y + self.height)
        
        if is_over:
            self.hovered = True
            self.target_scale = 1.08
        else:
            self.hovered = False
            self.target_scale = 1.0
