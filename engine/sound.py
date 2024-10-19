import pygame
import settings
import random

class BgSound:
    def __init__(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound(self.path)

    def play(self):
        if settings.IS_SOUND:
            self.sound.play(loops=-1)

    def stop(self):
        self.sound.stop()

class BtnSound:
    def __init__(self):
        self.sounds = [
            'data/sounds/buttons/btn1.mp3',
            'data/sounds/buttons/btn2.mp3',
            'data/sounds/buttons/btn3.mp3'
        ]

    def play(self):
        if settings.IS_SOUND:
            self.sound = pygame.mixer.Sound(random.choice(self.sounds))
            self.sound.play()