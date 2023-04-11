import pygame
import random


pygame.init()

width, height = 500, 500
BLOCK_SIZE = 10
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pygame.display.set_caption("Snake")

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 5


def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, white, [x[0], x[1], 10, 10])


def generate_food():
    food_x = round(random.randint(0, width// BLOCK_SIZE - 1 ) )
    food_y = round(random.randint(0, height // BLOCK_SIZE - 1))
    return [food_x, food_y]


def draw_food(food_position):
    pygame.draw.rect(screen, red, [food_position[0], food_position[1], BLOCK_SIZE, BLOCK_SIZE])

def loose():
    screen.fill('red')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True

x = width / 2
y = height / 2
x_change = 0
y_change = 0

food_position = generate_food()

snake_body = []
length_of_snake = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change != BLOCK_SIZE:
                x_change = -BLOCK_SIZE
                y_change = 0
            elif event.key == pygame.K_RIGHT and x_change != -BLOCK_SIZE:
                x_change = BLOCK_SIZE
                y_change = 0
            elif event.key == pygame.K_UP and y_change != BLOCK_SIZE:
                y_change = -BLOCK_SIZE
                x_change = 0
            elif event.key == pygame.K_DOWN and y_change != -BLOCK_SIZE:
                y_change = BLOCK_SIZE
                x_change = 0
    x += x_change
    y += y_change

    draw_food(food_position)

    snake_head = [x, y]
    snake_body.append(snake_head)
    if len(snake_body) > length_of_snake:
        del snake_body[0]
    draw_snake(snake_body)
    for block in snake_body[:-1]:
        if block == snake_head:
            game = False
            loose()
    if (x > width - 5 or x < 0) or (y > height - 5 or y < 0):
        game = False
        loose()
    pygame.display.update()
    if x == food_position[0] and y == food_position[1]:
        food_position = generate_food()
        length_of_snake += 1
        if (length_of_snake - 1) % 10 == 0:
            fps += 8


    clock.tick(fps)

    screen.fill(black)

    pygame.display.flip()
