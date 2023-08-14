import pygame, math
from MY_CONSTANTS import SCREEN_WIDTH, SCREEN_HEIGHT, RED

class Create_Circle(pygame.sprite.Sprite):
    def __init__(self, size, x, y, m, v, angle):
        super().__init__()
        self.size = size
        self.x = x
        self.y = y
        self.mass = m
        self.v = v
        self.angle = math.radians(angle)
        self.radius = size // 2
        self.clr = RED

        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, self.clr, [0, 0, size, size])
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self):
        if self.v > 0:
            # accel=-NU_CONST*G_CONST
            # dt = pygame.time.get_ticks()/1000
            # self.v = self.v+accel*dt

            dx = round(math.cos(self.angle)*self.v)
            dy = round(math.sin(self.angle)*self.v)

            if self.rect.right + dx > SCREEN_WIDTH:
                self.angle = math.pi - self.angle
                before_border = SCREEN_WIDTH - self.rect.right
                after_border = self.rect.right + dx - SCREEN_WIDTH
                dx = -(after_border - before_border) if after_border != before_border else before_border
            if self.rect.left + dx < 0:
                self.angle = math.pi - self.angle
                before_border = self.rect.left
                after_border = self.rect.left + dx
                dx = -(after_border + before_border) if after_border != before_border else before_border
            if self.rect.bottom + dy > SCREEN_HEIGHT:
                self.angle = 2 * math.pi - self.angle
                before_border = SCREEN_HEIGHT - self.rect.bottom
                after_border = self.rect.bottom + dy - SCREEN_HEIGHT
                dy = -(after_border - before_border) if after_border != before_border else before_border
            if self.rect.top + dy < 0:
                self.angle = 2 * math.pi - self.angle
                before_border = self.rect.top
                after_border = self.rect.top + dy
                dy = -(after_border + before_border) if after_border != before_border else before_border

            self.rect.move_ip(dx, dy)
            self.x += dx
            self.y += dy
