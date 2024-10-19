import pygame
from elements.Background import Background
from elements.Text import Text

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.image_path = 'data/images/screens/main_menu.png'
        self.background = Background(self.screen, self.image_path)
        

    def render(self):
        self.background.render()

    def event(self, event):
        if event.type == pygame.QUIT:
            return False
