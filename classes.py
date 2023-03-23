import pygame, sys
import random
from constants import *


class Background(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Background, self).__init__()

        self.image = pygame.image.load('images/background.jpg')

        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.topleft = pos

    def update(self):
        pass


class UpperPipe(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super(UpperPipe, self).__init__()

        self.image = pygame.transform.rotate(pygame.image.load(
		'images/pipe.png'), 180)

        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.topleft = pos

        self.velocity = velocity

    def update(self):
        self.rect.move_ip(self.velocity, 0)


class LowerPipe(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super(LowerPipe, self).__init__()

        self.image = pygame.image.load('images/pipe.png')

        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.topleft = pos

        self.velocity = velocity

    def update(self):
        self.rect.move_ip(self.velocity, 0)


class Heart(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super(Heart, self).__init__()

        self.image = pygame.image.load('images/heart.png')

        self.image = pygame.transform.scale(self.image, (HEART_WIDTH, HEART_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.center = pos

        self.velocity = velocity

    def update(self):
        self.rect.move_ip(self.velocity, 0)


class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, velocity, acceleration):
        super(Bird, self).__init__()

        self.image = pygame.image.load('images/bird.png')

        self.image = pygame.transform.scale(self.image, (BIRD_WIDTH, BIRD_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.center = pos

        self.velocity = velocity

        self.acceleration = acceleration

    def update(self):
        self.rect.move_ip(0, self.velocity)
        self.velocity = self.velocity + self.acceleration

    def flap(self):
        self.velocity = BIRD_VELOCITY

    def is_hit(self):
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            return True
        else:
            return False