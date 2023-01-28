import pygame  
pygame.init()                                                 #initializes pygame

screen_width, screen_height = 500, 500

win = pygame.display.set_mode((screen_width, screen_height))  #creates a display window or screen 

pygame.display.set_caption("First Game")                      #sets the caption of the window 

x=50            #character's x position
y=50            #character's y position
width=40        #character's width
height=60       #character's height
vel=5           #how fast the character moves
is_jump=False   #is the character jumping or not
jump_count=10   #
#main loop: we use main loop to check for events etc.
run = True
while run:
    pygame.time.delay(100)              #100 ms=0.1 sec delay, so nothing happens too quickly

    for event in pygame.event.get():    #pygame.event.get() gets a list of all the events that are happening                             
        if event.type==pygame.QUIT:     #such as mouse position moved, key presses, mouse clicks, etc.
            run=False
    
    keys = pygame.key.get_pressed()                             #listens for key presses
    if keys[pygame.K_LEFT] and x>vel:                           #left key press decreases x position by vel
        x-=vel
    if keys[pygame.K_RIGHT] and x<screen_width-width-vel:       #right key press increases x position by vel and
        x+=vel                                                  #prevents rectangle from moving out of screen     
    if not is_jump:
        if keys[pygame.K_UP] and y>vel:                         #up key press decreases y position by vel
            y-=vel
        if keys[pygame.K_DOWN] and y<screen_height-height-vel:  #down key press increases y position by vel and
            y+=vel  
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count>=-10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10                                           
            
    #fills the screen by black color to match the background so that 
    #as new rectangle is drawn, old ones are hidden
    win.fill((0,0,0))

    #makes a rectangle that represents our character:
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))  #arguments: 1. surface where to draw, 2. rgb, 3. rect i.e. x, y, width, height
    
    #makes the above rectangle show up on screen:
    pygame.display.update()
      
pygame.quit()

