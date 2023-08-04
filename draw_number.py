import pygame, sys
from pygame.locals import *
import random, time
import numpy as np

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = [0, 0, 0]

#Other Variables for use in the program
num = 28

# Screen information
SCREEN_WIDTH = num * 10
SCREEN_HEIGHT = num * 10

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(RED)
pygame.display.set_caption("Number")

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.clr = BLACK.copy()
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def change_clr_by(self, c):
        for i in range(3):
            self.clr[i] = np.clip((self.clr[i] + c), 0, 255)
        self.image.fill(self.clr)

def draw(m, i, j, d):
    m[i][j].change_clr_by(d * 12)

    m[i-1][j].change_clr_by(d * 2)
    m[i+1][j].change_clr_by(d * 2)
    m[i][j-1].change_clr_by(d * 2)
    m[i][j+1].change_clr_by(d * 2)

    m[i-1][j-1].change_clr_by(d)
    m[i+1][j-1].change_clr_by(d)
    m[i-1][j+1].change_clr_by(d)
    m[i+1][j+1].change_clr_by(d)

    # matrix[i][j-2].change_clr_by(30)
    # matrix[i][j+2].change_clr_by(30)
    # matrix[i-2][j].change_clr_by(30)
    # matrix[i+2][j].change_clr_by(30)

    # matrix[i-2][j-1].change_clr_by(20)
    # matrix[i-2][j+1].change_clr_by(20)
    # matrix[i-1][j-2].change_clr_by(20)
    # matrix[i-1][j+2].change_clr_by(20)
    # matrix[i+1][j-2].change_clr_by(20)
    # matrix[i+1][j+2].change_clr_by(20)
    # matrix[i+2][j-1].change_clr_by(20)
    # matrix[i+2][j+1].change_clr_by(20)

    # matrix[i-2][j-2].change_clr_by(10)
    # matrix[i+2][j-2].change_clr_by(10)
    # matrix[i-2][j+2].change_clr_by(10)
    # matrix[i+2][j+2].change_clr_by(10)

all_sprites = pygame.sprite.Group()
matrix = [ [0 for i in range(num)] for j in range(num)]
y = 0
for i in range(num):
    x = 0
    for j in range(num):
        matrix[i][j] = Block(x, y)
        all_sprites.add(matrix[i][j])
        x += 10
    y += 10
    

while True:     
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if pressed[0]:
        for i in range(num):
            for j in range(num):
                if matrix[i][j].rect.collidepoint(pos):
                    draw(matrix,i,j,5)
    if pressed[2]:
        for i in range(num):
            for j in range(num):
                if matrix[i][j].rect.collidepoint(pos):
                    draw(matrix,i,j,-255)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)