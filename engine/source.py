import pygame
import random
import settings as settings

WIDTH = settings.WIDTH 
HEIGHT = settings.HEIGHT
FPS = settings.FPS 

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(settings.TITLE)
pygame.display.set_icon(pygame.image.load(settings.ICON_PATH))
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    clock.tick(FPS)


    pygame.display.update()
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
