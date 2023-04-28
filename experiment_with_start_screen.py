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

bird = Bird((int(1/3 * SCREEN_WIDTH), int(3/5 * SCREEN_HEIGHT)), 0, 0)
bird_group = pygame.sprite.Group(bird)
board = Board(BOARD_POS)
board_group = pygame.sprite.Group(board)
achievement = Medal(ACHIEVEMENT_POS, 20)
achievement_group = pygame.sprite.Group(achievement)
points = Points(POINTS_POS, 20)
points_group = pygame.sprite.Group(points)
best = Best(BEST_POS, 50)
best_group = pygame.sprite.Group(best)
word = Word(WORD_POS)
word_group = pygame.sprite.Group(word)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    background_group.update()
    bird_group.update()
    board_group.update()
    achievement_group.update(20)
    points_group.update()
    best_group.update()
    word_group.update()
    screen.fill(SCREEN_COLOR)
    background_group.draw(screen)
    bird_group.draw(screen)
    board_group.draw(screen)
    achievement_group.draw(screen)
    points_group.draw(screen)
    best_group.draw(screen)
    word_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)