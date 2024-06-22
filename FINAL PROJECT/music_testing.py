# - CAP1-S01 Playing With Music Files - #
# - Xzavier Moosomin - #
# - File created on: 06/18/2024  - #

# - Developer Comments - #
# so i got bored one day and decided to incorporate music into my game
# i thought it was getting boring moving a lil character around in the box
# back and forth, constantly dodging little white squares
# so i decided to add music so its significantly less tormenting.


# - Imports - #

import pygame
from pygame import mixer
from math import cos, sin, atan2
from random import randint


# - Pygame Initialization - #

pygame.init()
mixer.init() # initializes the mp3 player


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
start_time = 0


# - Music Settings - #

# choose one or the other by commenting out
#mixer.music.load('MUSIC/BATTLE/battle_01.mp3') # funny yellow fella
mixer.music.load('MUSIC/BATTLE/battle_02.mp3') # funny robot fella 
mixer.music.set_volume(0.1) # i think the volume can only be between 0 and 1
mixer.music.play() # plays the music 


# - Variables - #

p_health = 100

game = True

num_of_pellets = 3

backflip = False


# - Classes - #

class Player:
    def __init__(self):
        self.img = pygame.image.load('SPRITES/PLAYER/player_04.png').convert()
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
        
        time_01 = font.render("Time Survived:", 1, white)
        screen.blit(time_01, (50, 50))
        
        # Calculate elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        seconds = font.render(f"{elapsed_time:.2f} s", 1, white)
        screen.blit(seconds, (100, 75))
        
        
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
                
    def rotate(self):
        self.img = pygame.transform.rotate(self.img, -90)
        
            
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
        #self.rect.x, self.rect.y = (0, 0) # test spawn location
        
    def move_left(self):
        self.rect.x -= self.speed
        
    def move_up(self):
        self.rect.y -= self.speed
        

class P_Projectile(Player, Projectile): # added player class as inheritence so it can be called with player
    def __init__(self, width, height, color, speed):
        self.color = color
        self.img = pygame.Surface((width, height))
        self.img.fill(self.color)
        
        self.speed = speed
        
        self.rect = self.img.get_rect() # creates placeholder rect on top of the image
        self.rect.x, self.rect.y = (player.rect.x, player.rect.y) # spawns at the players location
        self.angle = 270 # shoots up
        
    def shoot(self):
        
        
# - Create Object(s)

player = Player()
pellet1 = SmallRect(30, 30, white, 10) # cheap way of doing it
pellet2 = SmallRect(30, 30, white, 10) # but that would be
pellet3 = SmallRect(30, 30, white, 10) # too much work and i dont have a big enough time frame
p_proj = P_Projectile(30, 60, blue, 10) # player projectile


# - Main Code - #

while game == True:
    
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
        
    # kill button
    if keys[pygame.K_3]:
        p_health = 0
        pygame.display.flip()
        
    # - ARROW KEY MOVEMENTS - #
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_UP]:
        player.move(0, -5)
    if keys[pygame.K_DOWN]:
        player.move(0, 5)
        
    if keys[pygame.K_b]:
        backflip = True
        
    if keys[pygame.K_b] and backflip == True:
        backflip = True
        
    if keys[pygame.K_e]:
        p_proj.shoot()
        
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
    if pygame.Rect.colliderect(player.rect, beam.rect):
        p_health -= 1
        
    pellet1.move()
    pellet2.move()
    pellet3.move()
    
    # if pellet is off the top/bottom of the screen, create new
    # pellet number 1
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
    
    # pellet number 2
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
        
    # pellet number 3
    if pellet3.rect.x < 0 or pellet3.rect.x > 800:
        num_of_pellets -= 1
        pellet3.rect.x, pellet3.rect.y = randint(0, 800), randint(0, 800)
        pellet3 = SmallRect(30, 30, white, 10)
        num_of_pellets += 1
        
    if p_health <= 0:
        deathtext = font.render("You died!", 1, white)
        mixer.music.fadeout(1500)
        screen.blit(deathtext, (350, 400))
        pygame.display.flip()
        pygame.time.wait(4000)
        game = False
        
    if backflip == True:
        player.rotate() # rotate img by 1 degree for constant flip
    
        
    # drawing code
    screen.fill(black) # fill screen
    screen.blit(playarea, (150, 150)) # create play area
    screen.blit(player.img, player.rect) # draw player
    screen.blit(pellet1.img, pellet1.rect) # create
    screen.blit(pellet2.img, pellet2.rect) # the
    screen.blit(pellet3.img, pellet3.rect) # pellets
    screen.blit(beam.img, beam.rect) # spawn the beam
    
    player.display_info() # display player health
    
    #print(player.rect.x, player.rect.y) # comment out when not needed
    
    #if backflip == True: # comment out when not needed
        #print("Backflip engaged!")
            
    pygame.display.flip() # update screen
    
    clock.tick(60)
