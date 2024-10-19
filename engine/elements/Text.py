import pygame
import settings

class Text:
    def __init__(self, text, x, y, size=20, color=(255, 255, 255)):
        self.__text = text
        self.__x = x
        self.__y = y
        self.__size = size
        self.__color = color
        self.__font = pygame.font.Font(settings.FONT, self.__size)
        self.__render = self.__font.render(self.__text, True, self.__color)

    def render(self):
        return self.__render

    def update_text(self, text):
        self.__text = text
        self.__render = self.__font.render(self.__text, True, self.__color)
    
    def update_color(self, color):
        self.__color = color
        self.__render = self.__font.render(self.__text, True, self.__color)
    
    def update_size(self, size):
        self.__size = size
        self.__render = self.__font.render(self.__text, True, self.__color)

    def update_position(self, x, y):
        self.__x = x
        self.__y = y
        self.__render = self.__font.render(self.__text, True, self.__color)

    def hide(self):
        self.__render = None