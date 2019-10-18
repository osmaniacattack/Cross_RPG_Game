# Pygame development 1
# Start the basic game set up
# Set up the display

import pygame

# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock used to update game events and frames
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:
    TICK_RATE = 60 #Rate of 60 like FPS
    
    # Constructor for game class w/ width, height, and title
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Creates window of specified size and set the game window color
        self.game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_screen.fill(WHITE)
        pygame.display.set_caption(SCREEN_TITLE)

    def run_game_loop(self):
        is_game_over = False

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
                # game_screen.blit(player_image, (375, 375))

                # Update graphics
                pygame.display.update()
                clock.tick(TICK_RATE)

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

# Quit pygame and the program
pygame.quit()
quit()