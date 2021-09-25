import pygame
import random


BLACK = (0, 0, 0)


class Roadster(pygame.sprite.Sprite):

    def __init__(self, screen, settings):
        """Initialize the roadster."""
        # Object initialization is inspired by practicals 6 & 9
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('media/roadster.png')
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = settings.screen_width
        self.rect.centery = random.randint(0, settings.screen_height)
        self.speed = random.randint(5, 10)

    def update(self, settings, sprites):
        # if roadster hasn't reached the left edge
        # move to the left by speed amount
        if self.rect.right > 0:
            self.rect.centerx -= self.speed
        # else destroy and replace
        else:
            self.kill()
            roadster = Roadster(self.screen, settings)
            sprites.add(roadster)
