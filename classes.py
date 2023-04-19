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

        self.passed = False

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

        self.passed = False

    def update(self):
        self.rect.move_ip(self.velocity, 0)


class Heart(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super(Heart, self).__init__()

        # self.image = pygame.image.load('images/heart.png')
        self.images = []
        for i in range(16):
            self.images.append(pygame.transform.scale(pygame.image.load('images/heart'+str(i)+'.png'), (HEART_WIDTH, HEART_HEIGHT)))

        # self.image = pygame.transform.scale(self.image, (HEART_WIDTH, HEART_HEIGHT))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        self.rect.center = pos

        self.velocity = velocity

    def update(self):
        # self.rect.move_ip(self.velocity, 0)

        self.index = (self.index+1) % len(self.images)

        self.image = self.images[self.index]

        pos = self.rect.center

        self.rect = self.image.get_rect()

        self.rect.center = pos

        self.rect.move_ip(self.velocity, 0)


class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, velocity, acceleration):
        super(Bird, self).__init__()

        self.image = pygame.image.load('images/bird.png')
        # self.original_image = pygame.image.load('images/bird.png')
        # self.original_image = pygame.transform.scale(self.original_image, (BIRD_WIDTH, BIRD_HEIGHT))
        
        # self.images = []
        # self.images.append(pygame.transform.scale(pygame.image.load('images/bird.png'), (BIRD_WIDTH, BIRD_HEIGHT)))
        # self.images.append(pygame.transform.scale(pygame.image.load('images/nothing.png'), (BIRD_WIDTH, BIRD_HEIGHT)))
        # self.images.append(pygame.image.load('images/nothing.png'))

        self.image = pygame.transform.scale(self.image, (BIRD_WIDTH, BIRD_HEIGHT))

        # self.index = 0

        # self.image = self.images[0]

        self.rect = self.image.get_rect()

        self.rect.center = pos

        self.velocity = velocity

        self.acceleration = acceleration

        self.is_immune = False

        self.immune_time = 10*FPS

        # self.display = True

        self.number_of_lives = 1

        self.score = 0

    def update(self):
        self.rect.move_ip(0, self.velocity)
        self.velocity = self.velocity + self.acceleration

        if self.is_immune:
            self.immune_time -= 1

        if self.immune_time <= 0:
            self.is_immune = False
            self.immune_time = 10*FPS

        # if self.display:
        #     self.image = self.original_image
        # else:
        #     self.image = None

        # self.display = not self.display
        
        # self.rect = self.image.get_rect()
        

    def flap(self):
        self.velocity = BIRD_VELOCITY

    def is_hit(self):
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            return True
        else:
            return False
        

class Portal(pygame.sprite.Sprite):
    LEFT = 0
    RIGHT = 1
    COUNTER = -1

    def __init__(self, pos, velocity, face):
        super(Portal, self).__init__()

        # self.image = pygame.image.load('images/portal.png')

        self.images = []
        for i in range(8):
            self.images.append(pygame.transform.scale(pygame.image.load('images/tile00'+str(i)+'.png'), (PORTAL_WIDTH, PORTAL_HEIGHT)))

        # self.image = pygame.transform.scale(self.image, (PORTAL_WIDTH, PORTAL_HEIGHT))
        self.index = 0

        self.image = self.images[self.index]

        self.face = face
        if self.face == self.RIGHT:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()

        self.rect.center = pos

        self.velocity = velocity

    def update(self):
        # self.rect.move_ip(self.velocity, 0)

        self.index = (self.index+1) % len(self.images)

        self.image = self.images[self.index]

        pos = self.rect.center

        self.rect = self.image.get_rect()

        self.rect.center = pos

        self.rect.move_ip(self.velocity, 0)


class Score(pygame.sprite.Sprite):

    def __init__(self):
        super(Score, self).__init__()
        self.FONT_SIZE = 32
        self.FONT_COLOR = (0, 0, 128)

        self.font = pygame.font.Font('freesansbold.ttf', self.FONT_SIZE)
        # self.text = self.font.render('GeeksForGeeks', True, self.FONT_COLOR)

    def update(self, player_score, number_of_lives):
        self.image = self.font.render(f'{player_score} : {number_of_lives}', True, self.FONT_COLOR)
        self.rect = self.image.get_rect()

        self.rect.topright = (SCREEN_WIDTH, 0)