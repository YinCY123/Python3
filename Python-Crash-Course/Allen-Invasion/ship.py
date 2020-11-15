import pygame


class Ship():

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get its rect.
        self.image = pygame.image.load('image/ship.bmp')
        self.ship_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # start each new ship at the bottom center of the screen.
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom


    def update(self):
        """update the ship's position based on the movement flag."""
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.ship_rect.centerx += 1
        else:
            self.ship_rect.centerx += 0

        if self.moving_left and self.ship_rect.left > 0:
            self.ship_rect.centerx -= 1
        else:
            self.ship_rect.centerx -= 0

        if self.moving_up and self.ship_rect.top > 0:
            self.ship_rect.centery -= 1
        else:
            self.ship_rect.centery -= 0

        if self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_rect.centery += 1
        else:
            self.ship_rect.centery += 0

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.ship_rect)

"""
In Pygame, the origin (0,0) is at the top-left corner of the screen, and 
coordinates increase as you go down and to the right.
"""