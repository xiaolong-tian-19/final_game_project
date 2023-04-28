import pygame, sys
import random
from constants import *


class Background(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Background, self).__init__()

        # self.image = pygame.image.load('images/background.jpg')

        self.images = []
        for i in range(319, -1, -1):
            self.images.append(pygame.transform.scale(pygame.image.load("images/frame_" + str(i).zfill(3) + "_delay-0.05s.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)))

        # self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        self.rect.topleft = pos

    def update(self):
        self.index = (self.index+1) % len(self.images)

        self.image = self.images[self.index]


class UpperPipe(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super(UpperPipe, self).__init__()

        prob = random.random()
        num_images = 6

        if prob < 1/num_images:
            self.image = pygame.image.load('images/pipe.png')
        elif prob < 2/num_images:
            self.image = pygame.image.load('images/london-big-ben-removebg.png')
        elif prob < 3/num_images:
            self.image = pygame.transform.rotate(pygame.image.load('images/spikes.png'), 180)
        elif prob < 4/num_images:
            self.image = pygame.image.load('images/crates.png')
        elif prob < 5/num_images:
            self.image = pygame.image.load('images/roller.png')
        else:
            self.image = pygame.image.load('images/tree-trunk-removebg.png')

        self.image = pygame.transform.rotate(self.image, 180)

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

        prob = random.random()
        num_images = 6

        if prob < 1/num_images:
            self.image = pygame.image.load('images/pipe.png')
        elif prob < 2/num_images:
            self.image = pygame.image.load('images/london-big-ben-removebg.png')
        elif prob < 3/num_images:
            self.image = pygame.transform.rotate(pygame.image.load('images/spikes.png'), 180)
        elif prob < 4/num_images:
            self.image = pygame.image.load('images/crates.png')
        elif prob < 5/num_images:
            self.image = pygame.image.load('images/roller.png')
        else:
            self.image = pygame.image.load('images/tree-trunk-removebg.png')


        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.topleft = pos

        self.velocity = velocity

        self.passed = False

    def update(self):
        # self.rect.move_ip(self.velocity, 0)

        # if self.type == FIRE:
        #     self.index = (self.index+1) % len(self.images)
        #     self.image = self.images[self.index]
        #     pos = self.rect.topleft
        #     self.rect = self.image.get_rect()
        #     self.rect.topleft = pos

        self.rect.move_ip(self.velocity, 0)


class Heart(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super(Heart, self).__init__()

        # self.image = pygame.image.load('images/heart.png')
        self.images = []
        for i in range(14):
            self.images.append(pygame.transform.scale(pygame.image.load('images/heart'+str(i)+'-removebg-preview.png'), (HEART_WIDTH, HEART_HEIGHT)))

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

        # self.image = pygame.image.load('images/bird.png')

        # self.image = pygame.transform.scale(self.image, (BIRD_WIDTH, BIRD_HEIGHT))

        self.images = []
        for i in range(4):
            self.images.append(pygame.transform.scale(pygame.image.load('images/frame'+str(i)+'.png'), (BIRD_WIDTH, BIRD_HEIGHT)))

        self.counter = 0
        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        self.rect.center = pos

        self.velocity = velocity

        self.acceleration = acceleration

        self.is_immune = False

        self.immune_time = 3*FPS

        # self.display = True

        self.number_of_lives = 1

        self.score = 0

    def update(self):
        self.counter += 1
        if self.counter % 2 == 0:
            self.index = (self.index+1) % len(self.images)
            self.image = self.images[self.index]
            pos = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = pos

        self.rect.move_ip(0, self.velocity)
        self.velocity = self.velocity + self.acceleration

        if self.is_immune:
            self.immune_time -= 1

        if self.immune_time <= 0:
            self.is_immune = False
            self.immune_time = 3*FPS
            

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
        self.image = self.font.render(f': {player_score}      : {number_of_lives}', True, self.FONT_COLOR)
        self.rect = self.image.get_rect()

        self.rect.topright = (SCREEN_WIDTH, 0)


class Ring(pygame.sprite.Sprite):
    def __init__(self, bird):
        super(Ring, self).__init__()
        self.bird = bird
        
        self.image = pygame.image.load('images/halo-angel-ring.png')
        self.image = pygame.transform.scale(self.image, (RING_WIDTH, RING_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.topleft = self.bird.rect.topleft

    def update(self):
        self.rect.topleft = self.bird.rect.topleft


class Life(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Life, self).__init__()

        self.image = pygame.image.load('images/heart.png')
        self.image = pygame.transform.scale(self.image, (LIFE_WIDTH, LIFE_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.topleft = pos

    def update(self):
        pass


class Medal(pygame.sprite.Sprite):   

    def __init__(self, pos, score):
        super(Medal, self).__init__()

        self.load_image(score)

        self.rect = self.image.get_rect()

        self.rect.topleft = pos

    def load_image(self, score):
        self.score = score

        if self.score < 20:
            self.image = pygame.transform.scale(pygame.image.load('images/bronze-removebg-preview.png'), (MEDAL_WIDTH, MEDAL_HEIGHT))
        elif self.score < 60:
            self.image = pygame.transform.scale(pygame.image.load('images/silver-removebg-preview.png'), (MEDAL_WIDTH, MEDAL_HEIGHT))
        elif self.score < 120:
            self.image = pygame.transform.scale(pygame.image.load('images/gold-removebg-preview.png'), (MEDAL_WIDTH, MEDAL_HEIGHT))
        else:
            self.image = pygame.transform.scale(pygame.image.load('images/light-removebg-preview.png'), (MEDAL_WIDTH, MEDAL_HEIGHT))

    def update(self, score):
        self.load_image(score)

        pos = self.rect.topleft

        self.rect = self.image.get_rect()

        self.rect.topleft = pos


class Board(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Board, self).__init__()

        self.image = pygame.transform.scale(pygame.image.load('images/board.png'), (BOARD_WIDTH, BOARD_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.topleft = pos

    def update(self):
        pass


class Points(pygame.sprite.Sprite):
    def __init__(self, pos, points):
        super(Points, self).__init__()

        self.FONT_SIZE = 12
        self.FONT_COLOR = (0, 0, 128)

        self.font = pygame.font.Font('freesansbold.ttf', self.FONT_SIZE)

        self.image = self.font.render(f'{points}', True, self.FONT_COLOR)

        self.rect = self.image.get_rect()

        self.rect.topright = pos

    def update(self, points):
        self.image = self.font.render(f'{points}', True, self.FONT_COLOR)

        # self.rect = self.image.get_rect()


class Best(pygame.sprite.Sprite):
    def __init__(self, pos, best):
        super(Best, self).__init__()

        self.FONT_SIZE = 12
        self.FONT_COLOR = (0, 0, 128)

        self.font = pygame.font.Font('freesansbold.ttf', self.FONT_SIZE)

        self.image = self.font.render(f'{best}', True, self.FONT_COLOR)

        self.rect = self.image.get_rect()

        self.rect.topright = pos

    def update(self, best):
        self.image = self.font.render(f'{best}', True, self.FONT_COLOR)



class Word(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Word, self).__init__()

        self.image = pygame.transform.scale(pygame.image.load('images/flappy_word.png'), (WORD_WIDTH, WORD_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.center = pos

    def update(self):
        pass