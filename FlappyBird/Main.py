import pygame
from pygame.locals import *
import sys
import time
import random

pygame.init() # initialize pygame

# initialize clock and fps
CLOCK = pygame.time.Clock()
FPS = 60
DT = 0

# store window size
WIDTH = 864
HEIGHT = 936

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # initialize screen
pygame.display.set_caption('Flappy Bird')  # set window title

#load images
IMAGES = 'FlappyBird/img'
bg = pygame.image.load( f'{IMAGES}/bg.png' )
ground_img = pygame.image.load( f'{IMAGES}/ground.png' )


# game variables
FLYING = False
GAME_OVER = False
ground_height = 768
ground_scroll = 0
scroll_speed = 4 # moves by x amount of pixels every iteration of the game
pipe_gap = 150 # the opening in between pipes
pipe_frequency = 1500 # (in milliseconds) the pipes rate of spawn
last_pipe = pygame.time.get_ticks() - pipe_frequency

# define bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) # initialize sprite class (blit functions coded into this class which is convenient)
        self.images = []
        self.index = 0 # selects the image shown (animation controller)
        self.counter = 0 # control speed of animation
        for num in range(1,4): # loop through the range of images
            img = pygame.image.load(f'{IMAGES}/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]  # assign sprite image
        self.rect = self.image.get_rect() # create rectangle for image boundaries
        self.rect.center = [x,y]  # set image position as center point
        self.vel = 0 # sprite velocity
        self.clicked = False
        
    def update(self): #add update functionality to the sprite
        
        # gravity
        if FLYING == True: # prevents falling until a key is pressed
            self.vel += 0.5 # increase velocity per iteration
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < ground_height: # only continue falling if position is above ground (prevents ground noclipping)
                self.rect.y += int(self.vel)
        if GAME_OVER == False:
            # jumping
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # Check if lmb was pressed
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
            # handle the animation
            self.counter += 1
            flap_cooldown = 15 # max amount of iterations
            
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):  # check if index is higher than available image length
                    self.index = 0
            self.image = self.images[self.index]
                    
            # rotate the bird
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2) # velocity is the angle of rotation
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90) # flip bird over when it dies
        
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__()
        self.image = "FlappyBird/img/pipe.png"
        self.rect = self.image.get_rect()
        # position 1 is the top, -1 is the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)] # position centered at bottom left
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)] # pipe is spawned at center thats why gap is divided

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0: # if pipe goes off screen
            self.kill()

# groups come with sprite classes and the same/extra functions
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(HEIGHT / 2)) # initialize and set Bird position

bird_group.add(flappy) # add character to group list

def render():
    # draw image
    SCREEN.blit(bg, (0,0))
    
    # draw and scroll the ground
    SCREEN.blit(ground_img, (ground_scroll, ground_height)) # adjust X position with scroll variable

    # draw character (bird)
    bird_group.draw(SCREEN) # sprites get drawn with this function
    pipe_group.draw(SCREEN)
    bird_group.update()
    pipe_group.update()

    pygame.display.update() # updates display
    pygame.display.flip()


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # makes closing the window possible
        if event.type == pygame.MOUSEBUTTONDOWN and FLYING == False and GAME_OVER == False: # to prevent game starting on entry (starts when player is ready to play)
            flying = True


# main game loop
run = True
while run:
    render()
    events()

    if GAME_OVER == False: # Stops scrolling when game is over
       ground_scroll -= scroll_speed
       if abs(ground_scroll) > 35:
           ground_scroll = 0

    # look for collision
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False): # kill entity: false 
        GAME_OVER = True

    # check if bird has hit the ground
    if flappy.rect.bottom > ground_height:
        GAME_OVER = True
        FLYING = False

    if GAME_OVER == False and FLYING == True:
        # generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, -1)
            top_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now
    

    CLOCK.tick(FPS) # run framerate
    DT = CLOCK.tick(FPS) / 1000
    
            
pygame.quit()
sys.exit()