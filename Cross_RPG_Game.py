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

############### GAME CLASS ##################

class Game:

    #Rate of 60 like FPS
    TICK_RATE = 60 
    
    # Constructor for game class w/ width, height, and title
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Creates window of specified size and set the game window color
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE)
        pygame.display.set_caption(SCREEN_TITLE)

    def run_game_loop(self):
        is_game_over = False
        direction = 0


        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy_0 = NonPlayerCharacter('enemy.png', 20, 600, 50, 50)
        enemy_1 = NonPlayerCharacter('enemy.png', 30, 400, 50, 50)
        enemy_2 = NonPlayerCharacter('enemy.png', 40, 200, 50, 50)
        treasure = GameObject('treasure.png', 375, 50, 50, 50)

        #Main game loop
        while not is_game_over:
            
            # Events usually mouse movement, clicks, exits
            for event in pygame.event.get():

                # if quit event, end the game
                if event.type == pygame.QUIT:
                    is_game_over = True

                # Detect when key is pressed down
                elif event.type == pygame.KEYDOWN:
                # Move up if up key is pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                # Move down if down key pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Detect when key is released
                elif event.type == pygame.KEYUP:
                # Stop movement when key no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

                print(event)

            # Redraw the screen to imitate animation
            self.game_screen.fill(WHITE)
            # Update player position
            player_character.move(direction, self.height)
            # Draw player at new position
            player_character.draw(self.game_screen)

            # Move/Draw enemy
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)
            enemy_1.move(self.width)
            enemy_1.draw(self.game_screen)
            enemy_2.move(self.width)
            enemy_2.draw(self.game_screen)

            treasure.draw(self.game_screen)

            enemies = [enemy_0, enemy_1, enemy_2]
            if player_character.detect_collision(treasure):
                is_game_over = True
            else:
                for enemy in enemies:
                    if player_character.detect_collision(enemy):
                        is_game_over = True

            # Update graphics
            pygame.display.update()
            clock.tick(self.TICK_RATE)

############### GAME OBJECT CLASS ##################

# Generic game object class to be subclassed by other objects in the game
class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # Scale image
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    # Draw the object by blitting it onto game screen
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

############### PLAYER CHARACTER CLASS ##################

# Class to represent the character controlled by the player
class PlayerCharacter(GameObject):

    # Tiles to move per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
    
    # Move function will move character up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        #stop player from going past bottom
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40
    
    # return false (no collision) if x/y do not overlap and true otherwise
    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True

############### ENEMY CHARACTER CLASS ##################

# Class to represent enemy
class NonPlayerCharacter(GameObject):
    # Tiles per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move character right once it hits the far left and vice versa
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

# Quit pygame and the program
pygame.quit()
quit()