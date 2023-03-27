import pygame

pygame.init()

screen_width = 640
screen_height = 480

ball_size = (50, 50)
ball_radius = 25

screen = pygame.display.set_mode((screen_width, screen_height))

background_color = (255, 255, 255)

ball_color = (255, 0, 0)

ball_x = screen_width // 2
ball_y = screen_height // 2

movement_speed = 20


def draw_ball():
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)



running = True
while running:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= movement_speed
            elif event.key == pygame.K_DOWN:
                ball_y += movement_speed
            elif event.key == pygame.K_LEFT:
                ball_x -= movement_speed
            elif event.key == pygame.K_RIGHT:
                ball_x += movement_speed

            if ball_x - ball_radius < 0:
                ball_x = ball_radius
            elif ball_x + ball_radius > screen_width:
                ball_x = screen_width - ball_radius
            if ball_y - ball_radius < 0:
                ball_y = ball_radius
            elif ball_y + ball_radius > screen_height:
                ball_y = screen_height - ball_radius

    draw_ball()

    pygame.display.update()

pygame.quit()
