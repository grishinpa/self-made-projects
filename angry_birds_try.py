from random import randrange
import pygame as pg
import sys
import pymunk.pygame_util
from pymunk.vec2d import Vec2d
pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 1200,600
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
FramePerSec = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = (0, 1000)

def zero_gravity(body, gravity, damping, dt):
    pymunk.Body.update_velocity(body, (0,0), damping, dt)

def default_gravity(body, gravity, damping, dt):
    pymunk.Body.update_velocity(body, space.gravity, damping, dt)

class Create_Ball(pg.sprite.Sprite):
    def __init__(self, size, x, y, m, v):
        super().__init__()

        self.ball_mass = m
        self.ball_radius = size
        ball_momemt = pymunk.moment_for_circle(self.ball_mass, 0, self.ball_radius)
        self.ball_body = pymunk.Body(self.ball_mass, ball_momemt)
        self.ball_body.position = (x, y)
        self.ball_body.velocity = v
        self.ball_body.velocity_func = zero_gravity
        ball_shape = pymunk.Circle(self.ball_body, self.ball_radius)
        ball_shape.color = pg.color.THECOLORS['orange']
        ball_shape.elasticity = 0.8
        ball_shape.friction = 0.5
        space.add(self.ball_body, ball_shape)

        # self.size = size
        # self.x = x
        # self.y = y
        # self.clr = pg.color.THECOLORS['blue']
        # self.image = pg.Surface((self.size, self.size), pg.SRCALPHA)
        # pg.draw.ellipse(self.image, self.clr, [0, 0, size, size])
        # self.rect = self.image.get_rect(center=(self.x, self.y))

def create_box(space, pos):
    box_mass, box_size = 1, (40,60)
    box_momemt = pymunk.moment_for_box(box_mass, box_size)
    box_body = pymunk.Body(box_mass, box_momemt)
    box_body.position = pos
    box_shape = pymunk.Poly.create_box(box_body, box_size)
    box_shape.color = [randrange(256) for i in range(4)]
    box_shape.elasticity = 0.1
    box_shape.friction = 1.0
    space.add(box_body, box_shape)
    return box_body

def create_segment(from_, to_, thickness, space, color):
    segment_shape = pymunk.Segment(space.static_body, from_, to_, thickness)
    segment_shape.color = pg.color.THECOLORS[color]
    segment_shape.elasticity = 0.8
    segment_shape.friction = 0.5
    space.add(segment_shape)

# borders
create_segment((0, HEIGHT), (WIDTH, HEIGHT), 10, space, 'grey')
create_segment((0, 0), (WIDTH, 0), 10, space, 'grey')
create_segment((0, 10), (0, HEIGHT-10), 10, space, 'grey')
create_segment((WIDTH, 0), (WIDTH, HEIGHT-10), 10, space, 'grey')

# create castle
for x in range(WIDTH-300, WIDTH-50, 40):
    for y in range(HEIGHT-300, HEIGHT-10, 60):
        create_box(space, (x,y))

x0, y0 = 0, 0
while True:
    surface.fill(pg.Color('black'))
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            x0, y0 = i.pos
            ball1 = Create_Ball(size=10, x=x0, y=x0, m=10, v=(0,0))
        pressed = pg.mouse.get_pressed()
        if pressed[0]:
            ball1.ball_body.position = i.pos
        if i.type == pg.MOUSEBUTTONUP:
            if i.button == 1:
                x1, y1 = i.pos
                ball1.ball_body.velocity_func = default_gravity
                ball1.ball_body.velocity = Vec2d(-(x1-x0)*5, -(y1-y0)*5)

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    pg.display.update()
    FramePerSec.tick(FPS)