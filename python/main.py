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
        
        TITLE_OFFSET_X = 40
        TITLE_OFFSET_Y = 15
        CLICK_TO_START_TEXT = "Click to Start"
        CLICK_TO_START_OFFSET_X = 26.5
        CLICK_TO_START_OFFSET_Y = 0

        if not self.started:
            pyxel.text(SCREEN_WIDTH/2 - TITLE_OFFSET_X, SCREEN_HEIGHT/2 - TITLE_OFFSET_Y, GAME_TITLE, 15)
            
            pyxel.text(SCREEN_WIDTH/2-CLICK_TO_START_OFFSET_X, 
                       SCREEN_HEIGHT/2+CLICK_TO_START_OFFSET_Y, 
                       CLICK_TO_START_TEXT, 
                       pyxel.frame_count % 16)
        else:
            self.game.render()
        
App()
