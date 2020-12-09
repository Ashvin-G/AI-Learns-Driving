import pygame
import os

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("AI-Learns-Driving")
        win_width = 1000
        win_height = 600
        
        self.screen = pygame.display.set_mode((win_width, win_height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

    def run(self):
        while not self.exit:
            dt = self.clock.get_time() / 1000

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            
            pressed = pygame.key.get_pressed()

            
            self.screen.fill((0, 0, 0))
            pygame.display.flip()

            self.clock.tick(self.ticks)
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()

        
