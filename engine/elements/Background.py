import pygame


class Background:
    def __init__(self, screen, background):
        self.screen = screen
        self.screen.fill((0, 0, 0))
        self.background = pygame.image.load(background)

    def render(self):
        self.screen.blit(self.background, (0, 0))
