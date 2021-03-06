import pygame
from colours import *
# from characteristics import *
from ai import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type, cor_x, cor_y):
        pygame.sprite.Sprite.__init__(self)
        self.type = enemy_type
        self.stats = enemy_stat[self.type]
        self.w, self.h = self.stats["w"], self.stats["h"]
        self.image = pygame.Surface((self.w, self.h))
        self.color = RED
        self.image.fill(self.color)
        self.speed = self.stats["speed"]
        self.rect = self.image.get_rect()
        self.rect.centerx = cor_x
        self.rect.centery = cor_y
        self.fractional_x = cor_x
        self.fractional_y = cor_y

    def update(self):
        from main import player_sprite
        x_change, y_change = move_calculate(self.type, player_sprite.rect.centerx, player_sprite.rect.centery,
                                            self.rect.centerx, self.rect.centery)
        self.fractional_x += x_change
        self.fractional_y += y_change
        if self.fractional_y <= 0:
            self.fractional_y = 1
        if self.fractional_y >= H:
            self.fractional_y = H - 1
        if self.fractional_x <= 0:
            self.fractional_x = 1
        if self.fractional_x >= W:
            self.fractional_x = W - 1
        self.rect.centerx = ceil(self.fractional_x)
        self.rect.centery = ceil(self.fractional_y)
