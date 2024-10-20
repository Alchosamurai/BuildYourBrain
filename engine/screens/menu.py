import pygame
import settings
from elements.Background import Background
from elements.Text import Text
from elements.Button import Button
from sound import BgSound
from sound import BtnSound

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.image_path = 'data/images/screens/main_menu.png'
        self.background = Background(self.screen, self.image_path)
        self.sound = BgSound('data/sounds/music/bg1.mp3')
        self.sound.play()

        self.play_btn = Button(self.screen,
            'ИГРАТЬ',
            settings.WIDTH / 2 - 80,
            settings.HEIGHT / 2 + 100,
            50,
        )

    def render(self):
        self.background.render()
        self.play_btn.render()
    
    def control(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_btn.rect.collidepoint(event.pos):
                BtnSound().play()
                return 'switch_scene', 'listing'
        
        return '', ''
    def event(self, event):
        if event.type == pygame.QUIT:
            return False
    
    def exit(self):
        self.sound.stop()

