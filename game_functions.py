import sys
import json
import pygame
from bullet import Bullet
from target import Target
from time import sleep


def check_events(ship, bullets, ai_settings, screen, stats, button, targets, sb):
    """Check key presses and releases."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, bullets, screen, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y, button, stats, ship, targets, bullets, ai_settings, screen, sb)


def check_play_button(mouse_x, mouse_y, button, stats, ship, targets, bullets, ai_settings, screen, sb):
    # check if play button has been clicked on.
    mouse_button = button.rect.collidepoint(mouse_x, mouse_y)
    if mouse_button and not stats.game_active:
        start_game(bullets, targets, ai_settings, stats, ship, screen, sb)


def start_game(bullets, targets, ai_settings, stats, ship, screen, sb):
    """Start game."""
    # make mouse invisible
    pygame.mouse.set_visible(False)
    sb.prep_score()
    sb.prep_highscore()
    sb.prep_level()
    sb.prep_bullets()
    stats.game_active = True
    # reset game.
    stats.reset_stats()
    sb.prep_ship()
    ai_settings.initialize_dynamic_settings()
    # empty bullets and targets.
    bullets.empty()
    targets.empty()
    create_target(targets, ai_settings, screen)
    ship.center()
    stats.bullets_left = ai_settings.magazine


def check_keydown_events(event, ship, ai_settings, bullets, screen, stats):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # create a new bullet and add it to bullets if bullets are less then 3.
        if len(bullets) < ai_settings.bullet_limit:
            new_bullet = Bullet(ai_settings, ship, screen)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def create_target(targets, ai_settings, screen):
    # create target.
    new_target = Target(ai_settings, screen)
    targets.add(new_target)


def check_ships(stats):
    """Check trials."""
    if stats.ships < 0:
        stats.game_active = False
        # make mouse visible
        pygame.mouse.set_visible(True)


def update_screen(ai_settings, screen, ship, bullets, targets, button, stats, sb):
    """Update screen."""
    check_ships(stats)
    screen.fill(ai_settings.bg_color)
    sb.show_score()
    # draw button if game over.
    if not stats.game_active:
        button.draw_button()

    # draw bullet
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # draw target
    for target in targets.sprites():
        target.draw_target()

    ship.blitme()
    pygame.display.flip()


def out_of_bullets(bullets, targets, ai_settings, stats, ship, screen, sb):
    stats.ships -= 1
    sb.prep_ship()
    ai_settings.initialize_dynamic_settings()
    # empty bullets and targets.
    bullets.empty()
    targets.empty()
    create_target(targets, ai_settings, screen)
    ship.center()
    stats.bullets_left = ai_settings.magazine
    sleep(0.5)


def bullet_edge(bullets, stats, sb):
    """Delete bullets that hit the edge."""
    for bullet in bullets.copy():
        if bullet.rect.right <= 0:
            bullets.remove(bullet)
            stats.bullets_left -= 1
            sb.prep_bullets()


def update_bullet(bullets, targets, ai_settings, screen, stats, ship, sb, filename):
    # update position of bullet and delete bullets that hit edge.
    bullets.update()
    bullet_edge(bullets, stats, sb)
    check_collisions(bullets, targets, ai_settings, screen, stats, sb, filename)

    # restart game if bullets are finished.
    if stats.bullets_left <= 0:
        out_of_bullets(bullets, targets, ai_settings, stats, ship, screen, sb)


def check_edge(targets):
    for target in targets.sprites():
        if target.rect.bottom >= target.screen_rect.bottom:
            target.edge_hit = True
        elif target.rect.top <= 0:
            target.edge_hit = True
        else:
            target.edge_hit = False


def check_target_edges(targets, ai_settings):
    check_edge(targets)
    for target in targets.sprites():
        if target.edge_hit:
            ai_settings.target_direction *= -1
            break


def update_target(targets, ai_settings):
    # update position of targets
    check_target_edges(targets, ai_settings)
    targets.update()


def check_collisions(bullets, targets, ai_settings, screen, stats, sb, filename):
    collisions = pygame.sprite.groupcollide(bullets, targets, True, True)
    if len(targets) == 0:
        stats.score += ai_settings.target_score
        stats.level += 1
        sb.prep_score()
        sb.prep_level()
        check_high_score(stats, filename, sb)
        ai_settings.increase_speed()
        create_target(targets, ai_settings, screen)
    if collisions:
        stats.bullets_left += 3
        sb.prep_bullets()


def check_high_score(stats, filename, sb):
    """Update high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score

        with open(filename, 'w') as f_obj:
            json.dump(stats.high_score, f_obj)
        sb.prep_highscore()
