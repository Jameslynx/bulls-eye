import json


class GameStats():
    """A class to manage game statistics."""

    def __init__(self, ai_settings, filename):
        """Intiate game attributes."""
        self.game_active = False
        self.ai_settings = ai_settings
        with open(filename) as f_obj:
            self.high_score = json.load(f_obj)

        self.reset_stats()

    def reset_stats(self):
        self.bullets_left = self.ai_settings.magazine
        self.score = 0
        self.ships = 3
        self.level = 1
