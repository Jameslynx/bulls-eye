import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage individual bullets."""

    def __init__(self, ai_settings, ship, screen):
        super().__init__()
        # Initiate bullet attributes.
        self.ai_settings = ai_settings
        self.ship = ship
        self.screen = screen
        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed_factor

        # create bullet and let it's pos be (0, 0).
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        # set pos.
        self.rect.center = ship.rect.center
        self.rect.left = ship.rect.left

        # stores x-coordinate as a decimal.
        self.x = self.rect.centerx

    def update(self):
        # update self.x
        self.x -= self.speed

        # update self.rect.centerx
        self.rect.centerx = self.x

    def draw_bullet(self):
        """Draw bullet to screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
