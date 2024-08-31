import pygame
from pygame.locals import *

pygame.init()


CLOCK = pygame.time.Clock()
FPS = 60
DT = 0

WIDTH, HEIGHT = 500, 500
CENTER = WIDTH / 2, HEIGHT / 2
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')
time = 0

player_img = pygame.transform.scale(pygame.image.load('Space Invaders/Spaceship.png'), (65, 65))
player_pos = pygame.Vector2( CENTER[0], 400 )
player_speed = 300
last_shot = 0
shot_cd = 1.5


background_img = pygame.image.load('Space Invaders/background.jpg')

class bullet_sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive = False
        self.image = pygame.transform.scale(pygame.image.load('Space Invaders/bullet.png'), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.speed = 50
        self.vel = 10
        
    def update(self):
        if self.alive:
            self.rect.y -= self.vel
            if self.rect.top <= 0:
                self.alive = False
                self.kill()

class alien_sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('Space Invaders/Alien.png'), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.speed = 5
        
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= (WIDTH - self.rect.width): # right side of the screen
            self.speed = self.speed * -1
        if self.rect.x <= 0: # left side of the screen
            self.speed = self.speed * -1

bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()

alien = alien_sprite(100, 100)
alien_group.add(alien)



def render():
    SCREEN.blit(background_img, (0,0))
    SCREEN.blit(player_img, player_pos)
    
    bullet_group.draw(SCREEN)
    bullet_group.update()
    alien_group.draw(SCREEN)
    alien_group.update()
    
    pygame.display.flip()
    pygame.display.update()
    
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            
        # handle player input    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                last_shot = time
                bullet.alive = True
                bullet_group.add(bullet)
                
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        run = False
        pygame.quit()
        

run = True
while run:
    render()
    events()
    
    bullet = bullet_sprite(player_pos.x + 30, player_pos.y)
    
    keys = pygame.key.get_pressed()
    if keys[K_d]:
        player_pos.x += player_speed * DT
    if keys[K_a]:
        player_pos.x -= player_speed * DT
        
    
    time = pygame.time.get_ticks() # game clock since initialization
    CLOCK.tick(FPS)
    DT = CLOCK.tick(FPS) / 1000
