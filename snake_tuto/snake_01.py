import pgzrun
from random import randint


def init_snake():
    return [[3, 0], [2, 0], [1, 0]]


def init_direction():
    return [1, 0]


def init_food():
    return [7, 0]


def draw():
    screen.fill('BLACK')
    draw_grid()
    draw_snake()


def draw_snake():
    for elt in snake[1:]:
        elt_rect = Rect((CASE * elt[0], CASE * elt[1]), (CASE, CASE))
        screen.draw.filled_rect(elt_rect, 'GREEN')
        screen.draw.rect(elt_rect, 'BLACK')

    tete = snake[0]
    tete_rect = Rect((CASE * tete[0], CASE * tete[1]), (CASE, CASE))
    screen.draw.filled_rect(tete_rect, 'YELLOW')
    screen.draw.rect(tete_rect, 'BLACK')


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
