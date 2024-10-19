import pygame
import settings
from elements.Text import Text


class Icon(Text):
    def __init__(self,screen,  x, y, size_w, size_h, img_path):
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__size_w = size_w
        self.__size_h = size_h
        self.__image = pygame.image.load(img_path)
        self.__image = pygame.transform.scale(self.__image, (self.__size_w, self.__size_h))

        self.rect = self.__image.get_rect(topleft=(self.__x, self.__y))

    def render(self):
        self.__screen.blit(self.__image, self.rect)

