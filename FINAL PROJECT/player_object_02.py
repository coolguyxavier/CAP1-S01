# - CAP1-S01 Simple Projectiles and Player Code - #
# - Xzavier Moosomin - #
# - Started on 05/27/2024

# - Imports - #

import pygame
from random import randint

# - Pygame Initialization - #

pygame.init()

# - Constants - #

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font(None, 35) # fontstyle, fontsize

# - Variables - #
p_health = 100

game = True

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
        
    def check_boundary(self):
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
            
    def move(self, x, y):
        self.rect.x += x # im pretty sure this code 
        self.rect.y += y # makes the player able to move
        
            
    def display_info(self):
        # health display text
        
        healthtext_01 = font.render("Player Health", 1, white)
        screen.blit(healthtext_01, (606, 50))
        
        healthtext_02 = font.render(f"{p_health}%", 1, white)
        screen.blit(healthtext_02, (650, 75))
            
class Projectile:
    def __init__(self, width, height):
        self.width = width # dimensions
        self.height = height
        
        self.img = pygame.Surface([width, height])
        
        self.rect = self.img.get_rect()
        self.rect.x = randint(0, 800) # spawn location
        self.rect.y = randint(0, 800)
        
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
        
# - Create Object(s)

player = Player()
bullet_01 = SmallRect(30, 60, red) # we can comment out
bullet_02 = SkinnyLong(15, 100, blue)
bullet_03 = ShortThick(60, 30, green)

# - Main Code - #

while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()
        
        # WASD INPUT
        if keys[pygame.K_a]:
            player.move(-5, 0) # 5 frames to the left
        
        if keys[pygame.K_d]:
            player.move(5, 0) # 5 frames to the right
        
        if keys[pygame.K_w]:
            player.move(0, -5) # 5 frames up 
        
        if keys[pygame.K_s]:
            player.move(0, 5) # 5 frames down
            
        if pygame.Rect.colliderect(player.rect, bullet_01.rect):
            p_health -= 1
            
        if pygame.Rect.colliderect(player.rect, bullet_02.rect):
            p_health -= 1
            
        if pygame.Rect.colliderect(player.rect, bullet_03.rect):
            p_health -= 1
        
        screen.fill(black)
        screen.blit(player.img, player.rect)
        screen.blit(bullet_01.img, bullet_01.rect)
        screen.blit(bullet_02.img, bullet_02.rect)
        screen.blit(bullet_03.img, bullet_03.rect)
        
        player.check_boundary()
        
        player.display_info()
        
        if p_health <= 0:
            deathtext = font.render("You died!", 1, white)
            screen.blit(deathtext, (350, 400))
            pygame.time.wait(4000)
            game = False
            
        pygame.display.flip()
        clock.tick(60)
