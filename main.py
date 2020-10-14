import pygame
import math
from queue import PriorityQueue

WIDTH = 800
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

