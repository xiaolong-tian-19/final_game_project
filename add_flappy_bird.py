import pygame, sys
import random
from constants import *
from classes import *
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

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
    upper_pipe = UpperPipe((SCREEN_WIDTH+i*(GAP_WIDTH + PIPE_WIDTH), upper_bottom-PIPE_HEIGHT), PIPE_VELOCITY)
    lower_pipe = LowerPipe((SCREEN_WIDTH+i*(GAP_WIDTH+PIPE_WIDTH), upper_bottom+GAP_HEIGHT), PIPE_VELOCITY)

    pipe_group.add(upper_pipe, lower_pipe)
    pipes.append(upper_pipe)
    pipes.append(lower_pipe)


bird = Bird((int(1/2 * SCREEN_WIDTH), int(1/2 * SCREEN_HEIGHT)), 0, BIRD_ACCELERATION)
bird_group = pygame.sprite.Group(bird)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            bird.flap()

    if pipes[0].rect.right < 0:
        pipe_group.remove(pipes.pop(0))
        pipe_group.remove(pipes.pop(0))

        upper_bottom = random.randrange(10, SCREEN_HEIGHT-GAP_HEIGHT-10)
        upper_pipe = UpperPipe((SCREEN_WIDTH + GAP_WIDTH, upper_bottom-PIPE_HEIGHT), PIPE_VELOCITY)
        lower_pipe = LowerPipe((SCREEN_WIDTH + GAP_WIDTH, upper_bottom+GAP_HEIGHT), PIPE_VELOCITY)
 
        pipe_group.add(upper_pipe, lower_pipe)
        pipes.append(upper_pipe)
        pipes.append(lower_pipe)

        for heart in hearts:
            if heart.rect.left < -1:
                hearts.remove(heart)
                heart_group.remove(heart)

        if random.random() < 0.4:
            heart = Heart((SCREEN_WIDTH+GAP_WIDTH+PIPE_WIDTH+1/2*GAP_WIDTH, random.randrange(HEART_HEIGHT, SCREEN_HEIGHT-HEART_HEIGHT)), HEART_VELOCITY)
            heart_group.add(heart)
            hearts.append(heart)
        

    background_group.update()
    pipe_group.update()
    heart_group.update()
    bird_group.update()
    screen.fill(SCREEN_COLOR)
    background_group.draw(screen)
    pipe_group.draw(screen)
    heart_group.draw(screen)
    bird_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)