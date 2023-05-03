import pyxel
from enum import Enum, auto

from modules.globals import *

class Component:
    pass

class PositionComponent(Component):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_position(self, x, y):
        self.x = x
        self.y = y

class VelocityComponent(Component):
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

class CollisionEvent:
    def __init__(self, obj1, obj2, x, y):
        self.obj1 = obj1
        self.obj2 = obj2
        self.x = x
        self.y = y

class HitboxComponent(Component):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class RenderableComponent(Component):
    def __init__(self, img_bank_no, u, v, w, h, colkey=0, visible=True):
        self.img_bank_no = img_bank_no
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.colkey = colkey

        self.visible = visible

        self.offset_x = 0
        self.offset_y = 0

    def draw(self, obj, dx=0, dy=0):
        """
        obj is the object
        dx = global offset x, dy = global offset y
        self.offset_x = local offset x, self.offset_y = local offset y (of the object)
        """

        if self.visible:

            if hasattr(obj, 'position_component'):

                pos_x = obj.position_component.x
                pos_y = obj.position_component.y

                real_x = STAGE_UPPER_LEFT_X + pos_x * STAGE_LEVEL_ONE_TILE_WIDTH + dx + self.offset_x
                real_y = STAGE_UPPER_LEFT_Y + pos_y * STAGE_LEVEL_ONE_TILE_HEIGHT + dy + self.offset_y

                if hasattr(obj, 'animation_component'):
                    obj.animation_component.draw(real_x, real_y, self.colkey)
                    return

                pyxel.blt(
                    real_x, real_y,
                    self.img_bank_no, 
                    self.u, self.v, 
                    self.w, self.h, 
                    self.colkey)
            else:
                raise Exception(f'Renderable Component {obj.__name__} has no position component')
        
    def add_offset(self, dx, dy):
        self.offset_x += dx
        self.offset_y += dy

        tile_offset_x = 0
        tile_offset_y = 0
        if self.offset_x > STAGE_LEVEL_ONE_TILE_WIDTH:
            self.offset_x -= STAGE_LEVEL_ONE_TILE_WIDTH
            tile_offset_x = 1

        if self.offset_y > STAGE_LEVEL_ONE_TILE_HEIGHT:
            self.offset_y -= STAGE_LEVEL_ONE_TILE_HEIGHT
            tile_offset_y = 1

        return tile_offset_x, tile_offset_y
    
    def set_offset(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y
    
    def clear_offset(self):
        self.offset_x = 0
        self.offset_y = 0
        
class AnimationComponent(Component):
    def __init__(self, img_bank_no, start_u, start_v, w, h, frames, auto_update=True):
        self.tick = 0
        self.frames = frames

        self.img_bank_no = img_bank_no
        self.start_u = start_u
        self.start_v = start_v
        self.w = w
        self.h = h

        self.auto_update = auto_update

    def draw(self, x, y, transparent_color):
        pyxel.blt(
            x, y,
            self.img_bank_no, 
            self.start_u + STAGE_LEVEL_ONE_TILE_WIDTH * self.tick, self.start_v, 
            self.w, self.h, 
            transparent_color)
        
        if self.auto_update:
            self.update_one_tick()

    def update_one_tick(self, direction=1):
        self.tick = (self.tick + direction) % self.frames


class Inputs(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class InputComponent(Component):

    def __init__(self, *callables):
        self.callables = callables

    def handle_inputs(self, pressing, pressed, released):
        for callable in self.callables:
            callable(pressing, pressed, released)

class AutoUpdateComponent(Component):
    pass