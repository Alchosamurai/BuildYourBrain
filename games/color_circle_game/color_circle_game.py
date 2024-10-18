from games.cleaner import Cleaner
import os
import time
import random

class ColorCircleGame:
    def __init__(self):
        self.color_dict = {0: '🟥', 1: '🟩', 2: '🟦', 3: '🟨'}
        self.__circles = []
        self.__score = 0
    
    def generate_circles(self,size:int):
        self.__circles = [random.randint(0, 3) for _ in range(size)]
    
    def count_circles(self, color:int):
        result = sum([1 for c in self.__circles if c == color])
        return result
    def check_circles(self, color:int, answer:int):
        if self.count_circles(color) == answer:
            return True
        return False
    def print_circles(self):
        for i in range(len(self.__circles)):
            print(self.color_dict[self.__circles[i]], end = ' ')
        print()
    
    def print_score(self):
        print(f'Ваш счет - {self.__score}')

    def play_game(self, count:int = 10):
        self.generate_circles(count)
        while True:
            self.print_circles()
            current_color = random.randint(0, 3)
            time.sleep(count/2)
            Cleaner.clear()
            print(f'Cколько было {self.color_dict[current_color]} ?')
            color = int(input())
            if self.check_circles(current_color, color):
                self.__score += 1
                print('Правильный ответ! Продолжаем!')
                self.generate_circles(count)
                time.sleep(1)
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

    game = ColorCircleGame()
    game.play_game()

if __name__ == "__main__":
    main()