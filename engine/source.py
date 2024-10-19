import pygame
import random
import settings as settings
from router import Router

#* Game settings ------------------------------------------------------------
WIDTH = settings.WIDTH 
HEIGHT = settings.HEIGHT
FPS = settings.FPS 


current_scene = Router.current_scene()

clock = pygame.time.Clock()
#* end Game settings --------------------------------------------------------
# Цикл игры
running = True
while running:

    clock.tick(FPS)
    if Router.need_to_change:
        current_scene = Router.current_scene()
    current_scene.render()
    pygame.display.flip()
    for event in pygame.event.get():
        action, arg = current_scene.control(event)
        if action == 'switch_scene':
            Router.change_scene(arg)
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
