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

    def __init__(self, stage, x, y):

        self.stage = stage

        components = (
            PositionComponent(x, y),
            VelocityComponent(0, 0),
            HitboxComponent(1, 1),
            RenderableComponent(0, 0, 8, 8, 8, visible=False),
            AnimationComponent(0, 0, 8, 8, 8, frames=4, auto_update=False),
            InputComponent(self._player_handle_inputs),
            AutoUpdateComponent(),
        )

        super().__init__(name="player", components=components)

        self.prev_x = self.position_component.x
        self.prev_y = self.position_component.y

    def _player_handle_inputs(self, pressing, pressed, released):

        # Updating position component instead of velocity component because it's 16x16 and each update will be majorly visible (if using velocity, there is a high chance that it will update one more frame before release)
        if Inputs.LEFT in pressed:
            self.prev_x = self.position_component.x
            self.position_component.x += -1
            self.animation_component.update_one_tick(1)
            pyxel.play(3, 40)

        elif Inputs.RIGHT in pressed:
            self.prev_x = self.position_component.x
            self.position_component.x += 1
            self.animation_component.update_one_tick(-1)
            pyxel.play(3, 40)

        # if Inputs.LEFT in released or Inputs.RIGHT in released:
        #     self.velocity_component.dx = 0

    def handle_collision(self, other_obj):
        if other_obj.name == "wall":
            self.position_component.set_position(self.prev_x, self.prev_y)
            if hasattr(self.stage, "shake_screen_system"):
                self.stage.shake_screen_system.shake()
        
        elif other_obj.name == "white_color_pickup":
            self.stage.remove_object(other_obj)
            self.stage.lights_on = True
            self.renderable_component.visible = True
            pyxel.playm(1)

    def update(self):
        if self.bottom_tile_is_empty():
            tile_offset_x, tile_offset_y =self.renderable_component.add_offset(0,1.5)
            self.position_component.x += tile_offset_x
            self.position_component.y += tile_offset_y
        
        if self.position_component.x >= 14:
            LevelManager().get_instance().load_level(2)

    def bottom_tile_is_empty(self):
        return get_tile(self.position_component.x, self.position_component.y + 1) not in BLOCKING_TILES

class WhiteColorPickup(StageObject):
    
    
    def __init__(self):

        components = (
            PositionComponent(10, 14),
            HitboxComponent(1, 1),
            RenderableComponent(0, 0, 16, 8, 8)
        )

        super().__init__(name="white_color_pickup", components=components)


class Level_1(StageLevel):

    def __init__(self):
        super().__init__(
            level_id=1, 
            level_data={},
            tm=0,
            tmu=16*8, # Map 2
            tmv=0)

        self.set_player(Player(self, 3, 14))
        self.add_object(WhiteColorPickup())

        self.lights_on = False

    def load(self):
        pass

    def update(self):
        
        # self.systems.movement_system.update()
        self.update_system(InputSystem)

        self.update_system(MovementSystem)
        self.update_system(CollisionSystem)
        
        self.update_system(AutoUpdateSystem)

    def render(self):        
        self.update_system(RenderSystem)

    def unload(self):
        pass

    def render_stage(self, offset_x=0, offset_y=0):
        # Render the background of stage
        if self.lights_on:
            # bltm(x, y, tm, u, v, w, h, [colkey])
            pyxel.bltm(STAGE_UPPER_LEFT_X, STAGE_UPPER_LEFT_Y, 
                    self.tm, self.tmu, self.tmv,
                    STAGE_LEVEL_PIXEL_WIDTH, STAGE_LEVEL_PIXEL_HEIGHT, 
                    STAGE_TRANSPARENT_COLOR)