# - CAP1 - S01 Player Focused Code - #
# - Xzavier Moosomin - #
# - File started on 05/21/2024 - #

# - Developer Notes - #
# - My plans for this file is to hopefully have it be able to run on its own
# - So that the player can freely move around in a pygame window
# - and then hopefully create a method so that when the player collides with something else
# - in another file work as intended.
# - Might be difficult though, so I'm not sure.
# - Included is a play area for the player.

# - Imports - #
import pygame
import sys

# - Pygame Initialization - #
pygame.init()

# - Constants - #
white = (255, 255, 255)
grey = (128, 128, 128)
darker_grey = (48, 48, 48)
black = (0, 0, 0)

# - Variables - #

gameon = True

p_health = 100
    
# - Game/Window Settings - #

screen_width, screen_height = 800, 800 # x, y pixels, starting from top left
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Player Testing')

clock = pygame.time.Clock()

# - Classes - #

class Player:
    def __init__(self):
        self.img = pygame.image.load('SPRITES/PLAYER/player_02.png').convert()
        self.rect = self.img.get_rect() # sets a collision box to the img
        self.rect.x = 375 # this and next line underneath determine
        self.rect.y = 375 # where the player spawns
        self.player_xpos, self.player_ypos = self.rect.x, self.rect.y
        
    def move(self, x, y):
        self.rect.x += x # im pretty sure this code 
        self.rect.y += y # makes the player able to move

        # this block of code makes sure that it doesn't go outside the box
        # for now, there is absolutely no chance for the player to roam outside
        # possibly later for the player to roam the screen...?
        
        # removed code for box, but will keep the movement restrictions
        # cause thats a lot of work to recreate
        if self.rect.left < 155: # left side of box
            self.rect.left = 155
            
        elif self.rect.right > 645: # right side of box
            self.rect.right = 645
            
        if self.rect.top < 155: # ceiling of box
            self.rect.top = 155
            
        elif self.rect.bottom > 645: # floor of box
            self.rect.bottom = 645

        
# - Create Objects - #

player = Player()
    
# - Code - #

while gameon == True:
    
    screen.fill(black)
    
    font = pygame.font.Font(None, 35) # fontstyle, fontsize
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    # ARROW KEY INPUT
    if keys[pygame.K_LEFT]:
        player.move(-5, 0) # 5 frames to the left
    
    if keys[pygame.K_RIGHT]:
        player.move(5, 0) # 5 frames to the right
    
    if keys[pygame.K_UP]:
        player.move(0, -5) # 5 frames up 
    
    if keys[pygame.K_DOWN]:
        player.move(0, 5) # 5 frames down
        
    # WASD INPUT
    if keys[pygame.K_a]:
        player.move(-5, 0) # 5 frames to the left
    
    if keys[pygame.K_d]:
        player.move(5, 0) # 5 frames to the right
    
    if keys[pygame.K_w]:
        player.move(0, -5) # 5 frames up 
    
    if keys[pygame.K_s]:
        player.move(0, 5) # 5 frames down

    # remember to comment out when not needed
    # print(player.rect.x, player.rect.y) # prints out the players position
    # from the top left of the sprite
    
    # display player image
    #screen.blit(player.img, player.rect)
    # health display text
    healthtext_01 = font.render("Player Health", 1, white)
    screen.blit(healthtext_01, (606, 50))
    
    healthtext_02 = font.render(f"{p_health}%", 1, white)
    screen.blit(healthtext_02, (650, 75))
    
    pygame.display.flip() # updates window
    
    clock.tick(60) # caps game speed 
