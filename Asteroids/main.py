import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


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

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = updatable, drawable
    Asteroid.containers = updatable, drawable, asteroids
    player = Player(x, y)  


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        updatable.update(dt)

        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
