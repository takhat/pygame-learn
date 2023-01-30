import pygame

class Enemy:
    walk_right=[pygame.image.load('assets/R1E.png'),
        pygame.image.load('assets/R2E.png'),
        pygame.image.load('assets/R3E.png'),
        pygame.image.load('assets/R4E.png'),
        pygame.image.load('assets/R5E.png'),
        pygame.image.load('assets/R6E.png'),
        pygame.image.load('assets/R7E.png'),
        pygame.image.load('assets/R8E.png'),
        pygame.image.load('assets/R9E.png'),
        pygame.image.load('assets/R10E.png'),
        pygame.image.load('assets/R11E.png')]

    walk_left=[pygame.image.load('assets/L1E.png'),
        pygame.image.load('assets/L2E.png'),
        pygame.image.load('assets/L3E.png'),
        pygame.image.load('assets/L4E.png'),
        pygame.image.load('assets/L5E.png'),
        pygame.image.load('assets/L6E.png'),
        pygame.image.load('assets/L7E.png'),
        pygame.image.load('assets/L8E.png'),
        pygame.image.load('assets/L9E.png'),
        pygame.image.load('assets/L10E.png'),
        pygame.image.load('assets/L11E.png')]   

    def __init__(self, x, y, width, height, end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.walk_count=0
        self.vel=3
        self.path=[self.x, self.end]
        self.hitbox=(self.x+17, self.y+2, 31, 57) #we can use rect for hitboxes for simplicity, hitboxes help with collisions

    def draw(self, win):
        self.move()         #every time we draw the character, we are going to move the character first
        if self.walk_count+1 >= 33:
            self.walk_count=0
        
        if self.vel > 0:
            win.blit(self.walk_right[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        
        else:
            win.blit(self.walk_left[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        self.hitbox=(self.x+17, self.y+2, 31, 57)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel>0:                           #if +ve vel i.e. character is moving toward the right
            if self.x + self.vel < self.path[1]: #if x coord + vel < end 
                self.x += self.vel               #allow character to continue to move to the right
            else:
                self.vel = self.vel *-1          #change vel to -ve  so character doesn't move past the end pos
                self.walk_count=0
        else:
            if self.x -self.vel > self.path[0]:  #if x coord - vel < left starting pos(x) 
                self.x += self.vel               #allow character to continue to move left  
            else:
                self.vel = self.vel *-1          #change vel to +ve  so character doesn't move past the left start pos
                self.walk_count=0

    def hit(self):
        print("hit")

