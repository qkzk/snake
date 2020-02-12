import pgzrun
from random import randint


def init_snake():
    return [[3, 0], [2, 0], [1, 0]]


def init_direction():
    return [1, 0]


def init_food():
    return [7, 0]


def draw():
    draw_grid()
    pass


def draw_grid():
    for i in range(WIDTH_BOX):
        for j in range(HEIGHT_BOX):
            r = Rect((i * CASE, j * CASE), (CASE, CASE))
            screen.draw.rect(r, 'WHITE')


def update():
    pass


# globals
count = 0
snake = init_snake()
food = init_food()
direction = init_direction()

# constants
CASE = 60
WIDTH_BOX = 8
HEIGHT_BOX = 6
MAX_SNAKE = WIDTH_BOX * HEIGHT_BOX
WIDTH = WIDTH_BOX * CASE
HEIGHT = HEIGHT_BOX * CASE

pgzrun.go()
