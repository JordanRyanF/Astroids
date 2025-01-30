from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    SHOT_RADIUS = 5
    
    def __init__(self, x, y,velocity):
        super().__init__(x, y, self.SHOT_RADIUS)
        self.velocity = velocity
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),(int(self.position.x), int(self.position.y)),self.SHOT_RADIUS)
    def update(self, dt):
        self.position += self.velocity * dt