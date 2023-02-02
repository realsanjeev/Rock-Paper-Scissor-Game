'''
Importing pygame for handling button
'''
import pygame
class Button:
    '''
    Class for Button Handler in Game
    '''
    def __init__(self, text, pos_x, pos_y, color):
        '''
        Args:
            text: str -> Text inside button
            pos_x: int -> X coordinate for button
            pos_y: int -> Y coordinate for button
            color: _Color -> color of button
        '''
        self.text = text
        self.x = pos_x
        self.y = pos_y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        '''
        Draw button in window
        '''
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2),
                                self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        '''
        Return True if button is clicked
        '''
        pos_x = pos[0]
        pos_y = pos[1]
        if (self.x <= pos_x <= self.x+self.width) and (self.y <= pos_y <= self.y+self.height):
            return True
        else:
            return False
