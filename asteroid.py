from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_vectors = [self.velocity.rotate(random_angle),
                       self.velocity.rotate(-random_angle)]
        new_radii = [self.radius - ASTEROID_MIN_RADIUS,
                     self.radius - ASTEROID_MIN_RADIUS]
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radii[0])
        new_asteroid_1.velocity = new_vectors[0]
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radii[1])
        new_asteroid_2.velocity = new_vectors[1]