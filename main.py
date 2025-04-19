import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       
                return
        
        updatable.update(dt)
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.collision(player):
                print("Game Over")
                sys.exit()

        for astoroid in asteroids:
            for shot in shots:
                if astoroid.collision(shot):
                    astoroid.split()
                    shot.kill()


        pygame.display.flip()
        #frame
        dt = (clock.tick(60))/1000

if __name__ == "__main__":
    main()


