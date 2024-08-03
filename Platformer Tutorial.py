import sys
import pygame
from pygame.locals import *

pygame.init()

running = True
TITLE = "Platformer"
WIDTH, HEIGHT = 400, 450
ACC = 0.5
FRIC = -0.12
FPS = 60
DT = 0

CLOCK = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30)) # sprite size
        self.surf.fill((128,255,40)) # sprite color
        self.rect = self.surf.get_rect(center = (10, 420)) # sprite position

        self.pos = pygame.Vector2((10,385))
        self.vel = pygame.Vector2(0,0)
        self.acc = pygame.Vector2(0,0)

    def move(self):
        self.acc = pygame.Vector2(0,0)

        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            self.acc.x += -ACC
            print("left")
        if pressed_key[K_RIGHT]:
            self.acc.x += ACC
        if pressed_key[K_ESCAPE]:
            pygame.quit()

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = WIDTH
        
        self.rect.midbottom = self.pos

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20)) # sprite size
        self.surf.fill((255, 0, 0)) # sprite color
        self.rect = self.surf.get_rect(center = (WIDTH / 2, HEIGHT - 10)) # sprite position

        self.pos = pygame.Vector2((10,385))
        self.vel = pygame.Vector2(0,0)
        self.acc = pygame.Vector2(0,0)

p1 = platform()
plr = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(Player())
all_sprites.add(platform())

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    displaysurface.fill((255,255,255))

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    plr.move()

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()