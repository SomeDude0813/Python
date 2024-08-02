import pygame
from pygame.locals import *

pygame.init()

window_title = "Project"
w, h = 1280, 720

# Set up the display
pygame.display.set_caption(window_title)
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_speed = 500 # Default 300

def render():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white") # fill the screen with a color to wipe away anything from last frame
    
    pygame.draw.circle(screen, "black", player_pos, 40) # Player

# Main game
while running:
    render()
    # Keybindings
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += player_speed * dt
        
    if keys[pygame.K_ESCAPE]: # Force quit
        pygame.quit()
    
    pygame.display.flip() # flip() the display to put your work on screen
    
    clock.tick(60) # limits FPS to 60
    dt = clock.tick(60) / 1000 # dt is delta time in seconds since last frame, used for framerate independent physics.
    
pygame.quit() #pygame.QUIT event means the user clicked X to close your window