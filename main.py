import game_of_life
import pygame
import time
import random
BLACK = (0, 0, 0)
SIZE = 1000
TILE_SIZE = 10

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Cells")
    display = pygame.display.set_mode((SIZE, SIZE))
    display.fill(BLACK)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    game = game_of_life.GameOfLife(size=SIZE,
                                   display=display,
                                   tile_size=TILE_SIZE,
                                   cell_color=(r, g, b))
    while True:
        time.sleep(0.1)
        game.display.fill((b//10, r//10, g//10))
        game.iterate()
        game.draw()
        pygame.display.update()
