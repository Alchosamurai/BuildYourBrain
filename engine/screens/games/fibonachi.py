import pygame
import settings
from elements.Background import Background
from elements.Text import Text
from elements.Button import Button
from elements.icon import Icon
from elements.InputBox import InputBox
from sound import BgSound
from sound import BtnSound
from sound import ErrorSound
import time

class Fibonachi:
    def __init__(self, screen):
        self.screen = screen
        screen.fill((0, 0, 0))
        self.game = FibonachiGame()

        # self.image_path = 'data/images/screens/main_menu.png'
        # self.background = Background(self.screen, self.image_path)
        self.sound = BgSound('data/sounds/music/bg3.mp3')
        self.sound.play()
        self.back = Icon(self.screen, 20, 20, 50, 50, 'data/images/back.png')
        self.text = Text(self.screen, 'Числа Фибоначчи', 100, 30)
        self.current_num = 1
        self.current_num_text = Text(self.screen, str(self.game.get_actual_num()), 100, 100)
        self.user_answer = ''
        self.plus_btn = Button(self.screen, '+', settings.WIDTH / 2 - 80, settings.HEIGHT / 2 + 100, 50)
        self.input = InputBox(settings.WIDTH / 2 - 80, settings.HEIGHT / 2 - 50, 160, 32)

        self.lose = False
        self.lose_text = Text(self.screen, f'Вы проиграли!\n Счет: {self.game.get_score()}', 100, 100)

        

    

    def render(self):
        self.screen.fill((0, 0, 0))
        self.input.draw(self.screen)
        self.text.render()
        self.current_num_text.render()
        self.plus_btn.render()
        if self.lose:
            self.screen.fill((0, 0, 0))
            self.lose_text.render()
        self.back.render()
    
    def next_turn(self):
        if self.game.check(int(self.user_answer)):
            self.user_answer = ''
            self.current_num_text.update_text(str(self.game.get_actual_num()))
        else: 
            self.lose = True
            ErrorSound().play()
            self.lose_text.update_text(f'Вы проиграли!\n Счет: {self.game.get_score()}')
        
    
    def control(self, event):
        self.input.handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.plus_btn.rect.collidepoint(event.pos):
                BtnSound().play()
                self.current_num += 1
                self.current_num_text.update_text(str(self.current_num))
            if self.back.rect.collidepoint(event.pos):
                BtnSound().play()
                return 'switch_scene', 'listing'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Нажатие Enter
                    try:
                        self.user_answer = self.input.get_text()
                        self.input.clear_text()
                        self.next_turn()
                    except ValueError:
                        print("Пожалуйста, введите корректное число.")
                    
            #При нажатии кнопки мышки/пальцем по экрану вызывается клавиатура

        return '', ''

    def exit(self):
        self.sound.stop()

class FibonachiGame:
    def __init__(self):
        self.__nums = [1,2]
        self.__default_value = [1,2]
        self.__score = 0
    def next(self):
        self.__nums[0], self.__nums[1] = self.__nums[1], self.__nums[0] + self.__nums[1]
    def upp_score(self):
        self.__score += 1
    
    def get_actual_num(self):
        return self.__nums[1]
    def get_score(self):
        return self.__score
    def check(self, num):
        if num == self.__nums[1] + self.__nums[0]:
            self.upp_score()
            self.next()
            return True
        return False
    def reset_game(self):
        self.__nums = self.__default_value
        self.__score = 0    
    def game_rule(self):
        print('Для игры необходимо вводить последовательность чисел фибоначи')
        print('Для примера возьмем самое начало - 0 и 1 ')
        print(' 0 + 1 = 1, теперь последние элементы ряда - 1 и 1 ')
        print(' 1 + 1 = 2, теперь последние элементы ряда - 1 и 2 ')
        print('Продолжайте игру')
    
    