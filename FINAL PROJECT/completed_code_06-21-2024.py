# - CAP1-S01 Final Code Hand In - #
# - Xzavier Moosomin - #
# - File created on: 06/18/2024  - #

# - Developer Comments - #
# Man, in the single month that I had to do this, I did less than I had hoped.
# I do not see this as a failure, I see this as a chance that I had not properly utilized.
# I see it that this has pushed my knowledge of computer science enough. Sure, it didn't really utilize
# EVERY aspect of Python, but I believe that I had achieved an adequte - if not proper - understanding
# of its mechanics.


# - Imports - #

import pygame
from pygame import mixer
from math import cos, sin, atan2
from random import randint


# - Pygame Initialization - #

pygame.init()
mixer.init() # initializes the mp3 player


# - Constants - #

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font(None, 35) # fontstyle, fontsize
start_time = 0


# - Game Setting - #

screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Object and Player 02 Testing')

clock = pygame.time.Clock()


# - Load Images - #
background_02 = pygame.image.load('SPRITES/PLAY AREA/background_02.png').convert()
playarea = pygame.image.load('SPRITES/PLAY AREA/box_01.png').convert()
bad_guy = pygame.image.load('SPRITES/CHARACTERS/sans.png').convert()
bad_guy = pygame.transform.scale(bad_guy, (350, 350))
pygame.Surface.set_colorkey(bad_guy, black)


# - Music Settings - #

# choose one or the other by commenting out

#mixer.music.load('MUSIC/BATTLE/battle_01.mp3') # funny yellow fella
mixer.music.load('MUSIC/BATTLE/battle_02.mp3') # funny robot fella

mixer.music.set_volume(0.1) # i think the volume can only be between 0 and 1
mixer.music.play(-1) # -1 makes the music loop

channel1 = mixer.Channel(0)
channel2 = mixer.Channel(1)
hit_sound = mixer.Sound('MUSIC/SFX/damage.mp3') # # sound hit effect


# - Variables - #

p_health = 100

game = True

backflip = False

heals_left = 1


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
        
        # convert all that fun stuff to seconds
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        seconds = font.render(f"{elapsed_time:.2f} s", 1, white)
        screen.blit(seconds, (100, 75))
        
        # heal button
        heal_text_01 = font.render("Heal = E", 1, white)
        screen.blit(heal_text_01, (25, 150))
        
        heal_text_02 = font.render("Heals left:", 1, white)
        screen.blit(heal_text_02, (5, 175))
        
        heal_text_03 = font.render(str(heals_left), 1, white)
        screen.blit(heal_text_03, (130, 176))
        
        
        
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
        
        
# - Create Object(s)

player = Player()
pellet1 = SmallRect(30, 30, white, 10) # cheap way of doing it
pellet2 = SmallRect(30, 30, white, 10) # but that would be
pellet3 = SmallRect(30, 30, white, 10) # too much work and i dont have a big enough time frame
pellet4 = SmallRect(30, 30, white, 10)
pellet5 = SmallRect(30, 30, white, 10)

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
        
    # - ARROW KEY MOVEMENTS - #
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_UP]:
        player.move(0, -5)
    if keys[pygame.K_DOWN]:
        player.move(0, 5)
    
    # makes the player infinitely spin
    if keys[pygame.K_b]:
        backflip = True
    
    # heal button
    if keys[pygame.K_e] and heals_left != 0 and p_health <= 25:
        heals_left -= 1
        p_health += 100
        
    # kill button
    if keys[pygame.K_3]:
        p_health = 0
        pygame.display.flip()
        
    # mini logic code 
    if pygame.Rect.colliderect(player.rect, pellet1.rect):
        p_health -= 1
        channel1.play(hit_sound)
    if pygame.Rect.colliderect(player.rect, pellet2.rect):
        p_health -= 1
        channel1.play(hit_sound)
    if pygame.Rect.colliderect(player.rect, pellet3.rect):
        p_health -= 1
        channel1.play(hit_sound, 1)

    # object movements
    pellet1.move()
    pellet2.move()
    pellet3.move()
    pellet4.move()
    pellet5.move()
    
    
    # if pellet is off the top/bottom of the screen, create new
    # pellet number 1
    if pellet1.rect.x < 0 or pellet1.rect.x > 800:
        pellet1.rect.x, pellet1.rect.y = randint(0, 800), randint(0, 800)
        pellet1 = SmallRect(30, 30, white, 10)
            
    if pellet1.rect.y < 0 or pellet1.rect.y > 800:
        pellet1.rect.x, pellet1.rect.y = randint(0, 800), randint(0, 800)
        pellet1 = SmallRect(30, 30, white, 10)
    
    # pellet number 2
    if pellet2.rect.x < 0 or pellet2.rect.x > 800:
        pellet2.rect.x, pellet2.rect.y = randint(0, 800), randint(0, 800)
        pellet2 = SmallRect(30, 30, white, 10)
            
    if pellet2.rect.y < 0 or pellet2.rect.y > 800:
        pellet2.rect.x, pellet2.rect.y = randint(0, 800), randint(0, 800)
        pellet2 = SmallRect(30, 30, white, 10)
        
    # pellet number 3
    if pellet3.rect.x < 0 or pellet3.rect.x > 800:
        pellet3.rect.x, pellet3.rect.y = randint(0, 800), randint(0, 800)
        pellet3 = SmallRect(30, 30, white, 10)
    
    # pellet number 4
    if pellet4.rect.x < 0 or pellet4.rect.x > 800:
        pellet4.rect.x, pellet4.rect.y = randint(0, 800), randint(0, 800)
        pellet4 = SmallRect(30, 30, white, 10)
        
    # pellet number 5
    if pellet5.rect.x < 0 or pellet5.rect.x > 800:
        pellet5.rect.x, pellet5.rect.y = randint(0, 800), randint(0, 800)
        pellet5 = SmallRect(30, 30, white, 10)

    
    # if player health is less than or equal to 0, game ends
    if p_health <= 0:
        deathtext = font.render("You died!", 1, white)
        mixer.music.fadeout(1500) # music takes 1.5 seconds to fade out
        screen.blit(deathtext, (350, 400))
        pygame.display.flip()
        pygame.time.wait(4000)
        game = False
        
    if backflip == True:
        player.rotate() # rotate player.img by 1 degree for constant flip
    
        
    # drawing code
    screen.fill(black) # fill screen
    screen.blit(background_02, (0, 0)) # background
    screen.blit(bad_guy, (225, 1))
    screen.blit(playarea, (150, 150)) # create play area
    screen.blit(player.img, player.rect) # draw player
    screen.blit(pellet1.img, pellet1.rect) # create
    screen.blit(pellet2.img, pellet2.rect) # the
    screen.blit(pellet3.img, pellet3.rect) # pellets
    screen.blit(pellet4.img, pellet4.rect) # the
    screen.blit(pellet5.img, pellet5.rect) # pellets
    
    player.display_info() # display player health
    
    #print(player.rect.x, player.rect.y) # comment out when not needed
    
    #if backflip == True: # comment out when not needed
        #print("Backflip engaged!")
    
            
    pygame.display.flip() # update screen
    
    clock.tick(60)


