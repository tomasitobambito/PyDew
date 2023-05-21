import pygame as pg
import sys, time
from settings import *
from level import Level

class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("PyDew")
        self.clock = pg.time.Clock()

        self.level = Level()

    def run(self):
        prevTime = time.time()

        while True:
            dt = time.time() - prevTime
            prevTime = time.time()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.level.run(dt)

            pg.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
