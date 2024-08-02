import pygame
from pygame.locals import *

pygame.init() # initialize pygame

# initialize clock and fps
clock = pygame.time.Clock()
fps = 60

# store window size
screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))  # initialize screen
pygame.display.set_caption('Flappy Bird')  # set window title

#load images
img_folder = '/home/christian/Desktop/Scripts/Python/FlappyBird/img'
bg = pygame.image.load( f'{img_folder}/bg.png' )
ground_img = pygame.image.load( f'{img_folder}/ground.png' )


# game variables
ground_height = 768
ground_scroll = 0
scroll_speed = 4 # moves by x amount of pixels every iteration of the game
game_over = False
flying = False

# define bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) # initialize sprite class (blit functions coded into this class which is convenient)
        self.images = []
        self.index = 0 # selects the image shown (animation controller)
        self.counter = 0 # control speed of animation
        for num in range(1,4): # loop through the range of images
            img = pygame.image.load(f'{img_folder}/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]  # assign sprite image
        self.rect = self.image.get_rect() # create rectangle for image boundaries
        self.rect.center = [x,y]  # set image position as center point
        self.vel = 0 # sprite velocity
        self.clicked = False
        
    def update(self): #add update functionality to the sprite
        
        # gravity
        if flying == True: # prevents falling until a key is pressed
            self.vel += 0.5 # increase velocity per iteration
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < ground_height: # only continue falling if position is above ground (prevents ground noclipping)
                self.rect.y += int(self.vel)
        if game_over == False:
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
        
        
# groups come with sprite classes and the same/extra functions
bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2)) # initialize and set Bird position

bird_group.add(flappy) # add character to group list


# main game loop
run = True
while run:
    
    clock.tick(fps) # run framerate
    
    # draw image
    screen.blit(bg, (0,0))
    
    
    # draw and scroll the ground
    screen.blit(ground_img, (ground_scroll, ground_height)) # adjust X position with scroll variable
    
    if game_over == False: # Stops scrolling when game is over
       ground_scroll -= scroll_speed
       if abs(ground_scroll) > 35:
           ground_scroll = 0
    
    # draw character (bird)
    bird_group.draw(screen) # sprites get drawn with this function
    bird_group.update()
    
    # check if bird has hit the ground
    if flappy.rect.bottom > ground_height:
        game_over = True
        flying = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # makes closing the window possible
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False: # to prevent game starting on entry (starts when player is ready to play)
            flying = True
            
    pygame.display.update() # updates display
            
pygame.quit()