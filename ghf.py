import pygame

pygame.font.init()
 
pygame.font.get_init()


 
 

 


background_colour = (50, 50, 50)

screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption('GHF-window')

screen.fill(background_colour)

pygame.display.flip()
clicked = False
running = True
trigger = True
mp = (0, 0)
def button(text = "hello",x=600, y=30, width=60, height=30, font_size=35,curve = 8, outline = 1 ,color = (0, 200, 0), hover = (0, 230, 0), cli = (0, 130, 0)):
    global trigger
    font1 = pygame.font.Font('Smokind-lg2Kd.otf', font_size)
    text1 = font1.render(text, True, (255, 255, 255))
    text2 = font1.render(text, True, (0, 0, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (x, y)

    textRect2 = text1.get_rect()
 
    
    textRect2.center = (x + outline, y + outline)
    
        

    
    if (mp[0] < x + width and mp[0] > x - width and mp[1] < y + height and mp[1] > y - height):
        color = hover
        if clicked:
            color = cli
        

    pygame.draw.rect(screen, color, pygame.Rect(x-width, y-height, width * 2, height* 2), 0, curve)
    pygame.draw.rect(screen, (0), pygame.Rect(x-width, y-height, width * 2, height* 2), outline, curve)
        
    screen.blit(text2, textRect2)
    screen.blit(text1, textRect1)
    pygame.display.flip()
    #logic
    if (mp[0] < x + width and mp[0] > x - width and mp[1] < y + height and mp[1] > y - height):
        if clicked:
            
            trigger = False
            return False
        if not clicked and trigger == False:
            if trigger:
                return

                # do something

            trigger = True
            return True

            
        
        #if not clicked and t == True:


    
    
# game loop
while running:
    mp = pygame.mouse.get_pos()
    if (button()):
        print("test")
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        if event.type == pygame.QUIT:
            running = False
