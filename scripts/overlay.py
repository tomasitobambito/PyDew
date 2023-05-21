import pygame as pg
from settings import *

class Overlay():
    def __init__(self, player):

        # general setup
        self.displaySurf = pg.display.get_surface()
        self.player = player

        # import
        overlayPath = '../graphics/overlay/'
        self.toolsSurf = {tool: pg.image.load(f'{overlayPath}{tool}.png').convert_alpha() for tool in player.tools}
        self.seedsSurf = {seed: pg.image.load(f'{overlayPath}{seed}.png').convert_alpha() for seed in player.seeds}

    def display(self):

        # tool
        toolSurf = self.toolsSurf[self.player.selectedTool]
        toolRect = toolSurf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
        self.displaySurf.blit(toolSurf, toolRect)

        # seeds
        seedSurf = self.seedsSurf[self.player.selectedSeed]
        seedRect = seedSurf.get_rect(midbottom = OVERLAY_POSITIONS['seed'])
        self.displaySurf.blit(seedSurf, seedRect)