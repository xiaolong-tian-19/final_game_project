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


class Bird(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Bird, self).__init__()

        self.image = pygame.image.load('images/bird.png')

        self.image = pygame.transform.scale(self.image, (BIRD_WIDTH, BIRD_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.center = pos

        self.velocity = 0

        self.acceleration = 1

    def update(self):
        self.rect.move_ip(0, self.velocity)
        self.velocity = self.velocity + self.acceleration

    def flap(self):
        self.velocity = -7

    def is_hit(self):
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            return True
        else:
            return False


bird = Bird((int(1/2 * SCREEN_WIDTH), int(1/2 * SCREEN_HEIGHT)))
bird_group = pygame.sprite.Group(bird)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            bird.flap()
			

    background_group.update()
    bird_group.update()
    screen.fill(SCREEN_COLOR)
    background_group.draw(screen)
    bird_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)