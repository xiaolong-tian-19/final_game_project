import pygame, sys
import random

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 499

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

screenColor = (200, 200, 200)


class Background(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Background, self).__init__()

        self.image = pygame.image.load('images/background.jpg')

        self.rect = self.image.get_rect()

        self.rect.topleft = pos

    def update(self):
        pass

class UpperPipe(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super(UpperPipe, self).__init__()

        self.image = pygame.transform.rotate(pygame.image.load(
		'images/pipe.png'), 180)

        self.rect = self.image.get_rect()

        self.rect.topleft = pos

        self.velocity = velocity

    def update(self):
        self.rect.move_ip(self.velocity, 0)

class LowerPipe(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super(LowerPipe, self).__init__()

        self.image = pygame.image.load('images/pipe.png')

        self.rect = self.image.get_rect()

        self.rect.bottomleft = pos

        self.velocity = velocity

    def update(self):
        self.rect.move_ip(self.velocity, 0)

class Pipes():
    def __init__(self):
        pass

framepersecond = 80
framepersecond_clock = pygame.time.Clock()
framepersecond_clock.tick(framepersecond)

def generate_random():
    return int(random.random() * -200)

background = Background((0, 0))
backgrounds = pygame.sprite.Group(background)
group = pygame.sprite.Group()
pipes = []

offset = generate_random()
pipe1 = UpperPipe((600, offset), -1)
height1 = pipe1.rect.height + offset
height2 = height1 + 100 + pipe1.rect.height
pipe2 = LowerPipe((600, height2), -1)

group.add(pipe1, pipe2)


# pipe1 = UpperPipe((600, generate_random()), -1)
# pipe2 = UpperPipe((800, generate_random()), -1)
# pipe3 = UpperPipe((1000, generate_random()), -1)
# pipe4 = UpperPipe((1200, generate_random()), -1)
# pipe5 = UpperPipe((1400, generate_random()), -1)

# group = pygame.sprite.Group()
# group.add(pipe1)
# group.add(pipe2)
# group.add(pipe3, pipe4, pipe5)
# pipes = []
# pipes.append(pipe1)
# pipes.append(pipe2)
# pipes.append(pipe3)
# pipes.append(pipe4)
# pipes.append(pipe5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # if pipes[0].rect.right < -10:
    #     pipe = UpperPipe((800, generate_random()), -1)
    #     group.remove(pipes.pop(0))
    #     pipes.append(pipe)
    #     group.add(pipe)
        

    backgrounds.update()
    group.update()
    screen.fill(screenColor)
    backgrounds.draw(screen)
    group.draw(screen)

    pygame.display.update()
    framepersecond_clock.tick(framepersecond)

