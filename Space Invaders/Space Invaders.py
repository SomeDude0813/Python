import pygame
from pygame.locals import *

w, h = 500,500
screen = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()
fps = 60
dt = 0

img_folder = "/home/christian/Desktop/Scripts/Python/Space Invaders"
alien_img = pygame.transform.scale(pygame.image.load(f"{img_folder}/LargeAlien.png"), (32, 32))
bg_img = pygame.image.load(f"{img_folder}/background.png")

#player variables
player_img = pygame.transform.scale(pygame.image.load(f"{img_folder}/Spaceship.png").convert(), (64, 64)) # .convert() images when loading them
player_pos = pygame.Vector2(screen.get_width() / 2, 350)
player_speed = 200

running = True
class Main():    
    def render():
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
        screen.blit(bg_img, (0,0))
        
        #player
        screen.blit(player_img, player_pos)
        screen.blit(alien_img, (screen.get_width() / 2, 100))
        
    def shoot():
        bullet = pygame.draw.circle(screen, "black", 350,400)
        bullet_pos = pygame.Vector2(350,400)
        bullet_speed = -10
        
    while running:
        render()
        
        keys = pygame.key.get_pressed()
        #movement
        if keys[pygame.K_a]:
            player_pos.x -= player_speed * dt
        if keys[pygame.K_d]:
            player_pos.x += player_speed * dt
        
        
        if keys[pygame.K_ESCAPE]:
            running = False
        
        pygame.display.flip()
        clock.tick(fps)
        dt = clock.tick(fps) / 1000
        
pygame.quit()