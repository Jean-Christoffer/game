import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from player import Player
from shot import Shot

GAME_RUNNING = True


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    time = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while GAME_RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        dt = time.tick(60) / 1000.0


print("Starting Asteroids!")
print("Screen width:", SCREEN_WIDTH)
print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
