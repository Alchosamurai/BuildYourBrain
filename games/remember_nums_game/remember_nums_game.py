import os
import random
import time
import sys
from games.cleaner import Cleaner
class RememberNumsGame:
    def __init__(self):
        self.__nums = []
        self.__score = 0
    
    def generate_num(self):
        self.__nums.append(random.randint(0, 9))
    
    def get_nums_str(self):
        return ''.join([str(num) for num in self.__nums])
    
    def check_num(self, num:str):
        if str(num) == self.get_nums_str():
            return True
        return False
    
    def upp_score(self):
        self.__score += 1
    
    def sleep(self):
        if self.__score < 10:
            time.sleep(2)
        elif self.__score < 20:
            time.sleep(5)
        elif self.__score < 30:
            time.sleep(15)
        else:
            time.sleep(20)

    def reset_game(self):
        self.__nums = []
        self.__score = 0
        self.generate_num()
    
    def game_rule(self):
        print('На экране на короткое время будет появляться последовательность чисел')
        print('Необходимо ввести эту последовательность по памяти (без пробелов)')
        print('С каждым разом последовательность будет увеличиваться на 1')
        print('Приятной игры!')

    def play_game(self):
        self.game_rule()
        self.generate_num()
        while True:
            print(f'Текущая последовательность - {self.get_nums_str()}')
            self.sleep()
            Cleaner.clear()
            print('Введите последовательность')
            num = input()
            if self.check_num(num):
                self.upp_score()
                print('Правильный ответ! Продолжаем!')
                time.sleep(3)
                self.generate_num()
                Cleaner.clear()
            else:
                print('Вы проиграли')
                print(f'Ваш счет - {self.__score}')
                time.sleep(1)
                print('Сыграть снова? (y/n)')
                answer = input()
                if answer == 'y':
                    self.reset_game()
                else:
                    break

def main():

    game = RememberNumsGame()
    game.play_game()

if __name__ == "__main__":
    main()
