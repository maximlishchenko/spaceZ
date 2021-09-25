import pygame
import random
import math


BLACK = (0, 0, 0)


class Bitcoin(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        """Initialize the bitcoin."""
        # Object initialization inspired by practicals 6 & 9
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('media/bitcoin.png')
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self, settings, sprites):
        self.rect.centerx += 10


class Supercoin(Bitcoin):

    def __init__(self, screen, x, y):
        """Initialize the supercoin."""
        super().__init__(screen, x, y)  # Initialize same as regular bitcoin
        self.angle = random.randint(0, 359)  # add an angle attribute

    def update(self, settings, sprites):
        radian = self.angle * math.pi / 180
        self.rect.centerx += (10 * math.cos(radian))
        self.rect.centery += (10 * math.sin(radian))
