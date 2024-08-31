import pygame
import time
import sys
import numpy as np
import cv2 as cv
from pygame.locals import *

pygame.init()

WIDTH = 232
HEIGHT = 256

CLOCK = pygame.time.Clock()
DT = 0
FPS = 60

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CENTER = WIDTH / 2, HEIGHT / 2
pygame.display.set_caption("Pacman")

sprites_path = "Pacman/Sprites"
map_img = pygame.transform.scale(
        pygame.image.load(f"{sprites_path}/maze.png"), (WIDTH, HEIGHT))
pacman_spritesheet = pygame.image.load(f"{sprites_path}/pacman.png").convert_alpha()


# detect pixel colors for collision
def check_pixel_color(x, y, width, height):
    pixel_color = map_img.get_atmap_img.subsurface(pygame.Rect(x, y, width, height))
    
    print(pixel_color)
    
# Animation is a work in progress
class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.frame_count = 2
        self.width = 16
        self.height = 16
        self.directions = {
            "right"
        }
        self.direction = ""
        self.next_dir = ""
        self.speed = 200
        # animation
        #self.frames = [pygame.Rect(i * self.width, 0, self.width, self.height) for i in range(self.frame_count)]  # stores frame coordinates with a for loop
        #self.frame_surfaces = [pacman_spritesheet.subsurface(self.rect) for self.rect in self.frames] # grabs surface images from coordinates in frames
        #self.current_frame = 1
        #self.image = self.frame_surfaces[self.current_frame]
        #self.frame_rate = 10
        #self.frame_delay = 1000 / self.frame_rate # 
        self.rect = pygame.Rect(32, 0, self.width, self.height)
        self.image = pacman_spritesheet.subsurface(self.rect)
        self.rect.center = [x, y]
        self.last_update_time = pygame.time.get_ticks()

    def move(self, directionX, directionY):
        self.rect.x += directionX * self.speed * DT
        self.rect.y += directionY * self.speed * DT
        
    def update(self):
        self.current_time = pygame.time.get_ticks()
        #print(self.last_update_time, self.current_time, self.current_time - self.last_update_time)
        #print(self.current_frame)
        #if self.current_time - self.last_update_time >= self.frame_delay:
        #    self.current_frame = (self.current_frame + 1) % self.frame_count
        #    self.last_update_time = self.current_time
        

Player = pygame.sprite.Group()

pacman = Pacman(117, 143)
Player.add(pacman)


def render():
    SCREEN.blit(map_img, (0,0))    
    Player.draw(SCREEN)
    Player.update()
    
    pygame.display.flip()
    pygame.display.update()
    
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
run = True
while run:
    render()
    events()
    
    key = pygame.key.get_pressed()
    if key[K_ESCAPE]:
        run = False
        
    # check if input direction has a wall infront of it
    # if it does then delay the input (next_input) until it is available
    # change next_input if player presses another key whilst it is also blocked
    # if input is availble then set current_input
    
    
    CLOCK.tick(FPS)
    DT = CLOCK.tick(FPS) / 1000
    
pygame.quit()
sys.exit()