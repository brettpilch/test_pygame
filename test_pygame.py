import pygame
import random
import math
pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Draw line:
    # pygame.draw.line(Surface, color, start point, end point, thickness)
    pygame.draw.line(screen, GREEN, [100,100], [600,400], 5)

    # Draw rectangle:
    # pygame.draw.rect(Surface, color, [topleft x, topleft y, width, height], thickness)
    pygame.draw.rect(screen, RED, [100, 100, 500, 300], 3)

    # Draw ellipse:
    # pygame.draw.ellipse(Surface, color, [topleft x, topleft y, width, height], thickness)
    pygame.draw.ellipse(screen, BLUE, [100, 100, 500, 300], 10)

    # Draw an arc as part of an ellipse. Use radians to determine what
    # angle to draw.
    pygame.draw.arc(screen, GREEN, [100,100,250,200],  math.pi/2,     math.pi, 2)
    pygame.draw.arc(screen, BLACK, [100,100,250,200],     0,   math.pi/2, 2)
    pygame.draw.arc(screen, RED,   [100,100,250,200],3*math.pi/2,   2*math.pi, 2)
    pygame.draw.arc(screen, BLUE,  [100,100,250,200],    math.pi, 3*math.pi/2, 2)

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100,100], [0,200], [200,200]], 5)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("My text",True,BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
pygame.quit()
