import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot


class Player(CircleShape):
    containers = ()
    shoot_timer = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.forward = 0
        self.containers

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        rotate_speed = PLAYER_TURN_SPEED * dt

        self.rotation += rotate_speed

    def move(self, dt):
        direction_speed = PLAYER_SPEED * dt

        self.direction += direction_speed

    def shoot(self):
        PLAYER_SHOOT_COOLDOWN = 0.3
        if self.shoot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            forward_position = forward * PLAYER_SPEED * dt
            self.position += forward_position

        if keys[pygame.K_s]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            forward_position = forward * PLAYER_SPEED * dt
            self.position -= forward_position

        if keys[pygame.K_SPACE]:
            self.shoot()
