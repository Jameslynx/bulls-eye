import pygame
from pygame.sprite import Sprite


class Target(Sprite):
    """A class to manage individual targets."""

    def __init__(self, ai_settings, screen):
        super().__init__()
        # Initiate target attributes.
        self.ai_settings = ai_settings
        self.screen = screen
        self.speed = ai_settings.target_speed_factor
        self.color = ai_settings.target_color

        # create target and set intial pos to (0, 0).
        self.rect = pygame.Rect(0, 0, ai_settings.target_width, ai_settings.target_height)
        self.screen_rect = screen.get_rect()

        # set position.
        self.rect.top = self.rect.height
        self.rect.left = self.screen_rect.left

        # store y-coordinates as a decimal.
        self.y = self.rect.centery

        # hit_edge flaf.
        self.edge_hit = False

    def update(self):
        # update self.y.
        self.y += (self.speed * self.ai_settings.target_direction)
        # update self.rect.centery.
        self.rect.centery = self.y

    def draw_target(self):
        # Draw target on screen.
        pygame.draw.rect(self.screen, self.color, self.rect)
