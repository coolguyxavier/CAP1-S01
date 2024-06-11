# - CAP1-S01 Proper Projectiles and Player Code - #
# - Xzavier Moosomin - #
# - Started on 05/27/2024 - #

# - Developer Comments - #
# here in this module, i'm gonna be making the projectiles move
# hopefully i could create some sprites for them.
# the plan for the dictionary is that for each pellet/beam spawn, it subtracts one
# from the key's value
# like if 10 pellets spawn, the Pellet Key has an updated value of 90.

# - Imports - #

import pygame
from math import cos, sin, atan2
from random import randint

# - Lists / Dictionaries - #

projectile_dict = {'Pellet': 100, 'Beam': 5}

# - Pygame Initialization - #

pygame.init()

# - Constants - #

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font(None, 35) # fontstyle, fontsize

# - Variables - 
p_health = 100

game = True

num_of_pellets = 3

# - Game Setting - #

screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Object and Player 02 Testing')

clock = pygame.time.Clock()

# - Classes - #

class Player:
    def __init__(self):
        self.img = pygame.image.load('SPRITES/PLAYER/player_02.png').convert()
        self.rect = self.img.get_rect() # sets a collision box to the img
        self.rect.x = 375 # this and next line underneath determine
        self.rect.y = 375 # where the player spawns
        self.player_xpos, self.player_ypos = self.rect.x, self.rect.y
            
    def display_info(self):
        # health display text
        healthtext_01 = font.render("Player Health", 1, white)
        screen.blit(healthtext_01, (606, 50))
        
        healthtext_02 = font.render(f"{p_health}%", 1, white)
        screen.blit(healthtext_02, (650, 75))
        
    def move(self, x, y):
        self.rect.x += x # im pretty sure this code 
        self.rect.y += y # makes the player able to move
        
        # this block of code makes sure that it doesn't go outside the box
        # for now, there is absolutely no chance for the player to roam outside
        # possibly later for the player to roam the screen...?
        if self.rect.left < 155: # left side of box
            self.rect.left = 155
            
        elif self.rect.right > 645: # right side of box
            self.rect.right = 645
            
        if self.rect.top < 155: # ceiling of box
            self.rect.top = 155
            
        elif self.rect.bottom > 645: # floor of box
            self.rect.bottom = 645
            
            
class Projectile:
    def __init__(self, width, height, speed):
        self.img = pygame.Surface((width, height))
        self.img.fill(white)
        
        self.speed = speed
        
        self.rect = self.img.get_rect() # creates placeholder rect on top of the image
        self.rect.x, self.rect.y = (randint(0, 800)), (randint(0, 800)) #random spawn location^
        self.angle = atan2(player.rect.y - self.rect.y, player.rect.x - self.rect.x)
        
    def move(self):
        self.rect.x += self.speed * cos(self.angle) # but i know cos
        self.rect.y += self.speed * sin(self.angle) # and sin though, so that's cool

        
class SmallRect(Projectile):
    def __init__(self, width, height, color, speed):
        super().__init__(width, height, speed)
        self.color = color
        self.img.fill(self.color)
        
class ThickLong(Projectile):
    def __init__(self, width, height, color, speed):
        super().__init__(width, height, speed)
        self.color = color
        self.img.fill(color)
        self.img = pygame.image.load('SPRITES/PROJECTILES/comp_beam.png')
        self.rect = self.img.get_rect() # creates rect on the image for collision
        
        self.rect.x, self.rect.y = (randint(0, 800)), (randint(0, 800)) #random spawn location^
         
# - Create Object(s)

player = Player()
pellet = SmallRect(30, 30, white, 10) # we can comment out
beam = ThickLong(50, 800, blue, 6)

# - Main Code - #

while game == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move(-5, 0)
    if keys[pygame.K_d]:
        player.move(5, 0)
    if keys[pygame.K_w]:
        player.move(0, -5)
    if keys[pygame.K_s]:
        player.move(0, 5)
        
    if p_health <= 0:
        deathtext = font.render("You died!", 1, white)
        screen.blit(deathtext, (350, 400))
        pygame.time.wait(4000)
        game = False
        
    # mini logic code 
    if pygame.Rect.colliderect(player.rect, pellet.rect):
        p_health -= 1
        
    if pygame.Rect.colliderect(player.rect, beam.rect):
        p_health -= 1
        
    # if there is less than 5 pellets on the screen and there are some in the dict, spawn a new pellet
    pellet.move()
    if num_of_pellets < 5 and projectile_dict['Pellet'] > 0:
        pellet = SmallRect(30, 30, white, 10)

        projectile_dict['Pellet'] - 1
        
        # if pellet is off the top/bottom of the screen, create new
        if pellet.rect.x < 0 or pellet.rect.x > 800:
            num_of_pellets -= 1
            pellet.rect.x, pellet.rect.y = randint(0, 800), randint(0, 800)
            pellet = SmallRect(30, 30, white, 10)
            num_of_pellets += 1
            
        if pellet.rect.y < 0 or pellet.rect.y > 800:
            num_of_pellets -= 1
            pellet.rect.x, pellet.rect.y = randint(0, 800), randint(0, 800)
            pellet = SmallRect(30, 30, white, 10)
            num_of_pellets += 1
        
    #beam.beam_move()   # i'll bring all this back once I'm able to spawn more pellets at a time
    #if beam.rect.x < - 1005 or beam.rect.x > 1000:
    #    beam.rect.x, beam.rect.y = randint(1000, 1250), randint(1000, 1250)
    #    beam = ThickLong(50, 800, blue, 6)
        
    #if beam.rect.y < -1010 or beam.rect.y > 1000:
     #   beam.rect.x, beam.rect.y = randint(1000, 1250), randint(1000, 1250)
      #  beam = ThickLong(50, 800, blue, 6)
        
    # drawing code
    screen.fill(black)
    screen.blit(player.img, player.rect)
    screen.blit(pellet.img, pellet.rect)    
    screen.blit(beam.img, beam.rect) 
    
    player.display_info()
    
    #print(player.rect.x, player.rect.y) # comment out when not needed
            
    pygame.display.flip()
    
    clock.tick(60)

