import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
def main():
    pygame.init()
    
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (update_group,draw_group)
    Asteroid.containers = (asteroids, update_group, draw_group)
    AsteroidField.containers = (update_group)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for sprite in update_group:
            sprite.update(dt)
        
        for sprite in asteroids:
            if sprite.collision(player):
                sys.exit("Game over!")
        
        for sprite in draw_group:
            sprite.draw(screen)

        pygame.display.flip() 
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()