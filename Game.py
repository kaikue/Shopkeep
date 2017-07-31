import pygame
from pygame.locals import DOUBLEBUF
import sys

#Global constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SEC = 60
#Player dimensions
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
#Player movement speed
SPEED = 5

#Colors
GRAY = (128, 128, 128)
MAGENTA = (255, 0, 255)

def start():
    #Initialize pygame
    pygame.init()
    
    #Set the window caption
    pygame.display.set_caption("Simple Game")
    
    #Use double buffering for better performance
    flags = DOUBLEBUF
    #Create the screen
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
    
    #Create the clock
    global clock
    clock = pygame.time.Clock()
    
    #Start the player at [100, 100]
    global player_pos
    player_pos = [100, 100]
    
    #Start the game loop
    run()

def run():
    while True:
        #Wait one frame
        clock.tick_busy_loop(FRAMES_PER_SEC)
        
        #Process inputs and game logic
        update()
        
        #Draw to the screen
        render()

def update():
    #Put game logic in this function.
    
    #Get the list of currently pressed keys
    pressed = pygame.key.get_pressed()
    
    #If the user pressed ESC: quit
    if pressed[pygame.K_ESCAPE]:
        sys.exit(0)
    
    #If the user has pressed an arrow key, move the player
    #Horizontal movement
    if pressed[pygame.K_LEFT]:
        player_pos[0] -= SPEED
    if pressed[pygame.K_RIGHT]:
        player_pos[0] += SPEED
    #Vertical movement
    if pressed[pygame.K_UP]:
        player_pos[1] -= SPEED
    if pressed[pygame.K_DOWN]:
        player_pos[1] += SPEED
    
    #If the user clicked close: quit
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            sys.exit(0)

def render():
    #Only use this function for graphical rendering.
    #Other logic should go in update().
    
    #Draw a gray background
    screen.fill(GRAY)
    
    #Draw the player as a pink rectangle
    player_rect = pygame.rect.Rect(player_pos, (PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, MAGENTA, player_rect)
    
    #Update the display
    pygame.display.update()