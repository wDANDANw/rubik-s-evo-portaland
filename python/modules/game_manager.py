
from .game_state import GameState
from .level_manager import LevelManager
from .color_system import ColorSystem
from .ui_system import UISystem
from .display_manager import DisplayManager
from .pickup_system import PickupSystem
from .input_manager import InputManager

class GameManager:

    __instance = None

    def __new__(cls):

        raise NotImplementedError("can not initialize via constructor.")

    def __init__(self):

        # Get Game State
        self.game_state = GameState.get_instance()

        # Init Level Manager and Load the Initial Level
        self.level_manager = LevelManager.get_instance()
        self.level_manager.init_manager()

        # Init the Input Manager
        self.input_manager = InputManager.get_instance()

        # self.color_system = ColorSystem(self.game_state)
        # self.ui_system = UISystem(self.game_state)

        # # self.display_manager = DisplayManager()
        
        # self.pickup_system = PickupSystem(self.game_state)

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
        # Get inputs
        # inputs = self.input_manager.update()

        # Update game systems
        # self.game_state.update()
        self.level_manager.update()
        # self.color_system.update()
        # self.ui_system.update()
        # self.pickup_system.update()

    def render(self):
        # Render game objects
        # self.display_manager.render()

        # Render level-specific entities
        self.level_manager.render()

        # Render UI components
        # self.ui_system.render()

    # def handle_user_input(self, inputs):
    #     # Handle user input for game state changes, e.g., starting a new game, pausing

    #     # Delegate user input handling to the active level implementation
    #     self.level_manager.handle_user_input(inputs)