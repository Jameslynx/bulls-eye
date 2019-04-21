import pygame.font
from ship import Ship
from pygame.sprite import Group


class Scoreboard():
    """A class to manage the games dashboard."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scoreboard's attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.text_color = 30, 30, 30
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_bullets()
        self.prep_ship()

    def prep_score(self):
        """Render score image and position it."""
        rounded_score = int(round(self.stats.score, -1))
        score = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score, True, self.text_color, self.ai_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.top = self.screen_rect.top
        self.score_image_rect.right = self.screen_rect.right - 70

    def prep_highscore(self):
        """Render target image and position it."""
        rounded_highscore = int(round(self.stats.high_score, -1))
        highscore = "{:,}".format(rounded_highscore)
        self.highscore_image = self.font.render(highscore, True, self.text_color, self.ai_settings.bg_color)
        self.highscore_image_rect = self.highscore_image.get_rect()
        self.highscore_image_rect.top = self.screen_rect.top
        self.highscore_image_rect.centerx = self.screen_rect.centerx

    def prep_level(self):
        """Render level image and position it."""
        level = "{:,}".format(self.stats.level)
        self.level_image = self.font.render(('level ' + level), True, self.text_color, self.ai_settings.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.top = self.screen_rect.top
        self.level_image_rect.left = self.screen_rect.left + 20

    def prep_bullets(self):
        """Render bullets image and position it."""
        bullets = "{:,}".format(self.stats.bullets_left)
        self.bullets_image = self.font.render(('bullets ' + bullets), True, self.text_color, self.ai_settings.bg_color)
        self.bullets_image_rect = self.bullets_image.get_rect()
        self.bullets_image_rect.top = self.screen_rect.top
        self.bullets_image_rect.left = self.screen_rect.left + 170

    def prep_ship(self):
        """Create ships to display."""
        self.ships = Group()
        for ship_num in range(self.stats.ships):
            new_ship = Ship(self.ai_settings, self.screen)
            new_ship.rect.top = self.screen_rect.top
            new_ship.rect.x = 750 + new_ship.rect.width * ship_num
            self.ships.add(new_ship)

    def show_score(self):
        """Draw score to screen."""
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.highscore_image, self.highscore_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.screen.blit(self.bullets_image, self.bullets_image_rect)
        self.ships.draw(self.screen)
