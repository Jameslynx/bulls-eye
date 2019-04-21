import pygame
from settings import Settings
import game_functions as gf
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    """ This is the main game function."""
    # Initiate pygame, create a screen and caption/title.
    filename = "Highscore.json"

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Bull's eye")

    # create an instance of ship.
    ship = Ship(ai_settings, screen)

    # create groups of bullets.
    bullets = Group()
    targets = Group()

    # create target.
    gf.create_target(targets, ai_settings, screen)

    # Instantiate statistics, play button and scoreboard.
    stats = GameStats(ai_settings, filename)
    button = Button(screen, 'Play')
    sb = Scoreboard(ai_settings, screen, stats)

    while True:
        """Main loop/runs the game and updates everything."""
        gf.check_events(ship, bullets, ai_settings, screen, stats, button, targets, sb)
        if stats.game_active:
            gf.update_bullet(bullets, targets, ai_settings, screen, stats, ship, sb, filename)
            gf.update_target(targets, ai_settings)
            ship.update()
        gf.update_screen(ai_settings, screen, ship, bullets, targets, button, stats, sb)


run_game()
