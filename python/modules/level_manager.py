# level_manager.py

from typing import Dict, Any, Type
from .base_level import BaseLevel
from .stage_level import StageLevel

import os, importlib, inspect

LEVEL_DIRECTORY = "../levels/"
factory_levels = [BaseLevel, StageLevel]
def is_factory_level(obj):
    
    answer = False

    for level in factory_levels:
        if obj is level:
            answer = True
            break
    
    return answer

class LevelManager:

    __instance = None

    def __init__(self):
        """
        Initialize the level manager.
        """
        self.levels = {}
        self.current_level_id = -1  # Set the active level to None
        self._current_level = None 

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

    def init_manager(self):
        # Load all levels
        self.load_all_levels()

        # Set the first level to be level 0
        self.load_level(0)
       

    def get_current_level_id(self) -> int:
        """
        Get the currently active level id
        """
        return self.current_level_id

    def _set_active_level(self, level_id : int):
        """
        Set the active level.
        """
        self._current_level = self.levels[level_id]

    def load_level(self, target_level_id: int):
        """
        Load a level, unloading the currently active level if necessary.
        """
        if self._current_level:
            self._current_level.unload()
        self._set_active_level(target_level_id)
        self._current_level.load()

    def update(self):
        """
        Update the active level based on the elapsed time since the last frame.
        """
        if self._current_level:
            self._current_level.update()

    def render(self):
        """
        Render the active level, including entities and UI elements.
        """
        if self._current_level:
            self._current_level.render()

    def get_level_states(self) -> Dict[str, Dict]:
        """
        Get all level states.
        """
        raise NotImplementedError("Implement this later when saving & loading")
        level_states = {}
        # for level_id, level_instance in self.levels.items():
        #     level_states[level_id] = level_state.level_data
        return level_states

    def load_level_states(self, level_states: Dict[str, Dict]):
        """
        Load all level states.
        """
        raise NotImplementedError("Implement this later when saving & loading")
        # for level_id, level_data in level_states.items():
        #     self.level_states[level_id] = LevelState(level_id, level_data)

    def load_all_levels(self):
        """
        Load all levels.
        """

        levels = {}

        # Iterate through all files in the levels directory
        absolute_path = os.path.dirname(__file__)
        full_path = os.path.join(absolute_path, LEVEL_DIRECTORY)

        for file in os.listdir(full_path):
            if file.endswith(".py") and not file.startswith("__"):
                # Remove the file extension to get the module name
                module_name = file[:-3]

                # Import the module dynamically
                module = importlib.import_module(f"levels.{module_name}")

                # Inspect the module to find Level_X classes
                for name, obj in inspect.getmembers(module):

                    if inspect.isclass(obj) and issubclass(obj, BaseLevel) and not is_factory_level(obj):
                        # Get the level number from the class name
                        level_number = int(name.split("_")[-1])

                        # Add the level class to the dictionary
                        levels[level_number] = obj.get_instance()

        assert len(levels) > 0, "No levels found"
        self.levels = levels




