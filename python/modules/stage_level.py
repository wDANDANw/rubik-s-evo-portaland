import pyxel
from typing import List
from modules.stage_components import *
from modules.stage_systems import *
from modules.base_level import BaseLevel
from modules.globals import *

from modules.utils import to_snake_case

class StageObject:
    def __init__(self, name="default_object", components=()):
        self.name = name
        self.components = []
        for component in components:
            self.add_component(component)

    def add_component(self, component):
        self.components.append(component)
        component_name = component.__class__.__name__
        setattr(self, to_snake_case(component_name), component)

class StageSystemsDict(dict):
    
    def __init__(self, stage):
        super().__init__()

        self.stage = stage

    def __getattr__(self, system_name):
        if system_name in self:
            return self[system_name]
        raise AttributeError(f"'Level {self.stage.level_id}' has no system '{system_name}'")
    
    def add_system(self, system_name, system: System):
        self[system_name] = system
        

class StageWall(StageObject):
    def __init__(self):
        super().__init__("wall")

class StageLevel(BaseLevel):
    def __init__(self, level_id, level_data, tm, tmu, tmv):
        super().__init__(level_id, level_data)

        self.tm = tm
        self.tmu = tmu
        self.tmv = tmv

        self.player = None
        self.objects: List[StageObject] = []

        self.systems = StageSystemsDict(self)
        self.add_systems(
            MovementSystem(self),
            CollisionSystem(self),
            InputSystem(self),
            RenderSystem(self),
            AutoUpdateSystem(self)
        )

        self.wall_object = StageWall()

    def add_systems(self, *systems: System):
        for system in systems:
            system_name = to_snake_case(system.__class__.__name__)
            self.systems.add_system(system_name, system)
            setattr(self, system_name, system)

    def update_system(self, SystemClass):
        system_name = to_snake_case(SystemClass.__name__)
        if system_name in self.systems:
            self.systems[system_name].update()
        else:
            raise KeyError(f"No system of type '{SystemClass.__name__}' found in the stage {self.level_id}")

    def update_systems(self, *SystemClasses: tuple):
        for SystemClass in SystemClasses:
            self.update_system(SystemClass)

    def add_object(self, obj: StageObject):
        self.objects.append(obj)

    def remove_object(self, obj: StageObject):
        self.objects.remove(obj)

    def set_player(self, player: StageObject):
        self.player = player

    def render_stage(self, offset_x=0, offset_y=0):
        # Render the background of stage

        # bltm(x, y, tm, u, v, w, h, [colkey])
        pyxel.bltm(STAGE_UPPER_LEFT_X + offset_x, STAGE_UPPER_LEFT_Y + offset_y, 
                   self.tm, self.tmu, self.tmv,
                   STAGE_LEVEL_PIXEL_WIDTH, STAGE_LEVEL_PIXEL_HEIGHT, 
                   STAGE_TRANSPARENT_COLOR)