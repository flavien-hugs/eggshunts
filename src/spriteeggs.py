# src/spriteeggs.py

import random
import pygame


class SpriteEggs(pygame.sprite.Sprite):
    """docstring for SpriteEggs"""
    def __init__(self, screen_weight, screen_height, spritecart):
        super(SpriteEggs, self).__init__()
        self.spritecart = spritecart
        self.spritecart_group = pygame.sprite.Group()
        self.spritecart_group.add(self.spritecart)

        self.screen_weight = screen_weight
        self.screen_height = screen_height

        self.image = pygame.image.load("assets/eggs.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30, screen_weight - 30)

        self.velocity = random.randint(1, 4)

    def eggs_destroy(self):
        self.rect.x = random.randint(30, self.screen_weight - 30)
        self.rect.y = 0 - self.image.get_height()
        self.velocity = random.randint(1, 4)

    def down_gravity_eggs(self):
        self.rect.y += self.velocity

        if pygame.sprite.spritecollide(self, self.spritecart_group, False, pygame.sprite.collide_mask) and self.rect.y >= 350:
            # print("coordonnée collision: {}".format(self.rect.y))
            self.eggs_destroy()
            self.spritecart.add_health()

        if self.rect.y >= self.screen_height:
            self.eggs_destroy()
            self.spritecart.remove_health()
