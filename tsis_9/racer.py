import random

import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Street Racer v0')
background = pygame.image.load("images/AnimatedStreet.png")
moneta_font = pygame.font.SysFont("Verdana",30)
SCORE = 0
MONETA = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('images/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(0, WIDTH - self.rect.width),
            self.rect.height // 2,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE

        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 0.0001
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH - self.rect.width)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('images/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x >= self.speed:
            self.rect.x -= self.speed
        if pressed[pygame.K_RIGHT] and self.rect.x + self.rect.width + self.speed <= WIDTH:
            self.rect.x += self.speed


class Coins(pygame.sprite.Sprite):  # класс монеток

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/image_part_001.png')
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(24, WIDTH - 24), random.randint(24, HEIGHT - 24))

    def update(self):
        global SCORE


        self.rect.x = random.randint(0, WIDTH - self.rect.width)

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.speed += 0.1
            self.rect.y = 0



    def draw(self, surface):  # отрисовка
        surface.blit(self.image, self.rect)

def main():
    running = True
    global MONETA
    player = Player()
    enemy = Enemy()
    coin = Coins()

    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    coins = pygame.sprite.Group()
    coins.add(coin)

    while running:
        SCREEN.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        player.draw(SCREEN)
        enemy.draw(SCREEN)
        coin.draw(SCREEN)

        player.update()
        enemy.update()
        coin.move()

        moneta = moneta_font.render(f" Your moneta: {str(MONETA)}", True, (0, 0, 0))
        SCREEN.blit(moneta, (0, 0))

        if pygame.sprite.spritecollideany(player, enemies):
            running = False

        if pygame.sprite.spritecollideany(player, coins):
            MONETA += 1
            coin.update()

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()