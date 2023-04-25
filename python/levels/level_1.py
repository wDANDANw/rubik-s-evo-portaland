

import pyxel

from typing import Dict, Any

from modules.base_level import BaseLevel
from modules.level_manager import LevelManager

from modules.globals import *


class Level_1(BaseLevel):

    def __init__(self):
        super().__init__(1, {})

    def load(self):
        pass

    def update(self):
        pass

    def render(self):
        pyxel.blt(120, 30, 0, 0, 16, 16, 16, )
        # pyxel.bltm(50, 20, 0, 0, 0, 16*8, 16*8)

    def unload(self):
        pass