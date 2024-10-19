import pygame
import settings
class Numpad:

    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.Surface((settings.WIDTH/2, settings.HEIGHT/2))
        self.numpad = pygame.image.load('assets/numpad.png')
        self.numpad = pygame.transform.scale(self.numpad, (settings.WIDTH, settings.HEIGHT))