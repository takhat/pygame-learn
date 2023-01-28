import pygame  
pygame.init()                                                 #initializes pygame

screen_width, screen_height = 500, 480

win = pygame.display.set_mode((screen_width, screen_height))  #creates a display window or screen 

pygame.display.set_caption("First Game")                      #sets the caption of the window 

clock = pygame.time.Clock()

walk_right=[pygame.image.load('assets/R1.png'),
    pygame.image.load('assets/R2.png'),
    pygame.image.load('assets/R3.png'),
    pygame.image.load('assets/R4.png'),
    pygame.image.load('assets/R5.png'),
    pygame.image.load('assets/R6.png'),
    pygame.image.load('assets/R7.png'),
    pygame.image.load('assets/R8.png'),
    pygame.image.load('assets/R9.png')]

walk_left=[pygame.image.load('assets/L1.png'),
    pygame.image.load('assets/L2.png'),
    pygame.image.load('assets/L3.png'),
    pygame.image.load('assets/L4.png'),
    pygame.image.load('assets/L5.png'),
    pygame.image.load('assets/L6.png'),
    pygame.image.load('assets/L7.png'),
    pygame.image.load('assets/L8.png'),
    pygame.image.load('assets/L9.png')]   

bg = pygame.image.load('assets/bg.jpg')

char = pygame.image.load('assets/standing.png')


x=50            #character's x position
y=400           #character's y position
width=64        #character's width
height=64       #character's height
vel=5           #how fast the character moves
is_jump=False   #is the character jumping or not
jump_count=10   
left=False      #is the character is moving or not and in which direction. So display pic can be changed acc.
right=False     # "
walk_count=0    # how many steps has the character already moved

def redraw_game_window():
    global walk_count

    win.blit(bg,(0,0)) #sets a background image. args: 1. pic name, 2. tuple with position coordinates
   
    #animates the character:
    if walk_count+1>=27:
        walk_count=0
    
    if left:
        win.blit(walk_left[walk_count//3],(x,y))
        walk_count+=1
    elif right:
        win.blit(walk_right[walk_count//3],(x,y))
        walk_count+=1
    else:
        win.blit(char, (x,y))
    
    pygame.display.update()

#main loop: we use main loop to check for events etc.
run = True
while run:
    #pygame.time.delay(100)              #100 ms=0.1 sec delay, so nothing happens too quickly
    clock.tick(27)                       # sets FPS(frames per sec) to 27

    for event in pygame.event.get():    #pygame.event.get() gets a list of all the events that are happening                             
        if event.type==pygame.QUIT:     #such as mouse position moved, key presses, mouse clicks, etc.
            run=False
    
    keys = pygame.key.get_pressed()                             #listens for key presses
    if keys[pygame.K_LEFT] and x>vel:                           #left key press decreases x position by vel
        x-=vel
        left=True
        right=False
    elif keys[pygame.K_RIGHT] and x<screen_width-width-vel:       #right key press increases x position by vel and
        x+=vel  
        right=True
        left=False    
    else:
        left=False
        right=False
        walk_count=0                                            #prevents rectangle from moving out of screen     
    if not is_jump:
        #As per game design, getting rid of the character's ability to move up and down, except to jump:

        # if keys[pygame.K_UP] and y>vel:                         #up key press decreases y position by vel
        #     y-=vel
        # if keys[pygame.K_DOWN] and y<screen_height-height-vel:  #down key press increases y position by vel and
        #     y+=vel  
        if keys[pygame.K_SPACE]:
            is_jump = True
            left=False
            right=False
            walk_count=0
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

    redraw_game_window()                                      
    #replacing below code with redraw_game_window function:      
    # #fills the screen by black color to match the background so that 
    # #as new rectangle is drawn, old ones are hidden
    # win.fill((0,0,0))

    # #makes a rectangle that represents our character:
    # pygame.draw.rect(win, (255,0,0), (x, y, width, height))  #arguments: 1. surface where to draw, 2. rgb, 3. rect i.e. x, y, width, height
    
    # #makes the above rectangle show up on screen:
    # pygame.display.update()
      
pygame.quit()

