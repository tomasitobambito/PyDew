import pygame as pg
from pygame import Vector2
from settings import *
from support import *
from timer import Timer

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()
        self.status = 'down'
        self.frameIndex = 0

        # general setup
        self.image = self.animations[self.status][self.frameIndex]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']

        # movement attributes
        self.direction = Vector2()
        self.pos = Vector2(self.rect.center)
        self.speed = 250

        # timers
        self.timers = {
            'tool use': Timer(350, self.use_tool),
            'tool switch': Timer(200),
            'seed use': Timer(350, self.use_tool),
            'seed switch': Timer(200)
        }

        # tools
        self.tools = ['hoe', 'axe', 'water']
        self.toolIndex = 0
        self.selectedTool = self.tools[self.toolIndex]

        # seeds
        self.seeds = ['corn', 'tomato']
        self.seedIndex = 0
        self.selectedSeed = self.seeds[self.seedIndex]

    def use_tool(self):
        pass

    def use_seed(self):
        pass

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
        'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [], 
        'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
        'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
        'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []}

        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frameIndex += 4 * dt
        if self.frameIndex >= len(self.animations[self.status]):
            self.frameIndex = 0
        self.image = self.animations[self.status][int(self.frameIndex)]

    def input(self):
        keys = pg.key.get_pressed()

        if not self.timers['tool use'].active:
            # movement
            if keys[pg.K_UP] or keys[pg.K_w]:
                self.status = 'up'
                self.direction.y = -1
            elif keys[pg.K_DOWN] or keys[pg.K_s]:
                self.status = 'down'
                self.direction.y = 1
            else:
                self.direction.y = 0
            
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.status = 'left'
                self.direction.x = -1
            elif keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.status = 'right'
                self.direction.x = 1
            else:
                self.direction.x = 0

            # tool use
            if keys[pg.K_SPACE]:
                self.timers['tool use'].activate()
                self.direction = Vector2()
                self.frameIndex = 0

            # change tool
            if keys[pg.K_q] and not self.timers['tool switch'].active:
                self.timers['tool switch'].activate()
                self.toolIndex += 1
                self.toolIndex = self.toolIndex if self.toolIndex != len(self.tools) else 0
                self.selectedTool = self.tools[self.toolIndex]

            # seed use
            if keys[pg.K_LCTRL]:
                self.timers['seed use'].activate()
                self.direction = Vector2()

            # change seed
            if keys[pg.K_e] and not self.timers['seed switch'].active:
                self.timers['seed switch'].activate()
                self.seedIndex += 1
                self.seedIndex = self.seedIndex if self.seedIndex != len(self.seeds) else 0
                self.selectedSeed = self.seeds[self.seedIndex]

    def get_status(self):
        # idle
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

        # tool use
        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + "_" + self.selectedTool

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def move(self, dt):
        if self.direction.length() == 0:
            return
        self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()

        self.move(dt)
        self.animate(dt)