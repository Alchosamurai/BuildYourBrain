from screens.menu import Menu
from screens.game_list import Listing
from screens.games.fibonachi import Fibonachi
import pygame
import settings

WIDTH = settings.WIDTH
HEIGHT = settings.HEIGHT
class Router:
    scene_dict = {'menu': Menu, 'listing': Listing,
                'fibonachi': Fibonachi}
    need_to_change = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.init()
    pygame.mixer.init()  # для звука
    pygame.display.set_caption(settings.TITLE)
    pygame.display.set_icon(pygame.image.load(settings.ICON_PATH))
    scene_to_change = Menu(screen)


    @classmethod
    def current_scene(cls):
        return cls.scene_to_change

    @classmethod
    def change_scene(cls, scene_name):
        cls.scene_to_change.exit()
        cls.need_to_change = True
        cls.scene_to_change = cls.scene_dict[scene_name](cls.screen)