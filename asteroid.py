from random import uniform

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "red", (self.position.x, self.position.y), self.radius, width=2
        )

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = uniform(20, 50)
        scaling_factor = 1.2

        new_velocity1 = self.velocity.rotate(random_angle) * scaling_factor
        new_velocity2 = self.velocity.rotate(-random_angle) * scaling_factor

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_astro1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_astro2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_astro1.velocity = new_velocity1
        new_astro2.velocity = new_velocity2

        for group in self.containers:  # Iterate over sprite groups in the tuple
            group.add(new_astro1)
            group.add(new_astro2)

    def update(self, dt):
        self.position += self.velocity * dt
