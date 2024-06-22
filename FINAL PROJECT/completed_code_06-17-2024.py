# - CAP1-S01 The Full Working Code - #
# - Xzavier Moosomin - #
# - File Created on: 06/17/2024 - #

# - Developer Comments - #
# i dont plan to perform any testing on this file, as i plan to keep it untouched
# and only updated when a new version is completed with any extra features.

# - Imports - #

import pygame
from math import cos, sin, atan2
from random import randint

# - Pygame Initialization - #

pygame.init()

# - Game Setting - #

screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Object and Player 02 Testing')

clock = pygame.time.Clock()

# - Constants - #

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font(None, 35) # fontstyle, fontsize
playarea = pygame.image.load('SPRITES/PLAY AREA/box_01.png').convert()

# - Variables - 
p_health = 100

game = True

num_of_pellets = 3

pellet_time = 0


# - Classes - #

class Player:
    def __init__(self):
        self.img = pygame.image.load('SPRITES/PLAYER/player_03.png').convert()
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
        
        self.rect.x, self.rect.y = (randint(1000, 1250)), (randint(1000, 1250)) #random spawn location^
    
    def point(self):
        self.angle = round(player.rect.x / player.rect.y)
        self.img = pygame.transform.rotate(self.img, self.angle)
        screen.blit(self.img, self.rect)


# - Create Object(s)

player = Player()
pellet1 = SmallRect(30, 30, white, 10) # cheap way of doing it
pellet2 = SmallRect(30, 30, white, 10) # but that would be
pellet3 = SmallRect(30, 30, white, 10) # too much work and i dont have a big enough time frame
beam = ThickLong(50, 800, blue, 6)

# - Main Code - #

while game == True:
    
    pellet_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False

    keys = pygame.key.get_pressed()
    
    # - W A S D KEY MOVEMENTS - #
    if keys[pygame.K_a]:
        player.move(-5, 0)
    if keys[pygame.K_d]:
        player.move(5, 0)
    if keys[pygame.K_w]:
        player.move(0, -5)
    if keys[pygame.K_s]:
        player.move(0, 5)
        
    # - ARROW KEY MOVEMENTS - #
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_UP]:
        player.move(0, -5)
    if keys[pygame.K_DOWN]:
        player.move(0, 5)
        
    if p_health <= 0:
        deathtext = font.render("You died!", 1, white)
        screen.blit(deathtext, (350, 400))
        pygame.time.wait(4000)
        game = False
        
    # mini logic code 
    if pygame.Rect.colliderect(player.rect, pellet1.rect):
        p_health -= 1
    if pygame.Rect.colliderect(player.rect, pellet2.rect):
        p_health -= 1
    if pygame.Rect.colliderect(player.rect, pellet3.rect):
        p_health -= 1
    #if pygame.Rect.colliderect(player.rect, beam.rect):
        #p_health -= 1
        
    pellet1.move()
    pellet2.move()
    pellet3.move()
    # if pellet is off the top/bottom of the screen, create new
    if pellet1.rect.x < 0 or pellet1.rect.x > 800:
        num_of_pellets -= 1
        pellet1.rect.x, pellet1.rect.y = randint(0, 800), randint(0, 800)
        pellet1 = SmallRect(30, 30, white, 10)
        num_of_pellets += 1
            
    if pellet1.rect.y < 0 or pellet1.rect.y > 800:
        num_of_pellets -= 1
        pellet1.rect.x, pellet1.rect.y = randint(0, 800), randint(0, 800)
        pellet1 = SmallRect(30, 30, white, 10)
        num_of_pellets += 1
        
    if pellet2.rect.x < 0 or pellet2.rect.x > 800:
        num_of_pellets -= 1
        pellet2.rect.x, pellet2.rect.y = randint(0, 800), randint(0, 800)
        pellet2 = SmallRect(30, 30, white, 10)
        num_of_pellets += 1
            
    if pellet2.rect.y < 0 or pellet2.rect.y > 800:
        num_of_pellets -= 1
        pellet2.rect.x, pellet2.rect.y = randint(0, 800), randint(0, 800)
        pellet2 = SmallRect(30, 30, white, 10)
        num_of_pellets += 1
        
    if pellet3.rect.x < 0 or pellet3.rect.x > 800:
        num_of_pellets -= 1
        pellet3.rect.x, pellet3.rect.y = randint(0, 800), randint(0, 800)
        pellet3 = SmallRect(30, 30, white, 10)
        num_of_pellets += 1
        
    if p_health <= 0:
        deathtext = font.render("You died!", 1, white)
        screen.blit(deathtext, (350, 400))
        pygame.time.wait(4000)
        game = False
        
    # drawing code
    screen.fill(black)
    screen.blit(playarea, (150, 150))
    screen.blit(player.img, player.rect)
    screen.blit(pellet1.img, pellet1.rect)
    screen.blit(pellet2.img, pellet2.rect)
    screen.blit(pellet3.img, pellet3.rect) 
    screen.blit(beam.img, beam.rect)
    
    player.display_info()
    
    #print(player.rect.x, player.rect.y) # comment out when not needed
            
    pygame.display.flip()
    
    clock.tick(60)
