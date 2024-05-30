# - CAP1-S01 - Simple Projectile Code - #
# - Xzavier Moosomin - #
# - Started on 05/27/2024 - #

# - Developer Notes - #
# i couldnt figure out how to do it with all the other stuff going on
# so i just made a new file
# might copy and paste it into the bigger file, or i might import it (external file real)
# importing makes me seem smarter though, so i'll do that

# - Imports - #

import pygame
import time
from random import randint

# - Pygame Initialization - #

pygame.init()

# - Constants - #
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 192, 203)
grey = (126, 126, 126)
black = (0, 0, 0)

# - Game Settings - #
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Projectile Testing')

clock = pygame.time.Clock()

# - Dictionaries/Lists - #

projectile_count = {'Small Rectangle Projectile': 10, 'Long Skinny Projectile': 5, 'Short Thick Projectile': 5}

# - Classes - #

class Projectile:
    def __init__(self, width, height):
        self.width = width # dimensions
        self.height = height
        
        self.img = pygame.Surface([width, height])
        
        self.rect = self.img.get_rect()
        self.rect.x = 300#randint(0, 800) # spawn location
        self.rect.y = 300#randint(0, 800)
        
    def move(self):
        self.rect.x += self.x
        self.rect.y += self.y
        
class SmallRect(Projectile):
    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color
        self.img.fill(self.color)
        
class SkinnyLong(Projectile):
    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color
        self.img.fill(self.color)
        
class ShortThick(Projectile):
    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color
        self.img.fill(self.color)
        
class VariableSize(Projectile):
    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color
        self.img.fill(self.color)
        
class fella(Projectile): # this is just a joke class, got bored and made this little fella
    def __init__(self, width, height):
        super().__init__(width, height)
        self.img = pygame.image.load('SPRITES/CHARACTERS/sans.png').convert()
        self.rect = self.img.get_rect()
        self.rect.x = randint(0, 700)
        self.rect.y = randint(0, 700)
        
# - Functions - #

def pick_projectile(dictionary):
    pass
        
# - Create Object(s)

bullet_01 = SmallRect(30, 60, red) # we can comment out
bullet_02 = SkinnyLong(20, 110, blue) # these guys
bullet_03 = ShortThick(50, 50, green) # when they currently 
bullet_04 = VariableSize(randint(10, 100), randint(10, 100), pink) # serve 0 use
sans = fella(10, 10)

# - Main Code - #

while True:
    #screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    #screen.blit(bullet_01.img, bullet_01.rect) # puts the fella on the screen
    #screen.blit(bullet_02.img, bullet_02.rect) # WE CAN ALSO
    #screen.blit(bullet_03.img, bullet_03.rect) # COMMENT OUT 
    #screen.blit(bullet_04.img, bullet_04.rect) # THESE FOUR LINES
    #screen.blit(sans.img, sans.rect)
    # bullet_01.move() # makes the fella move
        
    pygame.display.flip() # allows you to see the fella move
    