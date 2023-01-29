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

class Player:
    def __init__(self, x, y, width, height):
        self.x=x             #character's x position
        self.y=y             #character's y position
        self.width=width     #character's width
        self.height=height   #character's height
        self.vel=5           #how fast the character moves
        self.is_jump=False   #is the character jumping or not
        self.jump_count=10   
        self.left=False      #is the character is moving or not and in which direction. So display pic can be changed acc.
        self.right=False     # "
        self.walk_count=0    # how many steps has the character already moved
    
    def draw(self, win):
        #animates the character:
        if self.walk_count+1>=27:
            self.walk_count=0
        
        if self.left:
            win.blit(walk_left[self.walk_count//3],(self.x,self.y))
            self.walk_count+=1
        elif self.right:
            win.blit(walk_right[self.walk_count//3],(self.x,self.y))
            self.walk_count+=1
        else:
            win.blit(char, (self.x,self.y))

def redraw_game_window():
    win.blit(bg,(0,0)) #sets a background image. args: 1. pic name, 2. tuple with position coordinates
    player.draw(win)
    pygame.display.update()

#main loop: we use main loop to check for events etc.
player=Player(x=300, y=410, width=64, height=64)
run = True
while run:
    #pygame.time.delay(100)              #100 ms=0.1 sec delay, so nothing happens too quickly
    clock.tick(27)                       # sets FPS(frames per sec) to 27

    for event in pygame.event.get():    #pygame.event.get() gets a list of all the events that are happening                             
        if event.type==pygame.QUIT:     #such as mouse position moved, key presses, mouse clicks, etc.
            run=False
    
    keys = pygame.key.get_pressed()                             #listens for key presses
    if keys[pygame.K_LEFT] and player.x>player.vel:                    #left key press decreases x position by vel
        player.x-=player.vel
        player.left=True
        player.right=False
    elif keys[pygame.K_RIGHT] and player.x<screen_width-player.width-player.vel:       
    #right key press increases x position by vel and
        player.x+=player.vel  
        player.right=True
        player.left=False    
    else:
        player.left=False
        player.right=False
        player.walk_count=0                                            #prevents rectangle from moving out of screen     
    if not player.is_jump:
        #As per game design, getting rid of the character's ability to move up and down, except to jump:

        # if keys[pygame.K_UP] and y>vel:                         #up key press decreases y position by vel
        #     y-=vel
        # if keys[pygame.K_DOWN] and y<screen_height-height-vel:  #down key press increases y position by vel and
        #     y+=vel  
        if keys[pygame.K_SPACE]:
            player.is_jump = True
            player.left=False
            player.right=False
            player.walk_count=0
    else:
        if player.jump_count>=-10:
            neg = 1
            if player.jump_count < 0:
                neg = -1
            player.y -= (player.jump_count ** 2) * 0.5 * neg
            player.jump_count -= 1
        else:
            player.is_jump = False
            player.jump_count = 10     

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

