import game_of_life
import seeds
import ant
import brain
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
    # game = game_of_life.GameOfLife(size=SIZE,
    #                                display=display,
    #                                tile_size=TILE_SIZE,
    #                                cell_color=(r, g, b))
    # game = seeds.Seeds(size=SIZE,
    #                    display=display,
    #                    tile_size=5,
    #                    cell_color=(r, g, b))
    # game = ant.Ant(size=SIZE,
    #                display=display,
    #                tile_size=TILE_SIZE,
    #                cell_color=(r, g, b))
    game = brain.Brain(size=SIZE,
                       display=display,
                       tile_size=TILE_SIZE,
                       cell_color=(r, g, b))
    while True:
        time.sleep(0.05)
        game.display.fill((b//5, r//5, g//5))
        game.iterate()
        game.draw()
        pygame.display.update()
