import pygame
from bitcoin import Bitcoin, Supercoin

BLACK = (0, 0, 0)


class Ship(pygame.sprite.Sprite):

    def __init__(self, screen, settings):
        """Initialize the starship."""
        # Object initialization is inspired by practicals 6 & 9
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('media/starship.png')
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = 200  # start at 200 pixels from left edge
        self.rect.centery = settings.screen_height / 2
        self.damage = 0
        self.mining = 0
        self.bitcoin = None

    def right(self):
        """Move starship 5 pixels to the right."""
        if self.rect.right < 1200:
            self.rect.centerx += 5

    def left(self):
        """Move starship 5 pixels to the left."""
        if self.rect.left > 0:
            self.rect.centerx -= 5

    def up(self):
        """Move starship 5 pixels up."""
        if self.rect.top > 0:
            self.rect.centery -= 5

    def down(self):
        """Move starship 5 pixels down."""
        if self.rect.bottom < 750:
            self.rect.centery += 5

    def launch_bitcoin(self, screen, sprites):
        if self.mining == 100:  # can only shoot when mining is 100%
            self.bitcoin = Bitcoin(screen, self.rect.centerx, self.rect.centery)
            # note that bitcoin is passed the x and y coordinates
            # of the ship as arguments
            sprites.add(self.bitcoin)
            self.mining = 0

    def launch_supercoin(self, screen, sprites):
        if self.mining == 100:  # can only shoot when mining is 100%
            self.bitcoin = Supercoin(screen, self.rect.centerx, self.rect.centery)
            # note that bitcoin is passed the x and y coordinates
            # of the ship as arguments
            sprites.add(self.bitcoin)
            self.mining = 0

    def update(self, settings, sprites):
        """Check whether the bitcoin has reached the screen boundaries."""
        if self.bitcoin is not None:
            if (self.bitcoin.rect.left >= settings.screen_width or self.bitcoin.rect.right <= 0 or
                    self.bitcoin.rect.top >= settings.screen_height or self.bitcoin.rect.bottom <= 0):
                self.bitcoin.kill()
                self.bitcoin = None
