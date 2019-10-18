# Pygame development 1
# Start the basic game set up
# Set up the display

import pygame

pygame.init()

# Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Clock used to update game events and frames
clock = pygame.time.Clock()
TICK_RATE = 60 #Rate of 60 like FPS
is_game_over = False

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Creates window of specified size and set the game window color
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_screen.fill(WHITE)
