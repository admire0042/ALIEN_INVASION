import sys
import pygame

from settings import Settings 
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #self.bg_color = (230, 230, 230)
        #self.bg_color = (255, 0, 0)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # watch for keyword mouse events.
            self._check_event()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)



    def _check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #We will move the ship to the right
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                         self.ship.moving_left = True
                    elif event.key == pygame.K_UP:
                         self.ship.moving_up = True
                    elif event.key == pygame.K_DOWN:
                         self.ship.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                         self.ship.moving_left = False
                    elif event.key == pygame.K_UP:
                         self.ship.moving_up = False
                    elif event.key == pygame.K_DOWN:
                         self.ship.moving_down = False

    def _update_screen(self):
        #Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # make the most recently drawn on screen visible
            pygame.display.flip()



if __name__ == "__main__":
    #make a game instance, and run the game  
    ai = AlienInvasion()
    ai.run_game()      

