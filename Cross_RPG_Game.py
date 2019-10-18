# Pygame development 1
# Start the basic game set up
# Set up the display

import pygame

pygame.init()

# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SCREEN_TITLE = 'Crossy RPG'

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
pygame.display.set_caption(SCREEN_TITLE)

# Load player image from file directory
player_image = pygame.image.load('player.png')
# Scale the image up
player_image = pygame.transform.scale(player_image, (50, 50))

#Main game loop
while not is_game_over:
    
    # Events usually mouse movement, clicks, exits
    for event in pygame.event.get():

        # if quit event, end the game
        if event.type == pygame.QUIT:
            is_game_over = True
        print(event)
        
        #pygame.draw.rect(game_screen, BLACK, [350, 350, 100, 100])
        #pygame.draw.circle(game_screen, BLACK, (400, 300), 50)

        # Draw the player image on top of the screen at (x, y) position
        game_screen.blit(player_image, (375, 375))

        # Update graphics
        pygame.display.update()
        clock.tick(TICK_RATE)

# Quit pygame and the program
pygame.quit()
quit()