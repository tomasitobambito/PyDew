import pygame as pg
from settings import *

class Level:
    def __init__(self):

        # get the display surface
        self.displaySurf = pg.display.get_surface()

        #sprite groups
        self.allSprites = pg.sprite.Group()

    def run(self, dt):
        self.displaySurf.fill('black')
        self.allSprites.draw(self.displaySurf)
        self.allSprites.update()