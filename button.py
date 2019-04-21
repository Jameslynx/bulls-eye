import pygame.font


class Button():
    """A class to manage the play button."""

    def __init__(self, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = 0, 255, 0
        self.text_color = 255, 255, 255
        self.font = pygame.font.SysFont(None, 48)

        # create button and set pos.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """create rendered image of the msg and set pos."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw button on screen.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
