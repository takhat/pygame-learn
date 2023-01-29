import pygame
char = pygame.image.load('assets/standing.png')
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

class Player:
    def __init__(self, x, y, width, height):
        self.x=x             #character's x position
        self.y=y             #character's y position
        self.width=width     #character's width
        self.height=height   #character's height
        self.vel=5           #how fast the character moves
        self.is_jump=False   #is the character jumping or not 
        self.left=False      #is the character is moving or not and in which direction. So display pic can be changed acc.
        self.right=False     # "
        self.walk_count=0    # how many steps has the character already moved
        self.jump_count=10  
        self.standing=True

    def draw(self, win):
        global walk_left
        global walk_right

        #animates the character:
        if self.walk_count+1>=27:
            self.walk_count=0
        
        if not self.standing:               #if player is moving
            if self.left:
                win.blit(walk_left[self.walk_count//3],(self.x,self.y))
                self.walk_count+=1
            elif self.right:
                win.blit(walk_right[self.walk_count//3],(self.x,self.y))
                self.walk_count+=1
        else:                               #if player is still, he needs to look either left or right..
            if self.right:                  #..depending on its last direction.
                win.blit(walk_right[0], (self.x,self.y))
            else:
                win.blit(walk_left[0], (self.x, self.y))