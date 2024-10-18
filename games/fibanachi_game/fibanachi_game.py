import os 
import time

class FibanachiGame:
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
    
    def play_game(self):
        self.game_rule()
        while True:
            print(f"Текущее число - {self.get_actual_num()}")
            print("Введите следующее число последовательности")
            num = int(input())
            if self.check(num):
                print("Правильный ответ! Продолжаем!")
                time.sleep(0.7)
                clear()
            else:
                print("Вы проиграли")
                print(f"Ваш счет - {self.__score}")
                time.sleep(1)
                print('Сыграть снова? (y/n)')
                answer = input()
                if answer == 'y':
                    self.reset_game()
                else:
                    break


def main():
    game = FibanachiGame()
    game.play_game()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
