# snake is bugged (fix it)

import pygame
from pygame.locals import *

pygame.init()

TITLE = 'Snake'
WIDTH, HEIGHT = 500, 500
CLOCK = pygame.time.Clock()
FPS = 60
DT = 0

# colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
pygame.display.set_caption(TITLE)

def render():
    pygame.display.flip()
    pygame.display.update()
    SCREEN.fill(black)
    #render objects

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    input = pygame.key.get_pressed()
    if input[K_ESCAPE]:
        run = False
        pygame.quit()

snake_block = 10
snake_speed = 15


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        # [rect] is position (x) and size (snake_block)
        pygame.draw.rect(SCREEN, green, [x[0], x[1], snake_block, snake_block]) #x[0], x[1] = x, y


run = True
while run:
    events()
    render()

    CLOCK.tick(FPS)
    DT = CLOCK.tick(FPS) / 1000

    # initial position and snake coordinates
    x1 = CENTER_X
    y1 = CENTER_Y

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    #movement
    input = pygame.key.get_pressed()
    if input[K_LEFT]:
        x1_change = -snake_block
        y1_change = 0
    elif input[K_RIGHT]:
        x1_change = snake_block
        y1_change = 0
    elif input[K_UP]:
        y1_change = -snake_block
        x1_change = 0
    elif input[K_DOWN]:
        y1_change = snake_block
        x1_change = 0
    
    # update snake coordinates on screen
    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
        print("game over")
        x1, y1 = CENTER_X, CENTER_Y
    x1 += x1_change
    y1 += y1_change

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    print(x1, y1, snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0] # deletes tail

    draw_snake(snake_block, snake_list)

    pygame.display.update()