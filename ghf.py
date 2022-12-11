import pygame

pygame.font.init()
 
pygame.font.get_init()


 
 

 


background_colour = (0, 0, 0)

screen = pygame.display.set_mode((790, 325), pygame.NOFRAME)

pygame.display.set_caption('GHS-window')

screen.fill(background_colour)

pygame.display.flip()
clicked = False
running = True
trigger = True
mp = (0, 0)



def button(text = "hello",x=600, y=30, width=60, height=30, font_size=45,curve = 5, 
    outline = 1 ,color = (0, 200, 0), hover = (0, 230, 0), cli = (0, 130, 0), 
    state_amount = 20, img = "caliber.png", imgCLI = "3.jpg", imgeHover = "3.jpg",
    image = True, draw = True, scene = 0, drawScene = 0):
    if scene != drawScene:
        draw = False
    if draw == False:
        color = background_colour
        hover = background_colour
        imgCLI = background_colour
        image = False
        text = " "
        outline = 0
        curve = 0

    if image:
        picture = pygame.image.load(img).convert_alpha()
        picture = pygame.transform.scale(picture, (width * 2, height * 2))

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
        if image:
            picture = pygame.image.load(imgeHover).convert_alpha()
            picture = pygame.transform.scale(picture, (width * 2, height * 2))
        if clicked:
            color = cli
            if image:
                picture = pygame.image.load(imgCLI).convert_alpha()
                picture = pygame.transform.scale(picture, (width * 2, height * 2))


    pygame.draw.rect(screen, color, pygame.Rect(x-width, y-height, width * 2, height* 2), 0, curve)
    pygame.draw.rect(screen, (0), pygame.Rect(x-width, y-height, width * 2, height* 2), outline, curve)
    if image:
        screen.blit(picture, (x-width, y-height))
        #screen.blit(picture, (x-width, y-height/2))

    screen.blit(text2, textRect2)
    screen.blit(text1, textRect1)
    pygame.display.flip()


    
        
    #logic
    if (mp[0] < x + width and mp[0] > x - width and mp[1] < y + height and mp[1] > y - height and draw == True):
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


scene = 0
# game loop
while running:
    mp = pygame.mouse.get_pos()
    if (button(text = "GAMES",x = 250 / 2 + 10, height = 135, y = 150, width = 125, color = (0, 0, 0), hover = (0, 0, 0), cli = (0, 0, 0),
            img = "games.png", imgeHover = "gameshover.png", imgCLI ="gamesclick.png", scene = scene, drawScene = 0
            )):
            print("test")

    if (button(text = "CALIBER" ,x = 750 / 2 + 20, height = 135, y = 150, width = 125,
            img = "caliberLogo.jpg", imgeHover = "caliberLogoHover.jpg", imgCLI = "caliberLogoClick.jpg",
            )):
            print("caliber")
            scene = 1
            

    if (button(text = "ECHO",x = 1250 / 2 + 30, height = 135, y = 150, width = 125,
            img = "echoengineicon.png", imgeHover = "echoengineiconhover.png", imgCLI = "echoengineiconclick.png",
            )):
            print("test")

    if (button(x = 1460 / 2 + 38, height = 13, y = 305, width = 13, image = False, curve = 100, text = "", color = (180, 0, 0)
        ,hover = (255, 0, 0), cli = (90, 0, 0))):
        running = False
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        if event.type == pygame.QUIT:
            running = False
