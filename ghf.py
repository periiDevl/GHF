# import the pygame module
import pygame

# Define the background colour
# using RGB color coding.
background_colour = (50, 50, 50)

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((500, 500))

# Set the caption of the screen
pygame.display.set_caption('cock')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()
clicked = False
# Variable to keep our game loop running
running = True
mp = (0, 0)
# Initialing Color
color = (0,255,0)
def button(x, y, width, height, chekerboard):

    

    
    if (mp[0] < x + width and mp[0] > x - width and mp[1] < y + height and mp[1] > y - height):
        print("hi")
        color = (255, 0, 0)
        chekerColorT = (80, 80, 80)
        chekerColor = (200, 200, 200)
    else:
        color = (0, 255, 0)
        chekerColorT = (200, 200, 200)
        chekerColor = (80, 80, 80)
    if (not chekerboard):
        pygame.draw.rect(screen, color, pygame.Rect(x - width, y - height, width, height))
        pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
        pygame.draw.rect(screen, color, pygame.Rect(x, y - height, width, height))
        pygame.draw.rect(screen, color, pygame.Rect(x - width, y, width, height))
        pygame.display.flip()
    if (chekerboard):
        pygame.draw.rect(screen, chekerColor, pygame.Rect(x - width, y - height, width, height), 5)
        pygame.draw.rect(screen, chekerColor, pygame.Rect(x, y, width, height), 5)
        pygame.draw.rect(screen, chekerColorT, pygame.Rect(x, y - height, width, height), 5)
        pygame.draw.rect(screen, chekerColorT, pygame.Rect(x - width, y, width, height), 5)
        pygame.display.flip()
# game loop
while running:
    mp = pygame.mouse.get_pos()
    #print(mp[0])
    button(144, 202, 20, 80, False)
    pos = pygame.mouse.get_pos()
# for loop through the event queue
    for event in pygame.event.get():
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")
        # Check for QUIT event  
        if event.type == pygame.QUIT:
            running = False
