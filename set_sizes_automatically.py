import pygame, sys
import random
from constants import *
from classes import *

# SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 350
# NUMBER_OF_PIPES = 8
# PIPE_SIZE = PIPE_WIDTH, PIPE_HEIGHT = int(SCREEN_WIDTH / NUMBER_OF_PIPES * 1/3), 350
# HEART_SIZE = HEART_WIDTH, HEART_HEIGHT = 20, 20
# GAP_WIDTH, GAP_HEIGHT = int(SCREEN_WIDTH / NUMBER_OF_PIPES - PIPE_WIDTH), int(SCREEN_HEIGHT * 1/7)
# FPS = 80
# SCREEN_COLOR = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)


# class Background(pygame.sprite.Sprite):
#     def __init__(self, pos):
#         super(Background, self).__init__()

#         self.image = pygame.image.load('images/background.jpg')

#         self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

#         self.rect = self.image.get_rect()

#         self.rect.topleft = pos

#     def update(self):
#         pass


# class UpperPipe(pygame.sprite.Sprite):
#     def __init__(self, pos, velocity):
#         super(UpperPipe, self).__init__()

#         self.image = pygame.transform.rotate(pygame.image.load(
# 		'images/pipe.png'), 180)

#         self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

#         self.rect = self.image.get_rect()

#         self.rect.topleft = pos

#         self.velocity = velocity

#     def update(self):
#         self.rect.move_ip(self.velocity, 0)


# class LowerPipe(pygame.sprite.Sprite):
#     def __init__(self, pos, velocity):
#         super(LowerPipe, self).__init__()

#         self.image = pygame.image.load('images/pipe.png')

#         self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

#         self.rect = self.image.get_rect()

#         self.rect.topleft = pos

#         self.velocity = velocity

#     def update(self):
#         self.rect.move_ip(self.velocity, 0)


# class Heart(pygame.sprite.Sprite):
#     def __init__(self, pos, velocity):
#         super(Heart, self).__init__()

#         self.image = pygame.image.load('images/heart.png')

#         self.image = pygame.transform.scale(self.image, (HEART_WIDTH, HEART_HEIGHT))

#         self.rect = self.image.get_rect()

#         self.rect.center = pos

#         self.velocity = velocity

#     def update(self):
#         self.rect.move_ip(self.velocity, 0)


clock = pygame.time.Clock()
clock.tick(FPS)

background = Background((0, 0))
background_group = pygame.sprite.Group(background)
pipe_group = pygame.sprite.Group()
pipes = []
heart_group = pygame.sprite.Group()
hearts = []


for i in range(NUMBER_OF_PIPES+1):
    upper_bottom = random.randrange(10, SCREEN_HEIGHT-GAP_HEIGHT-10)
    upper_pipe = UpperPipe((SCREEN_WIDTH+i*(GAP_WIDTH + PIPE_WIDTH), upper_bottom-PIPE_HEIGHT), -1)
    lower_pipe = LowerPipe((SCREEN_WIDTH+i*(GAP_WIDTH+PIPE_WIDTH), upper_bottom+GAP_HEIGHT), -1)

    pipe_group.add(upper_pipe, lower_pipe)
    pipes.append(upper_pipe)
    pipes.append(lower_pipe)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if pipes[0].rect.right < 0:
        pipe_group.remove(pipes.pop(0))
        pipe_group.remove(pipes.pop(0))

        upper_bottom = random.randrange(10, SCREEN_HEIGHT-GAP_HEIGHT-10)
        upper_pipe = UpperPipe((SCREEN_WIDTH + GAP_WIDTH, upper_bottom-PIPE_HEIGHT), -1)
        lower_pipe = LowerPipe((SCREEN_WIDTH + GAP_WIDTH, upper_bottom+GAP_HEIGHT), -1)
 
        pipe_group.add(upper_pipe, lower_pipe)
        pipes.append(upper_pipe)
        pipes.append(lower_pipe)

        for heart in hearts:
            if heart.rect.left < -1:
                hearts.remove(heart)
                heart_group.remove(heart)

        if random.random() < 0.4:
            heart = Heart((SCREEN_WIDTH+GAP_WIDTH+PIPE_WIDTH+1/2*GAP_WIDTH, random.randrange(HEART_HEIGHT, SCREEN_HEIGHT-HEART_HEIGHT)), -1)
            heart_group.add(heart)
            hearts.append(heart)
        

    background_group.update()
    pipe_group.update()
    heart_group.update()
    screen.fill(SCREEN_COLOR)
    background_group.draw(screen)
    pipe_group.draw(screen)
    heart_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)