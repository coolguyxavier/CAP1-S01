# - CAP1-S01 Environmental Based Code - #
# - Xzavier Moosomin - #
# - Started on 05/22/2024 - #

# - Developer Notes - #
# i only made this file because i realized that the environmental part inside the player movement code
# was taking up space and only made the thing slower
# so i decided to put the environmental code inside here. much better!

# BUT WAIT THERE IS MORE
# what if i could introduce a mechanic that allows the player outside of the play area?

# - Imports - #
import pygame

# - Pygame Initalization - #
pygame.init()

# - Game Settings - #

screen_width, screen_height = 800, 800 # x, y pixels, starting from top left
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Environment Testing')


# - Constants - #
black = (0, 0, 0)
white = (255, 255, 255)

background_01 = pygame.image.load('SPRITES/PLAY AREA/background_02.png').convert()
playarea = pygame.image.load('SPRITES/PLAY AREA/box_01.png').convert()

# - Variables - #

run = True

# - Main Code - #

while run == True:
    
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.blit(background_01, (0, 0))
    screen.blit(playarea, (150, 150))
    
    pygame.display.flip()