"""
 Show how to use a sprite backed by a graphic.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Initialize object properties for animation:
# Locations:
rect_x = 50
rect_y = 50

# Sizes:
rect_width = 50
rect_height = 50

# Velocities:
rect_x_vel = 2
rect_y_vel = 1

# Colors:
rect_color = BLUE

# Thicknesses:
rect_thickness = 0 # 0 => filled

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    # Update position from velocities:
    rect_x += rect_x_vel
    rect_y += rect_y_vel

    # Reverse velocity (bounce) if collision with wall:
    if rect_x + rect_width >= WIDTH or rect_x < 0:
        rect_x_vel *= -1
    if rect_y + rect_height >= HEIGHT or rect_y < 0:
        rect_y_vel *= -1
 
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    pygame.draw.rect(screen, rect_color, [rect_x, rect_y, rect_width, rect_height])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
