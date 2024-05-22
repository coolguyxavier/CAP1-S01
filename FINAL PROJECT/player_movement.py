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

# - Constants - #
white = (255, 255, 255)
black = (0, 0, 0)
center = 275, 275

# - Game/Window Settings - #
pygame.init()

screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Player Movement Test')

clock = pygame.time.Clock()

# - Classes - #

class Player:
    def __init__(self):
        self.img = pygame.image.load('SPRITES/PLAYER/player_02.png')
        self.rect = self.img.get_rect()
        self.rect.x = 275
        self.rect.y = 275
        
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

        # this block of code makes sure that it doesn't go outside the window
        if self.rect.left < 0:
            self.rect.left = 0
            
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            
        if self.rect.top < 0:
            self.rect.top = 0
            
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        
    
# - Create Objects - #

player = Player()
#player.rect = center
    
# - Code - #

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
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
    elif keys[pygame.K_a]:
        player.move(-5, 0) # 5 frames to the left
    
    elif keys[pygame.K_d]:
        player.move(5, 0) # 5 frames to the right
    
    elif keys[pygame.K_w]:
        player.move(0, -5) # 5 frames up 
    
    elif keys[pygame.K_s]:
        player.move(0, 5) # 5 frames down
            
    screen.fill(black)
    screen.blit(player.img, player.rect)
    pygame.display.flip()
    clock.tick(60)
