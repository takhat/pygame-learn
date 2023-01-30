import pygame  
from player import Player
from projectile import Projectile
from enemy import Enemy

pygame.init()                                                 #initializes pygame

screen_width, screen_height = 500, 480

win = pygame.display.set_mode((screen_width, screen_height))  #creates a display window or screen 

pygame.display.set_caption("First Game")                      #sets the caption of the window 

clock = pygame.time.Clock()

bg = pygame.image.load('assets/bg.jpg')

# char = pygame.image.load('assets/standing.png')
score = 0


def redraw_game_window():
    win.blit(bg,(0,0)) #sets a background image. args: 1. pic name, 2. tuple with position coordinates
    text=font.render("Score: " + str(score), 1, (0, 0, 0)) #forming a string to render to screen
    win.blit(text, (390,10))                               #rendering the string
    player.draw(win)                 
    for bullet in bullets:
        bullet.draw(win)
    enemy.draw(win)
    pygame.display.update()

#main loop: we use main loop to check for events etc.

font=pygame.font.SysFont('comicsans', 20, True)

player=Player(x=300, y=410, width=64, height=64)
enemy=Enemy(x=100, y=410, width=64, height=64, end=450)
shoot_loop=0
bullets=[]
run = True

while run:
    #pygame.time.delay(100)              #100 ms=0.1 sec delay, so nothing happens too quickly
    clock.tick(27)                       #sets FPS(frames per sec) to 27
    
    if shoot_loop>0:                     #when we shoot 1st time, shoot_loop =1 from 0
        shoot_loop+=1                    #when we shoot 2nd time, shoot_loop = 2 from 1, and no bullet

    if shoot_loop>3:                     #when we shoot 3rd time, shoot_loop =3 from 2, and no bullet
        shoot_loop=0                     #when we shoot 4th time, shoot_loop = 0 from 3, and there is bullet

    for event in pygame.event.get():     #pygame.event.get() gets a list of all the events that are happening..                             
        if event.type==pygame.QUIT:      #..such as mouse position moved, key presses, mouse clicks, etc.
            run=False
    
    for bullet in bullets:
        #the bullet should be inside the hitbox for collision 

        #if the bullet's y coord is within the top and the bottom of our enemy's rect's y coordinate
        if bullet.y-bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
             #if the bullet's x coord is within the enemy's rect's x coordinate
            if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x-bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()
                score+=1
                bullets.pop(bullets.index(bullet))

        if bullet.x < screen_width and bullet.x > 0:    #if bullet is within the screen width
            bullet.x += bullet.vel
        else:                                           #if its outside screen width, delete the bullet
            bullets.pop(bullets.index(bullet)) 
    
    keys = pygame.key.get_pressed()                             #listens for key presses

    if keys[pygame.K_SPACE] and shoot_loop==0:                  #space key press allows shooting bullets
        if player.left:
            facing=-1
        else:
            facing=1                                
        if len(bullets)<5:
            bullets.append(Projectile(round(player.x+player.width//2),round(player.y + player.height//2), 6, (0, 0, 0),facing))             
        
        shoot_loop=1                       #when we first shoot a bullet, shoot_loop is set to 1
    if keys[pygame.K_LEFT] and player.x>player.vel:             #left key press decreases x position by vel
        player.x-=player.vel
        player.left=True
        player.right=False
        player.standing=False
    elif keys[pygame.K_RIGHT] and player.x<screen_width-player.width-player.vel:       
        player.x+=player.vel                                     #right key press increases x position by vel
        player.right=True
        player.left=False    
        player.standing=False
    else:
        player.standing=True
        player.walk_count=0                                            
    if not player.is_jump:
        #As per game design, getting rid of the character's ability to move up and down, except to jump:

        # if keys[pygame.K_UP] and y>vel:                         #up key press decreases y position by vel
        #     y-=vel
        # if keys[pygame.K_DOWN] and y<screen_height-height-vel:  #down key press increases y position by vel and
        #     y+=vel  
        if keys[pygame.K_UP]:                                     #Up key press makes the player jump
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

