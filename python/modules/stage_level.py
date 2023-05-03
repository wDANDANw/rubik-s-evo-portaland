import pyxel
from typing import List
from abc import ABC, abstractmethod
from modules.base_level import BaseLevel
from modules.globals import *

STAGE_LEVEL_WIDTH_TILES = 16
STAGE_LEVEL_HEIGHT_TILES = 16
STAGE_LEVEL_ONE_TILE_WIDTH = 8
STAGE_LEVEL_ONE_TILE_HEIGHT = 8

STAGE_LEVEL_PIXEL_WIDTH = STAGE_LEVEL_WIDTH_TILES * STAGE_LEVEL_ONE_TILE_WIDTH
STAGE_LEVEL_PIXEL_HEIGHT = STAGE_LEVEL_HEIGHT_TILES * STAGE_LEVEL_ONE_TILE_HEIGHT


class StageObject(ABC):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.visible = True

    def get_hitbox(self):
        return (self.x, self.y, self.width, self.height)

    @abstractmethod
    def on_collision(self, other: "StageObject"):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class StageLevel(BaseLevel):
    def __init__(self, level_no, level_data, tm=0, tmu=0, tmv=0):
        super().__init__(level_no, level_data)

        self.tm = tm
        self.tmu = tmu
        self.tmv = tmv

        self.player = None
        self.objects: List[StageObject] = []

    def add_object(self, obj: StageObject):
        self.objects.append(obj)

    def set_player(self, player: StageObject):
        self.player = player

    def render_stage(self):
        # Render the background of stage
        upper_left_x = (SCREEN_WIDTH - STAGE_LEVEL_PIXEL_WIDTH) / 2
        upper_left_y = (SCREEN_HEIGHT - STAGE_LEVEL_PIXEL_HEIGHT) / 2

        transparent_color = 0

        # bltm(x, y, tm, u, v, w, h, [colkey])
        pyxel.bltm(upper_left_x, upper_left_y, 
                   self.tm, self.tmu, self.tmv,
                   STAGE_LEVEL_PIXEL_WIDTH, STAGE_LEVEL_PIXEL_HEIGHT, 
                   transparent_color)
        
    def detect_collisions(self):
        all_objects = self.objects.copy()

        if self.player:
            all_objects.append(self.player)

        for i, obj1 in enumerate(all_objects[:-1]):
            if not obj1.visible:
                continue

            obj1_hitbox = obj1.get_hitbox()

            for obj2 in all_objects[i+1:]:
                if not obj2.visible:
                    continue

                obj2_hitbox = obj2.get_hitbox()

                if self.check_collision(obj1_hitbox, obj2_hitbox):
                    obj1.on_collision(obj2)
                    obj2.on_collision(obj1)

    def check_collision(self, a, b):
        ax, ay, aw, ah = a
        bx, by, bw, bh = b

        return (ax < bx + bw) and (ax + aw > bx) and (ay < by + bh) and (ay + ah > by)

    def update(self):
        
        # Update the player
        if self.player:
            self.player.update()

        # Update the objects
        for obj in self.objects:
            obj.update()

        # Detect collisions
        self.detect_collisions()

    def draw(self):
        self.render_stage()

        # Draw player
        if self.player:
            self.player.draw()

        # Draw objects
        for obj in self.objects:
            if obj.visible:
                obj.draw()