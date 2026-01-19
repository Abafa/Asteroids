import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = updatable, drawable
    Asteroid.containers = updatable, drawable, asteroids
    Shot.containers = updatable, drawable, shots
    player = Player(x, y)  


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()

        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
