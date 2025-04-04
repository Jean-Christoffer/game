import pygame

from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)

GAME_RUNNING = True


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while GAME_RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()


print("Starting Asteroids!")
print("Screen width:", SCREEN_WIDTH)
print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
