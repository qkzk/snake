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
    draw_food()
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


def draw_food():
    food_rect = Rect((CASE * food[0], CASE * food[1]), (CASE, CASE))
    screen.draw.filled_rect(food_rect, 'RED')
    screen.draw.rect(food_rect, 'BLACK')


def update():
    global count, snake, food, direction
    if count % 20 == 0:
        count = 0
        victory = (len(snake) == MAX_SNAKE)
        if victory:
            print("WIN !")
        game_over = is_dead(snake) or victory
        if game_over:
            snake = init_snake()
            food = init_food()
            direction = init_direction()
        eat = (snake[0] == food)
        if eat:
            # print("eat")
            food = random_food()
        snake = move_snake(snake, eat=eat)

    count += 1
    check_keys()


def check_keys():
    global direction
    if keyboard.right and direction in ([0, 1], [0, -1]):
        direction = [1, 0]
    if keyboard.left and direction in ([0, 1], [0, -1]):
        direction = [-1, 0]
    if keyboard.up and direction in ([1, 0], [-1, 0]):
        direction = [0, -1]
    if keyboard.down and direction in ([1, 0], [-1, 0]):
        direction = [0, 1]


def random_food():
    x = snake[0][0]
    y = snake[0][1]
    while [x, y] in snake:
        x = randint(0, WIDTH_BOX - 1)
        y = randint(0, HEIGHT_BOX - 1)
    return [x, y]


def is_dead(snake):
    head = snake[0]
    if head[0] < 0 or head[0] >= WIDTH_BOX:
        return True
    if head[1] < 0 or head[1] >= HEIGHT_BOX:
        return True
    if head in snake[1:]:
        return True
    return False


def calc_head():
    tete = snake[0]
    return [tete[0] + direction[0], tete[1] + direction[1]]


def move_snake(snake, eat=False):
    if not eat:
        del snake[-1]
    return [calc_head()] + snake


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
