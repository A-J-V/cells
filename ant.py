import numpy as np
import random
from scipy.ndimage import convolve
import pygame
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


class Ant:
    def __init__(self,
                 size: int,
                 display,
                 tile_size: int = 10,
                 cell_color=WHITE,
                 ) -> None:
        self.size = size // tile_size
        self.state = np.zeros(shape=(self.size, self.size))
        self.state[self.size//2 - 3:self.size//2 + 3,
                   self.size//2 - 3:self.size//2 + 3] = np.random.randint(2, size=(6, 6))

        self.row_loc = self.size//2
        self.col_loc = self.size//2
        self.dir = random.choice(['n', 's', 'e', 'w'])
        self.tile_size = tile_size
        self.display = display
        self.cell_color = cell_color
        self.dir_map = ({'n': (-1, 0), 's': (1, 0), 'e': (0, 1), 'w': (0, -1)})
        self.clockwise_map = ({'n': 'e', 'e': 's', 's': 'w', 'w': 'n'})
        self.counter_map = ({'e': 'n', 's': 'e', 'w': 's', 'n': 'w'})

    def iterate(self):
        if not 0 < self.row_loc < self.size or not 0 < self.col_loc < self.size:
            return False
        is_on = self.state[self.row_loc, self.col_loc].item()
        if is_on:
            self.dir = self.clockwise_map[self.dir]
        else:
            self.dir = self.counter_map[self.dir]
        self.state[self.row_loc, self.col_loc] = 1 if is_on == 0 else 0
        self.row_loc += self.dir_map[self.dir][0]
        self.col_loc += self.dir_map[self.dir][1]

    def draw(self):
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.state[col, row] == 0:
                    continue
                rect = pygame.Rect(row * self.tile_size, col * self.tile_size, self.tile_size - 1, self.tile_size - 1)
                color = self.cell_color if self.state[col, row] == 1 else BLACK
                self.display.fill(color=color, rect=rect)
