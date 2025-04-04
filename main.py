import pygame

from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from player import Player

GAME_RUNNING = True


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    time = pygame.time.Clock()
    dt = 0

    y = SCREEN_HEIGHT / 2
    x = SCREEN_WIDTH / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    while GAME_RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        time.tick(60)
        dt = time.get_time() / 1000

        updatable.update(dt)


print("Starting Asteroids!")
print("Screen width:", SCREEN_WIDTH)
print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
