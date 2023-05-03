import pyxel

from typing import Dict, Any

from modules.stage_level import StageLevel, StageObject
from modules.stage_components import *
from modules.stage_systems import *
from modules.level_manager import LevelManager

from modules.globals import *


# Constants
BLOCKING_TILES = [WALL_TILE]


class Player(StageObject):

    def __init__(self, stage):

        self.stage = stage

        components = (
            PositionComponent(3, 1),
            VelocityComponent(0, 0),
            HitboxComponent(8, 8),
            RenderableComponent(0, 0, 8, 8, 8),
            AnimationComponent(0, 0, 8, 8, 8, frames=4, auto_update=False),
            InputComponent(self._player_handle_inputs),
            AutoUpdateComponent(),
        )

        super().__init__(name="player", components=components)

        self.prev_x = self.position_component.x
        self.prev_y = self.position_component.y

        self.flying = True

    def _player_handle_inputs(self, pressing, pressed, released):

        if self.flying:
            return

        # Updating position component instead of velocity component because it's 16x16 and each update will be majorly visible (if using velocity, there is a high chance that it will update one more frame before release)
        if Inputs.LEFT in pressed:
            self.prev_x = self.position_component.x
            self.position_component.x += -1
            self.animation_component.update_one_tick(1)

        elif Inputs.RIGHT in pressed:
            self.prev_x = self.position_component.x
            self.position_component.x += 1
            self.animation_component.update_one_tick(-1)

        # if Inputs.LEFT in released or Inputs.RIGHT in released:
        #     self.velocity_component.dx = 0

    def handle_collision(self, other_obj):
        if other_obj.name == "wall":

            if self.flying:
                self.flying = False
                self.position_component.set_position(10, 9)
                self.prev_x = 10
                self.prev_y = 9
                return

            self.position_component.set_position(self.prev_x, self.prev_y)
            self.renderable_component.clear_offset()

            if hasattr(self.stage, "shake_screen_system"):
                self.stage.shake_screen_system.shake()
                pyxel.play(3, 41)


    def update(self):

        if self.flying:
            tile_offset_x, tile_offset_y =self.renderable_component.add_offset(1,1)
            self.position_component.x += tile_offset_x
            self.position_component.y += tile_offset_y
            self.animation_component.update_one_tick(1)
            return

        if self.bottom_tile_is_empty():
            tile_offset_x, tile_offset_y =self.renderable_component.add_offset(0,1.5)
            self.position_component.x += tile_offset_x
            self.position_component.y += tile_offset_y
                

    def bottom_tile_is_empty(self):
        return get_tile(self.position_component.x, self.position_component.y + 1) not in BLOCKING_TILES

class Level_2(StageLevel):

    def __init__(self):
        super().__init__(
            level_id=2, 
            level_data={},
            tm=0,
            tmu=0,
            tmv=0)

        self.set_player(Player(self))
        self.add_systems(ShakeScreenSystem(self))

    def load(self):
        pass

    def update(self):
        
        # self.systems.movement_system.update()
        self.update_system(InputSystem)

        self.update_system(MovementSystem)
        self.update_system(CollisionSystem)
        
        self.update_system(AutoUpdateSystem)
        self.update_system(ShakeScreenSystem)

    def render(self):        
        self.update_system(RenderSystem)

    def unload(self):
        pass