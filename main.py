import pygame
import sys
from settings import *
from level import Level


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
        pygame.display.set_caption("Wenou Valley")
        Icon = pygame.image.load("wenou-valley.png")
        pygame.display.set_icon(Icon)
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000

            self.level.run(dt)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
