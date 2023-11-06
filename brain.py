import numpy as np
from scipy.ndimage import convolve
import pygame
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


class Brain:
    def __init__(self,
                 size: int,
                 display,
                 tile_size: int = 10,
                 cell_color=WHITE,
                 ) -> None:
        self.size = size // tile_size
        self.state = np.zeros(shape=(self.size, self.size))
        self.state[self.size//2 - 6:self.size//2 + 6,
                   self.size//2 - 6:self.size//2 + 6] = np.random.randint(2, size=(12, 12))

        self.kernel = np.array(object=[[1, 1, 1],
                                       [1, 0, 1],
                                       [1, 1, 1]],
                               dtype='int8',
                               )
        self.tile_size = tile_size
        self.display = display
        self.cell_color = cell_color

    def iterate(self):
        convolution = convolve(input=self.state,
                               weights=self.kernel,
                               mode='constant',
                               cval=0.0)
        # We're using a convolution here, so we need to cheat a little to get three categories,
        # alive, dead, and "dying". To do this, instead of using the rule that says a dead cell
        # becomes a live cell if it has exactly two live neighbors, we switch the rule to be if
        # the neighbors add up to between 1.9 and 2.1. Live neighbors count as 1, dying neighbors
        # count as 0.01. Therefore, the outcome is the same, but now we can get it by still only
        # using convolutions.
        self.state = np.where((self.state == 0) & (convolution > 1.9) & (convolution < 2.1), 1,
                              np.where(self.state == 1, 0.01, 0)
                              )

    def draw(self):
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.state[col, row] == 0:
                    continue
                rect = pygame.Rect(row * self.tile_size, col * self.tile_size, self.tile_size - 1, self.tile_size - 1)
                if self.state[col, row] == 1:
                    color = self.cell_color
                else:
                    color = WHITE
                self.display.fill(color=color, rect=rect)
