import pygame, sys
import random

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 350
PIPE_SIZE = PIPE_WIDTH, PIPE_HEIGHT = 30, 200
HEART_SIZE = HEART_WIDTH, HEART_HEIGHT = 20, 20

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

screenColor = (200, 200, 200)


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


class Heart(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super(Heart, self).__init__()

        self.image = pygame.image.load('images/heart.png')

        self.image = pygame.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect()

        self.rect.bottomleft = pos

        self.velocity = velocity

    def update(self):
        self.rect.move_ip(self.velocity, 0)



framepersecond = 80
framepersecond_clock = pygame.time.Clock()
framepersecond_clock.tick(framepersecond)

def generate_random():
    return int(random.random() * -200)

gap = 150

room = 100

background = Background((0, 0))
backgrounds = pygame.sprite.Group(background)
group = pygame.sprite.Group()
pipes = []
hgroup = pygame.sprite.Group()
hearts = []

# heart1 = Heart((200, 300), 0)
# hgroup.add(heart1)

number_of_pipes = SCREEN_WIDTH // gap
for i in range(number_of_pipes):
    # offset = generate_random()
    pipe_height = UpperPipe((0, 0), -1).rect.height
    offset = random.randrange(-4/5 * pipe_height, -1/5 * pipe_height)
    pipe1 = UpperPipe((SCREEN_WIDTH + i * gap, offset), -1)
    height1 = pipe1.rect.height + offset
    height2 = height1 + room + pipe1.rect.height
    pipe2 = LowerPipe((SCREEN_WIDTH + i * gap, height2), -1)
    if random.random() < 0.4:
        heart = Heart((SCREEN_WIDTH + i * gap + 1/2 * gap, random.randrange(10, 300)), -1)
        hgroup.add(heart)
        hearts.append(heart)
    group.add(pipe1, pipe2)
    # hgroup.add(heart)
    # hearts.append(heart)
    pipes.append(pipe1)
    pipes.append(pipe2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if pipes[0].rect.right < -1:
        group.remove(pipes.pop(0))
        group.remove(pipes.pop(0))
        # offset = generate_random()
        offset = random.randrange(-4/5 * pipe_height, -1/5 * pipe_height)
        pipe1 = UpperPipe((SCREEN_WIDTH + 1, offset), -1)
        height1 = pipe1.rect.height + offset
        height2 = height1 + room + pipe1.rect.height
        pipe2 = LowerPipe((SCREEN_WIDTH + 1, height2), -1)
        group.add(pipe1, pipe2)
        pipes.append(pipe1)
        pipes.append(pipe2)

        for heart in hearts:
            if heart.rect.left < -1:
                hearts.remove(heart)
                hgroup.remove(heart)

        if random.random() < 0.4:
            heart = Heart((SCREEN_WIDTH + 1 + 1/2 * gap, random.randrange(10, 300)), -1)
            hgroup.add(heart)
            hearts.append(heart)
        

    backgrounds.update()
    group.update()
    hgroup.update()
    screen.fill(screenColor)
    backgrounds.draw(screen)
    group.draw(screen)
    hgroup.draw(screen)

    pygame.display.update()
    framepersecond_clock.tick(framepersecond)