"""
“Piper Game” using Object-Oriented Programming (OOP) techniques. The sand piper must race the clock to collect as many clams on the beach without getting wet

CSCI150 Lab 10

Name: Sujay Banerjee, Tucker Lamb
Section: A

Creativity:
Added the ability to change the default game time with a command line argument
Increase the difficulty of the game by having the wave move higher and higher up the beach
"""
import pygame
import random
import math
import sys

# Constants to determine the size of the screen
SCREEN_WIDTH  = 500
SCREEN_HEIGHT = 500

# Number of clams to draw at the beginning of the game (or when regenerating)
NUM_CLAMS = 10

# Amount the player should move with each key press
STEP = 50

# Frames-per-second for the game
FPS = 60

class Entity():
    """Base class for all game entities

    You should not ever explicitly create an Entity object, only its child classes should be instantiated.

    Attributes:
        rect: A pygame.Rect that describes the location and size of the entity
    """
    def __init__(self, x, y, width, height):
        """Initialize an Entity

        Args:
            x, y: Initial x,y position for entity
            width: Width of entity's rectangle
            height: Height of entity's rectangle
        """
        self.rect = pygame.Rect(x, y, width, height)
    
    def get_x(self):
        """Return the current x-coordinate"""
        return self.rect.x
    
    def set_x(self, value):
        """Set the x-coordinate to value"""
        self.rect.x = value
    
    def shift_x(self, shift):
        """Shift the x-coordinate by shift (positively or negatively)"""
        self.rect.x += shift
    
    def get_y(self):
        """Return the current y-coordinate"""
        return self.rect.y
    
    def set_y(self, value):
        """Set the y-coordinate to value"""
        self.rect.y = value
    
    def shift_y(self, shift):
        """Shift the y-coordinate by shift (positively or negatively)"""
        self.rect.y += shift
        
        
    def collide(self, other):
        """Checks to see if two objects collided

            Args:
                other: another object
            
            Returns:
                booleans if objects collided
        """
        return self.rect.colliderect(other.rect)
        
        

class Player(Entity):
    """Player class inherited from Entity


    Attributes:
        image: An image that imports a picture and describes the location and size of the entity
        rect: A pygame.Rect that describes the location and size of the entity
    """
    def __init__(self):
        """Initialize a Player from parent class

        """
        super().__init__(0, 0, 50, 50)
        self.image = pygame.image.load("piper.png")
        self.image = pygame.transform.scale(self.image,(50, 50))
        
    def render(self, screen):
        """Draws the image on the screen
        
            Args:
                screen: surface to draw image on
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        
        
class Clam(Entity):
    """Clam class inherited from Entity


    Attributes:
        image: An image that imports a picture and describes the location and size of the entity
        rect: A pygame.Rect that describes the location and size of the entity
    """
    def __init__(self):
        """Initialize a Clam from parent class

        """
        super().__init__(random.randint(SCREEN_WIDTH/2 ,SCREEN_WIDTH-30), random.randint(0,SCREEN_WIDTH-30), 30, 30)
        self.image = pygame.image.load("clam.png")
        self.image = pygame.transform.scale(self.image,(30, 30))
        self.visible = True


    def render(self, screen):
        """Draws the image on the screen
        
            Args:
                screen: surface to draw image on
        """
        if self.visible:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        
        
class Wave(Entity):
    """Clam class inherited from Entity


    Attributes:
        rect: A pygame.Rect that describes the location and size of the entity
    """
    def __init__(self):
        """Initialize a Wave from parent class

        """
        super().__init__(0.75*SCREEN_WIDTH, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        
    def render(self, screen):
        """Draws the rect on the screen
        
            Args:
                screen: surface to draw image on
        """
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
        



def play_game(max_time):
    """Main game function for Piper's adventure

    Args:
        max_time: Number of seconds to play for
    """
    
    # Initialize the pygame engine
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Arial',14)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Piper's adventures")

    # Initialize Player, Wave and Clams
    piper = Player()
    all_clams = []
    for i in range(NUM_CLAMS):
        all_clams.append(Clam())
    wave = Wave()
    

    time  = 0
    score = 0

    # Main game loop
    while time < max_time:

        # Obtain any user inputs
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
          break

        # Screen origin (0, 0) is the upper-left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                piper.shift_x(STEP)
            elif event.key == pygame.K_LEFT:
                piper.shift_x(-STEP)
            elif event.key == pygame.K_UP:
                piper.shift_y(-STEP)
            elif event.key == pygame.K_DOWN:
                piper.shift_y(STEP)
        
        # Determine if Piper gathered more clams
        for clam in all_clams:
            if piper.collide(clam) & clam.visible:
                clam.visible = False
                score += 1

       
        # Update the position of the wave

        #wave.rect.x = 0.75*SCREEN_WIDTH-0.25*SCREEN_WIDTH*math.sin(time)
        wave.rect.x = 0.55*SCREEN_WIDTH-(0.45*SCREEN_WIDTH)*math.sin(time)
       
        # When the wave has reached its peak create new clams
    
        if wave.rect.x < .51*SCREEN_WIDTH:
            for i in range(NUM_CLAMS):
                all_clams[i] = Clam()

        # If the piper touched the wave the game is over...
        if piper.collide(wave):
            time = max_time

        # Draw all of the game elements
        screen.fill([255,255,255])
        piper.render(screen)
        for clam in all_clams:
            clam.render(screen)
        wave.render(screen)
       
       
        # Render the current time and score
        text = font.render('Time = ' + str(round(max_time-time, 1)), True, (0, 0, 0))
        screen.blit(text, (10, 0.95*SCREEN_HEIGHT))
    
        text = font.render('Score = ' + str(score), True, (0, 0, 0))
        screen.blit(text, (10, 0.90*SCREEN_HEIGHT))

        # Render next frame
        pygame.display.update()
        clock.tick(FPS)

        # Update game time by advancing time for each frame
        time += 1.0/FPS

    print('Game over!')
    print('Score =', score)

    pygame.display.quit()
    pygame.quit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        play_game(30)
    else:  
        play_game(int(sys.argv[1]))
    