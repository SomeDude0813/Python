import pygame
from pygame.locals import *
import random

pygame.init() # initialize pygame

# get framerate with pygame clock
clock = pygame.time.Clock()
fps = 60

# store window width and height
screen_width = 864
screen_height = 936

screen = pygame.display.set_mode( (screen_width, screen_height) )  # initialize pygame.display w/ width & height (set_mode)
pygame.display.set_caption('Flappy Bird')  # set window title to Flappy Bird

# define game variables
ground_scroll = 0
scroll_speed = 4

# load images
    # background img
    # ground img

# start game loop with constant run variable

    # start the game clock fps
    
    # initialize game images
        # draw background
        # draw and scroll the ground
        
    # loop through pygame.event
        # if event is QUIT
            # disable main game loop
            
    # update display
            
pygame.quit()