"""
 Show how to use a sprite backed by a graphic.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
WIDTH = 900
HEIGHT = 675
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

# Load images:
background_image = pygame.image.load("sky.jpg").convert()
fly_image = pygame.image.load("fly.png").convert()

# Make white background of fly image transparent:
fly_image.set_colorkey(WHITE)

# Load sounds:
pygame.mixer.init(frequency = 44100)
hihat_sound = pygame.mixer.Sound("808_hi_hat.ogg")
 
pygame.display.set_caption("Animating Snow")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Make a list of random snowflakes:
flakes = 500
max_size = 5
snow_x = [random.randrange(-200, WIDTH + 200) for x in range(flakes)]
snow_y = [random.randrange(-40, HEIGHT) for y in range(flakes)]
#snow_vel = [0.0 for y in range(flakes)]
snow_size = [random.choice([1,1,1,1,2,2,2,3,3,4]) for x in range(flakes)]
snow_vel = [(flake - 1.) / (max_size - 1) for flake in snow_size]
g = 2.8 / 60
wind = 0.0
ground = 10
brightness = 255.0
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hihat_sound.play()
 
    # --- Game logic should go here
    mouse_pos = pygame.mouse.get_pos()
    brightness -= 0.05
    if brightness < 0:
        brightness = 0
    wind += random.gauss(0,0.1)
    if wind > 4:
        wind = 4
    elif wind < -4:
        wind = -4
    for i in range(len(snow_x)):
        snow_y[i] += snow_vel[i]
        snow_x[i] += random.gauss(0, snow_size[i] / (max_size - 1.)) + wind / (max_size - snow_size[i])
        snow_vel[i] += g / (max_size - snow_size[i])
        if snow_y[i] > HEIGHT - ground:
            ground += snow_size[i] / float(WIDTH)
            snow_y[i] = -20
            snow_x[i] = random.randrange(-200, WIDTH + 200) - wind * 100
            snow_size[i] = random.choice([1,1,1,1,2,2,2,3,3,4])
            snow_vel[i] = (snow_size[i] - 1.) / (max_size - 1)
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill((0, 0, brightness))

    # Draw sky background:
    screen.blit(background_image, [0,0])

    # Draw snowflakes:
    for i in range(len(snow_x)):
        pygame.draw.ellipse(screen, WHITE, [snow_x[i], snow_y[i],
                                            snow_size[i], snow_size[i]])

    # Draw Ground:
    pygame.draw.rect(screen, WHITE, [0, HEIGHT - ground, WIDTH, ground])

    # Draw Fly:
    screen.blit(fly_image, mouse_pos)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
