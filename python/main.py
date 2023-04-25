# The main game file. Entry

import pyxel

from modules.game_manager import GameManager
from modules.level_manager import LevelManager

from modules.globals import *

# from input import Input

class App:

    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title=GAME_TITLE, fps=FPS)
        pyxel.load("./assets/rubiks.pyxres")
        
        self.started = False

        # pyxel.mouse(visible=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        if not self.started:
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT): 
                # Load the game manager
                self.game = GameManager.get_instance()

                # Star the game
                self.started = True
        else:
            self.game.update()
        
    def draw(self):
        pyxel.cls(0)
        
        if not self.started:
            pyxel.text(SCREEN_HEIGHT/2-3, SCREEN_WIDTH/2 - 50, GAME_TITLE, 15)
            pyxel.text(SCREEN_WIDTH/2-30, SCREEN_HEIGHT/2+30, "Click to Start", pyxel.frame_count % 16)
        else:
            self.game.render()
        
App()
