import pyxel
from enum import Enum, auto

class Inputs(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class InputManager:

    __instance = None

    def __new__(cls):

        raise NotImplementedError("can not initialize via constructor.")
    
    def __init__(self):
        self.inputs = []

    @classmethod
    def __internal_new__(cls):

        instance = super().__new__(cls)

        if instance is not None:
            instance.__init__()
            
        return instance

    @classmethod
    def get_instance(cls):

        if cls.__instance is None:
            cls.__instance = cls.__internal_new__()
            
        return cls.__instance

        
    def update(self):
        self.inputs.clear()
    
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W) or \
            pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.inputs.append(Inputs.UP)
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S) or \
            pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.inputs.append(Inputs.DOWN)
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A) or \
            pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.inputs.append(Inputs.LEFT)
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D) or \
            pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.inputs.append(Inputs.RIGHT)
            
        # if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_N) or \
        #     pyxel.btn(pyxel.GAMEPAD1_BUTTON_A):
        #     self.inputs.append(self.CONFIRM)
        # elif pyxel.btn(pyxel.KEY_X) or pyxel.btn(pyxel.KEY_M) or \
        #     pyxel.btn(pyxel.GAMEPAD1_BUTTON_B):
        #     self.inputs.append(self.CANCEL)
    
        return self
    
    def get_inputs(self):
        return self.inputs