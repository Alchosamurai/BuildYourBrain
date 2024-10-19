import pygame
import sys
class InputBox:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (255, 255, 255)
        self.text = ''
        self.active = False
        self.font = pygame.font.Font(None, 32)
    
    def get_text(self):
        return self.text
    
    def clear_text(self):
        self.text = ''

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active  # Переключаем активность поля
            else:
                self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:  # Нажатие Enter
                try:
                    number = int(self.text)  # Преобразуем текст в число
                    print(f"Введенное число: {number}")  # Выводим число в консоль
                except ValueError:
                    print("Пожалуйста, введите корректное число.")
                # Сбрасываем текст после ввода
            elif event.key == pygame.K_BACKSPACE:  # Удаление символа
                self.text = self.text[:-1]
            else:
                self.text += event.unicode  # Добавление символа

    def draw(self, surface):
        # Отрисовка текстового поля
        pygame.draw.rect(surface, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))