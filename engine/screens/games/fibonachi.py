import pygame
import settings
from elements.Background import Background
from elements.Text import Text
from elements.Button import Button
from sound import BgSound
from sound import BtnSound

class Fibonachi:
    def __init__(self, screen):
        self.screen = screen
        screen.fill((0, 0, 0))
        # self.image_path = 'data/images/screens/main_menu.png'
        # self.background = Background(self.screen, self.image_path)
        self.sound = BgSound('data/sounds/music/bg3.mp3')
        self.sound.play()

        self.text = Text(self.screen, 'Числа Фибоначчи', 100, 30)
        self.current_num = 1
        self.current_num_text = Text(self.screen, str(self.current_num), 100, 100)

        self.plus_btn = Button(self.screen, '+', settings.WIDTH / 2 - 80, settings.HEIGHT / 2 + 100, 50)

    def render(self):
        self.screen.fill((0, 0, 0))
        self.text.render()
        self.current_num_text.render()
        self.plus_btn.render()
    
    def control(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.plus_btn.rect.collidepoint(event.pos):
                BtnSound().play()
                self.current_num += 1
                self.current_num_text.update_text(str(self.current_num))
            #При нажатии кнопки мышки/пальцем по экрану вызывается клавиатура

        return '', ''

    def exit(self):
        self.sound.stop()