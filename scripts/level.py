import pygame as pg
from settings import *
from player import Player
from overlay import Overlay
from sprites import Generic
from pygame.math import Vector2

class Level:
    def __init__(self):

        # get the display surface
        self.displaySurf = pg.display.get_surface()

        #sprite groups
        self.allSprites = CameraGroup()
        
        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        self.player = Player((640, 360), self.allSprites)
        Generic(
            pos = (0,0),
            surf = pg.image.load('../graphics/world/ground.png').convert_alpha(),
            groups = self.allSprites,
            z = LAYERS['ground']
        )

    def run(self, dt):
        self.displaySurf.fill('black')
        # self.allSprites.draw(self.displaySurf)
        self.allSprites.custom_draw(self.player)
        self.allSprites.update(dt)

        self.overlay.display()

class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurf = pg.display.get_surface()
        self.offset = Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layerIndex in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layerIndex:
                    offsetRect = sprite.rect.copy()
                    offsetRect.center -= self.offset
                    self.displaySurf.blit(sprite.image, offsetRect)