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
portal_group = pygame.sprite.Group()
portals = []
score = Score()
score_group = pygame.sprite.Group(score)


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

    if bird.is_immune == False:
        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False):
            bird.is_immune = True
            bird.number_of_lives -= 1
            print("Collide with pipe.")

    if pygame.sprite.groupcollide(bird_group, heart_group, False, True):
        bird.number_of_lives += 1
        print("Obtain additional life.")

    if collisions := pygame.sprite.groupcollide(bird_group, portal_group, False, False):
        if collisions[bird][0].face == Portal.RIGHT:
            pass
        else:
            portal = collisions[bird][0]
            shift = 2*(GAP_WIDTH+PIPE_WIDTH)
            
            # for pipe in pipes:
            #     pipe.rect.left -= 

            for pipe in pipes:
                pipe.rect.left -= shift
            for heart in hearts:
                heart.rect.left -= shift
            for portal in portals:
                portal.rect.left -= shift

            pipe_group.remove(pipes.pop(0))
            pipe_group.remove(pipes.pop(0))
            pipe_group.remove(pipes.pop(0))
            pipe_group.remove(pipes.pop(0))

            last = pipes[len(pipes)-1]
            left = last.rect.left

            for i in range(1,3):
                upper_bottom = random.randrange(10, SCREEN_HEIGHT-GAP_HEIGHT-10)
                upper_pipe = UpperPipe((left+i*(PIPE_WIDTH+GAP_WIDTH), upper_bottom-PIPE_HEIGHT), PIPE_VELOCITY)
                lower_pipe = LowerPipe((left+i*(PIPE_WIDTH+GAP_WIDTH), upper_bottom+GAP_HEIGHT), PIPE_VELOCITY)

                pipe_group.add(upper_pipe, lower_pipe)
                pipes.append(upper_pipe)
                pipes.append(lower_pipe)

            print("Collide with left portal.")

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

        if Portal.COUNTER < 0:
            if random.random() < 0.3:
                heart = Heart((SCREEN_WIDTH+GAP_WIDTH+PIPE_WIDTH+1/2*GAP_WIDTH, random.randrange(HEART_HEIGHT, SCREEN_HEIGHT-HEART_HEIGHT)), HEART_VELOCITY)
                heart_group.add(heart)
                hearts.append(heart)
            elif random.random() < 0.4:
                portal_height = random.randrange(PORTAL_HEIGHT, SCREEN_HEIGHT-PORTAL_HEIGHT)
                enter_portal = Portal((SCREEN_WIDTH+GAP_WIDTH+PIPE_WIDTH+1/2*GAP_WIDTH, portal_height), PORTAL_VELOCITY, Portal.LEFT)
                exit_portal = Portal((SCREEN_WIDTH+GAP_WIDTH+PIPE_WIDTH+1/2*GAP_WIDTH+2*(GAP_WIDTH+PIPE_WIDTH), portal_height), PORTAL_VELOCITY, Portal.RIGHT)
                portal_group.add(enter_portal)
                portal_group.add(exit_portal)
                portals.append(enter_portal)
                portals.append(exit_portal)
                Portal.COUNTER = 2

        Portal.COUNTER -= 1

    for pipe in pipes:
        if pipe.passed == False and type(pipe) == LowerPipe:
            if pipe.rect.right < bird.rect.left:
                pipe.passed = True
                bird.score += 1
        

    background_group.update()
    pipe_group.update()
    heart_group.update()
    portal_group.update()
    bird_group.update()
    score_group.update(bird.score, bird.number_of_lives)
    screen.fill(SCREEN_COLOR)
    background_group.draw(screen)
    pipe_group.draw(screen)
    heart_group.draw(screen)
    portal_group.draw(screen)
    bird_group.draw(screen)
    score_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)