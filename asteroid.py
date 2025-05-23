from circleshape import *
from constants import *
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
        
        new_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(new_angle)
        vec2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = vec1 * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2.velocity = vec2 * 1.2
        
        
