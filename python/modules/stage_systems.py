from __future__ import annotations

import pyxel
from typing import TYPE_CHECKING

from modules.stage_components import *
from modules.globals import *
from modules.utils import * 

import random

if TYPE_CHECKING:
    from modules.stage_level import StageLevel

class System:
    def __init__(self, stage: StageLevel):
        self.stage = stage

    def update(self):
        pass

class AutoUpdateSystem(System):
    def update(self):
        all_objects = self.stage.objects.copy()

        if self.stage.player:
            all_objects.append(self.stage.player)

        for obj in all_objects:
            if hasattr(obj, 'auto_update_component'):
                obj.update()

class MovementSystem(System):
    def update(self):

        all_objects = self.stage.objects.copy()

        if self.stage.player:
            all_objects.append(self.stage.player)

        for obj in all_objects:
            if hasattr(obj, 'position_component') and hasattr(obj, 'velocity_component'):
                obj.position_component.x += obj.velocity_component.dx
                obj.position_component.y += obj.velocity_component.dy

class CollisionSystem(System):
    def update(self):
        all_objects = self.stage.objects.copy()

        if self.stage.player:
            all_objects.append(self.stage.player)

        for i, obj1 in enumerate(all_objects):
            if not hasattr(obj1, 'hitbox_component'):
                continue

            obj1_hitbox = (obj1.position_component.x, obj1.position_component.y, obj1.hitbox_component.width, obj1.hitbox_component.height)

            if get_tile(obj1.position_component.x, obj1.position_component.y) == WALL_TILE:
                obj1.handle_collision(self.stage.wall_object)
                continue

            for obj2 in all_objects[i+1:]:
                if not hasattr(obj2, 'hitbox_component'):
                    continue

                obj2_hitbox = (obj2.position_component.x, obj2.position_component.y, obj2.hitbox_component.width, obj2.hitbox_component.height)

                if self.check_collision(obj1_hitbox, obj2_hitbox):
                    if hasattr(obj1, 'handle_collision'):
                        obj1.handle_collision(obj2)
                    if hasattr(obj2, 'handle_collision'):
                        obj2.handle_collision(obj1)

    def check_collision(self, a, b):
        ax, ay, aw, ah = a
        bx, by, bw, bh = b

        return (ax < bx + bw) and (ax + aw > bx) and (ay < by + bh) and (ay + ah > by)
    

class RenderSystem(System):

    def __init__(self, stage: StageLevel):
        super().__init__(stage)

        self.offset_x = 0
        self.offset_y = 0

    def update(self):

        # Render background / the static stage
        self.stage.render_stage(self.offset_x, self.offset_y)

        # Dynamic renders of objects
        if self.stage.player:
            if hasattr(self.stage.player, 'renderable_component'):
              self.stage.player.renderable_component.draw(self.stage.player, self.offset_x, self.offset_y)

        for obj in self.stage.objects:
            if hasattr(obj, 'renderable_component'):
               obj.renderable_component.draw(obj, self.offset_x, self.offset_y)

    def set_offsets(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y

    # def render_stage(self, offset_x=0, offset_y=0):
    #     # Render the background of stage

    #     # bltm(x, y, tm, u, v, w, h, [colkey])
    #     pyxel.bltm(STAGE_UPPER_LEFT_X + offset_x, STAGE_UPPER_LEFT_Y + offset_y, 
    #                self.stage.tm, self.stage.tmu, self.stage.tmv,
    #                STAGE_LEVEL_PIXEL_WIDTH, STAGE_LEVEL_PIXEL_HEIGHT, 
    #                STAGE_TRANSPARENT_COLOR)

class InputSystem(System):
    def __init__(self, stage: StageLevel):
        
        super().__init__(stage)

        self.pressing = []
        self.pressed = []
        self.released = []

    def _get_inputs(self):
        self.pressing.clear()
        self.pressed.clear()
        self.released.clear()

        # Pressing
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            self.pressing.append(Inputs.LEFT)
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.pressing.append(Inputs.RIGHT)

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            self.pressing.append(Inputs.UP)
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            self.pressing.append(Inputs.DOWN)

        # Pressed
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_A):
            self.pressed.append(Inputs.LEFT)
        elif pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_D):
            self.pressed.append(Inputs.RIGHT)

        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_W):
            self.pressed.append(Inputs.UP)
        elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self.pressed.append(Inputs.DOWN)

        # Released
        if pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnr(pyxel.KEY_A):
            self.released.append(Inputs.LEFT)
        elif pyxel.btnr(pyxel.KEY_RIGHT) or pyxel.btnr(pyxel.KEY_D):
            self.released.append(Inputs.RIGHT)

        if pyxel.btnr(pyxel.KEY_UP) or pyxel.btnr(pyxel.KEY_W):
            self.released.append(Inputs.UP)
        elif pyxel.btnr(pyxel.KEY_DOWN) or pyxel.btnr(pyxel.KEY_S):
            self.released.append(Inputs.DOWN)
    
    def update(self):
        self._get_inputs()
        
        if self.stage.player:
            if hasattr(self.stage.player, 'input_component'):
                self.stage.player.input_component.handle_inputs(self.pressing, self.pressed, self.released)

        for obj in self.stage.objects:
            if hasattr(obj, 'input_component'):
                obj.input_component.handle_inputs(self.pressing, self.pressed, self.released)

class ShakeScreenSystem(System):

    def __init__(self, stage):                
        super().__init__(stage)

        self.shaking = False
        self.shake_tick = 0
        self.shake_frames = 7

    def update(self):
        if self.shaking:

            self.shake_tick += 1
            
            shake_x = random.randint(-SCREEN_SHAKE_MAGNITUDE, SCREEN_SHAKE_MAGNITUDE)
            shake_y = random.randint(-SCREEN_SHAKE_MAGNITUDE, SCREEN_SHAKE_MAGNITUDE)

            if self.shake_tick >= self.shake_frames:
                self.shaking = False
                self.shake_tick = 0
                shake_x = 0
                shake_y = 0
                
            self.stage.render_system.set_offsets(shake_x, shake_y)

    def shake(self):
        if not self.shaking:
            self.shaking = True


