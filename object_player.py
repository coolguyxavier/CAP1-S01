import player_movement
import spawncube
import pygame

pygame.init()

screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Object and Player Testing')

projectile_01 = spawncube.SmallRect(30, 60, red)
player_01 = player_movement.player

for event in event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
    
    screen.blit(projectile_01.img, projectile_01.rect)
    screen.blit(player_01.img, player_01.rect)