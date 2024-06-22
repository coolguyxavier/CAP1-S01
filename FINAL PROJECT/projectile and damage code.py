# - CAP1-S01 Code for Damaging Sprites - #
# - Xzavier Moosomin - #
# - Started on 05/22/2024 - #

# - Developer Notes - #
# not gonna lie, i might use external files for this, it seems like the play
# instead of copying it all over, I can just
# use code by importing it
# that'll be cool
# i'll be importing the player movement code in

# or maybe i'll copy/paste some of it and then import some of it, that'll be useful

# - Imports - #
import pygame
#import player_movement # the file where i made the player movement code
import environment_testing # the file where i made the environment
import spawncube # the file where i made the objects and classes
from random import randint
import sys

# - Pygame Initialization - #
pygame.init() # this function is so cool, it needs its own category

# - Constants - #

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# - Variables - #

gameon = True

# - Game Initialization - #

screen_width, screen_height = 800, 800 # x, y pixels, starting from top left
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Projectile Testing')
clock = pygame.time.Clock()

# - Classes - #

# imported the classes already?

# - Create Object - #
#player = player_movement.Player() # imported from player_movement.py - ngl im surprised i did that
# enviro_01 = environment_testing.background_01 # remember to comment
# playarea = environment_testing.playarea # out when not in use!!
bullet_01 = spawncube.SmallRect(30, 60, red)

# - Main Code - #

while gameon == True:
    
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # screen.blit(enviro_01, (0, 0)) # REMEMBER TO COMMENT OUT 
    # screen.blit(playarea, (150, 150)) # WHEN NOT IN USE!!!
    screen.blit(bullet_01.img, bullet_01.rect)
    
    pygame.display.flip()
    clock.tick(60)
            