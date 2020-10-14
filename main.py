import pygame
import math
from queue import PriorityQueue

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH)) # Creating a window of size 800 x 800
pygame.display.set_caption("A* path finding algorithm") # setting a title "A* path finding algorithm"

##############################
#color codes
##############################
RED = (255, 0 ,0)  # RGB value of red
GREEN = (0, 255, 0) # RGB value of green
BLUE = (0, 0, 255) # RGB value of blue 
YELLOW = (255, 255, 0) # RGB value of yellow
WHITE = (255, 255, 255) # RGB value of white
BLACK = (0, 0, 0) # RGB value of black
PURPLE = (128, 0, 128) # RGB value of purple
ORANGE = (255, 156, 0) # RGB value of orange
GREY = (128, 128, 128) # RGB value of grey
TURQUOISE = (64, 224, 208) # RGB value of turquoise

class Spot:
    def __init__ (self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width - width
        self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == PURPLE

    def reset(self):
        self.color == WHITE
    
