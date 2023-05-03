

import pyxel

from typing import Dict, Any

from modules.stage_level import StageLevel
from modules.level_manager import LevelManager

from modules.globals import *


class Level_1(StageLevel):

    def __init__(self):
        super().__init__(1, {})

    def load(self):
        pass

    def update(self):
        pass

    def render(self):        
        super().render_stage()


    def unload(self):
        pass