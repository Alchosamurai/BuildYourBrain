import pygame
import random
import settings as settings
from router import Router

#* Game settings ------------------------------------------------------------
WIDTH = settings.WIDTH 
HEIGHT = settings.HEIGHT
FPS = settings.FPS 

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(settings.TITLE)
pygame.display.set_icon(pygame.image.load(settings.ICON_PATH))
clock = pygame.time.Clock()
#* end Game settings --------------------------------------------------------
# Цикл игры
current_scene = Router(screen=screen).go_to_menu()
running = True
while running:
    clock.tick(FPS)
    current_scene.render()
    
    pygame.display.update()
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
