import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage ship."""

    def __init__(self, ai_game):
        """Initializes ship and starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for ship's horizontal position.
        self.x = float(self.rect.x)

        # Ship Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates ship's position depending on movement."""
        # Increase the movement of the ship one pixel to the right.
        # Set boundaries for the ship while keeping movement in place.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        # Decrease the movement one pixel to the left.
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        # Update rect object from self.x.

    def blitme(self):
        """Draw ship at current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centers ship on screens."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
