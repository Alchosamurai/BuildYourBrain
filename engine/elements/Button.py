import pygame
import settings
from elements.Text import Text


class Button(Text):
    def __init__(self,screen, text, x, y, size=20, color=(255, 255, 255)):
        self.__screen = screen
        self.__text = text
        self.__x = x
        self.__y = y
        self.__size = size
        self.__color = color
        self.__font = pygame.font.Font(settings.FONT, self.__size)
        self.__render = self.__font.render(self.__text, True, self.__color)
        self.rect = self.__render.get_rect(topleft=(self.__x, self.__y))

    def render(self):
        self.__screen.blit(self.__render, self.rect)

    