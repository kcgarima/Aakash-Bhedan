import sys
import pygame
from settings import Settings
from ship import Ship
def run_game():
    # Initialize game and creat a screen object.
    pygame.init()
    ab_settings = Settings()
    screen = pygame.display.set_mode(
        (ab_settings.screen_width, ab_settings.screen_height))
    pygame.display.set_caption("Aakash Bhedan")

    # Make a ship.
    ship = Ship(screen)

    # Set the background color.
    bg_color = (200, 90, 50)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard or mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(ab_settings.bg_color)
        ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()