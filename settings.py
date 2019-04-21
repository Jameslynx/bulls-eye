import random


class Settings():
    """A class to manage all our game's attribute's settings"""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = 230, 230, 230

        # bullet settings.
        self.magazine = 10
        self.bullet_limit = 3
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60

        # Target settings.
        self.target_width = 10
        self.target_height = 50
        self.target_color = 100, 60, 60
        self.target_speed_factor = 0.5
        self.target_direction = random.choice([1.0, 1.2, 1.5])

        # How quickly the game speeds up.
        self.speedup_scale = 1.009

        self.score_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.bullet_speed_factor = 5
        self.ship_speed_factor = 1.5
        self.target_speed_factor = 0.5
        self.target_score = 20

    def increase_speed(self):
        self.bullet_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.target_speed_factor *= self.speedup_scale
        self.target_score *= self.score_scale
