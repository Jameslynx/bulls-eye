import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage ship image."""

    def __init__(self, ai_settings, screen):
        """Initiate ship attributes."""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # Load image.
        self.image = pygame.image.load("images/ship2.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set position.
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        # store ship's y-coordinate as a decimal.
        self.y = float(self.rect.centery)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.ai_settings.ship_speed_factor

        self.rect.centery = self.y

    def center(self):
        # center ship.
        self.y = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
