import pygame, sys
from pygame.locals import *
import numpy as np
from MY_CONSTANTS import *
from Create_Rect import *
from Create_Circle import *

def check_collision_circle(ball_1, ball_2):
    if pygame.sprite.collide_circle(ball_1, ball_2):
        pos1 = [ball_1.x, ball_1.y]
        pos2 = [ball_2.x, ball_2.y]
        hypotenuse = round(np.sqrt((ball_1.x-ball_2.x)**2 + (ball_1.y-ball_2.y)**2)) # math.hypot
        farther_cathetus = np.abs(ball_1.y-ball_2.y)
        proximate_cathetus = np.abs(ball_1.x-ball_2.x)
        sin_of_angle = farther_cathetus / hypotenuse
        cos_of_angle = proximate_cathetus / hypotenuse
        angle = math.asin(sin_of_angle)

        pass

def display():
    pygame.init()
    FramePerSec = pygame.time.Clock()

    font_small = pygame.font.SysFont("Verdana", 20)
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("pulse")

    r1 = Create_Rect(size_x = 100, size_y = 100, x = 600, y = 300, m = 1, v = 5, angle = 45)
    c1 = Create_Circle(size = 100, x = 600, y = 300, m = 1, v = 10, angle = 30)
    c2 = Create_Circle(size = 100, x = 600, y = 300, m = 1, v = 5, angle = 60)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(c2)
    all_sprites.add(c1)

    while True:

        DISPLAYSURF.fill(WHITE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    for entity in all_sprites:
                        pass

        for entity in all_sprites:
            entity.move()
            DISPLAYSURF.blit(entity.image, entity.rect)
        info = font_small.render("time: {ti}".format(ti=pygame.time.get_ticks()/1000), True, BLACK)
        DISPLAYSURF.blit(info, (0,0))

        pygame.display.update()
        FramePerSec.tick(FPS)