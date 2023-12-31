import numpy as np
from scipy.ndimage import convolve
import pygame
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


class Seeds:
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
        self.state = np.where((self.state == 0) & (convolution == 2), 1, 0)

    def draw(self):
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.state[col, row] == 0:
                    continue
                rect = pygame.Rect(row * self.tile_size, col * self.tile_size, self.tile_size - 1, self.tile_size - 1)
                self.display.fill(color=self.cell_color, rect=rect)
