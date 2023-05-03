import pyxel

from stage_components import *
from stage_level import StageLevel

class System:
    def __init__(self, stage: StageLevel):
        self.stage = stage

    def update(self):
        pass

class MovementSystem(System):
    def update(self):
        for obj in self.stage.objects:
            if hasattr(obj, 'position_component') and hasattr(obj, 'velocity_component'):
                obj.position_component.x += obj.velocity_component.dx
                obj.position_component.y += obj.velocity_component.dy

class CollisionSystem(System):
    def update(self):
        all_objects = self.stage.objects.copy()

        if self.stage.player:
            all_objects.append(self.stage.player)

        for i, obj1 in enumerate(all_objects[:-1]):
            if not hasattr(obj1, 'hitbox_component'):
                continue

            obj1_hitbox = (obj1.position_component.x, obj1.position_component.y, obj1.hitbox_component.width, obj1.hitbox_component.height)

            for obj2 in all_objects[i+1:]:
                if not hasattr(obj2, 'hitbox_component'):
                    continue

                obj2_hitbox = (obj2.position_component.x, obj2.position_component.y, obj2.hitbox_component.width, obj2.hitbox_component.height)

                if self.stage.check_collision(obj1_hitbox, obj2_hitbox):
                    if hasattr(obj1, 'on_collision'):
                        obj1.on_collision(obj2)
                    if hasattr(obj2, 'on_collision'):
                        obj2.on_collision(obj1)

class InputControlSystem(System):
    def update(self):
        for obj in self.stage.objects:
            if hasattr(obj, 'input_control_component'):
                obj.handle_input()

class RenderSystem(System):
    def update(self):
        for obj in self.stage.objects:
            if hasattr(obj, 'drawable_component'):
                pyxel.blt(obj.position_component.x, obj.position_component.y, obj.drawable_component.img, obj.drawable_component.u, obj.drawable_component.v, obj.drawable_component.w, obj.drawable_component.h, obj.drawable_component.colkey)