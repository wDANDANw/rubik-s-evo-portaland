# level_manager.py
#
# This file contains the LevelManager class, which is responsible for managing
# the active level and handling transitions between levels, such as loading
# and unloading levels, menus, or other game states. It also contains the
# LevelState class, which stores the state of a level.

class LevelManager:
    def __init__(self):
        """
        Initialize the level manager.
        """
        # 1. Create a dictionary to store all LevelState instances, keyed by level IDs
        # 2. Set the active level to None

    def get_active_level(self) -> BaseLevel:
        """
        Get the currently active level.
        """
        # 1. Return the active level instance

    def set_active_level(self, level: BaseLevel):
        """
        Set the active level.
        """
        # 1. Set the active level instance to the given level

    def load_level(self, level: BaseLevel):
        """
        Load a level, unloading the currently active level if necessary.
        """
        # 1. Check if there is an active level
        # 2. If there is an active level, call its unload() method
        # 3. Set the active level to the given level
        # 4. Call the load() method of the new active level

    def update(self, dt: float):
        """
        Update the active level based on the elapsed time since the last frame.
        """
        # 1. Check if there is an active level
        # 2. If there is an active level, call its update() method with the elapsed time

    def render(self):
        """
        Render the active level, including entities and UI elements.
        """
        # 1. Check if there is an active level
        # 2. If there is an active level, call its render() method

    def get_level_states(self) -> Dict[str, Dict]:
        """
        Get all level states.
        """
        # 1. Create an empty dictionary for storing level states
        # 2. Iterate through all LevelState instances
        # 3. Add each level state to the dictionary with its level ID as the key
        # 4. Return the dictionary

    def load_level_states(self, level_states: Dict[str, Dict]):
        """
        Load all level states.
        """
        # 1. Iterate through the given level_states dictionary
        # 2. For each level state, create a new LevelState instance and add it to the stored LevelState instances

class LevelState:
    def __init__(self, level_id: int, level_data: Dict[str, Any]):
        """
        Initialize the level state with the level ID and level-specific data.
        """
        # 1. Set the level ID and level data attributes
        # 2. Initialize other properties required for storing the level state