import pygame 
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),(int(self.position.x), int(self.position.y)), self.radius, 2 )
     
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_velocity1 *= 1.2
            new_velocity2 *= 1.2
            Asteroid(x=self.position.x, y=self.position.y, radius=new_radius,velocity=new_velocity1)
            Asteroid(x=self.position.x, y=self.position.y, radius=new_radius,velocity=new_velocity2)
           