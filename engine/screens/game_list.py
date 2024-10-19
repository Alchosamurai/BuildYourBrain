import pygame
import settings
from elements.Background import Background
from elements.Text import Text
from elements.Button import Button
from sound import BgSound
from sound import BtnSound

class Listing:
    def __init__(self, screen):
        self.screen = screen
        screen.fill((0, 0, 0))
        # self.image_path = 'data/images/screens/main_menu.png'
        # self.background = Background(self.screen, self.image_path)
        self.sound = BgSound('data/sounds/music/bg2.mp3')
        self.sound.play()

        self.fibonachi_button = Button(self.screen,
            'Фибоначчи',
            settings.WIDTH / 2 - 130,
            settings.HEIGHT / 2 - 100,
            50,
        )

    def render(self):
        self.fibonachi_button.render()
    
    def control(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.fibonachi_button.rect.collidepoint(event.pos):
                BtnSound().play()
                return 'switch_scene', 'fibonachi'
        return '', ''

    def event(self, event):
        if event.type == pygame.QUIT:
            return False
    
    def exit(self):
        self.sound.stop()

