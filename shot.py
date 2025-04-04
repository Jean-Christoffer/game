import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "red", (self.position.x, self.position.y), SHOT_RADIUS, width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt
