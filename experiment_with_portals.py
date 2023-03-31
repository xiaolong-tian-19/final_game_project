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

for i in range(NUMBER_OF_PIPES+1):
    upper_bottom = random.randrange(10, SCREEN_HEIGHT-GAP_HEIGHT-10)
    upper_pipe = UpperPipe((SCREEN_WIDTH+i*(GAP_WIDTH + PIPE_WIDTH), upper_bottom-PIPE_HEIGHT), PIPE_VELOCITY)
    lower_pipe = LowerPipe((SCREEN_WIDTH+i*(GAP_WIDTH+PIPE_WIDTH), upper_bottom+GAP_HEIGHT), PIPE_VELOCITY)

    pipe_group.add(upper_pipe, lower_pipe)
    pipes.append(upper_pipe)
    pipes.append(lower_pipe)


class Portal(pygame.sprite.Sprite):
    LEFT = 0
    RIGHT = 1
    COUNTER = -1

    def __init__(self, pos, velocity, face):
        super(Portal, self).__init__()

        self.image = pygame.image.load('images/portal.png')

        self.image = pygame.transform.scale(self.image, (PORTAL_WIDTH, PORTAL_HEIGHT))

        self.face = face
        if self.face == self.RIGHT:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()

        self.rect.center = pos

        self.velocity = velocity

    def update(self):
        self.rect.move_ip(self.velocity, 0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
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

    background_group.update()
    pipe_group.update()
    heart_group.update()
    portal_group.update()
    screen.fill(SCREEN_COLOR)
    background_group.draw(screen)
    pipe_group.draw(screen)
    heart_group.draw(screen)
    portal_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)