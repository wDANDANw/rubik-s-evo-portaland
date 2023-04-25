"""
File: base_level.py

This file contains the BaseLevel abstract class definition, which serves as a foundation for each level in the game. The BaseLevel class contains common functionality and properties that can be extended by specific level implementations. The class provides a common interface for all levels, implements shared functionality for level management, and enables level-specific customization through inheritance.
"""

from abc import ABC, abstractmethod

class BaseLevel(ABC):
    """
    BaseLevel is an abstract class that serves as a foundation for each level in the game. It contains common functionality and properties, which can be extended by specific level implementations. It provides a common interface for all levels, implements shared functionality for level management, and enables level-specific customization through inheritance.
    """

    def __init__(self, level_id: int, level_data: Dict[str, Any]):
        """
        Initialize the base level with level ID and level-specific data.
        1. Set level ID and level data as instance variables.
        2. Initialize any other required instance variables.
        """
        pass

    @abstractmethod
    def load(self):
        """
        Load the level resources and set up the initial game state.
        1. Load level-specific resources (e.g., images, sounds) using the level_data.
        2. Set up the initial game state, including entities, UI elements, and other level-specific configurations.
        """
        pass

    @abstractmethod
    def update(self, dt: float):
        """
        Update the level state based on the elapsed time since the last frame.
        1. Update all entities in the level.
        2. Check for and handle any events, collisions, or other level-specific logic.
        3. Update the game state as needed (e.g., player progress, level completion).
        """
        pass

    @abstractmethod
    def render(self):
        """
        Render the level, including entities and UI elements.
        1. Clear the screen with the appropriate background color.
        2. Render all entities in the level.
        3. Render UI elements, such as the HUD, menus, or other interactive components.
        """
        pass

    @abstractmethod
    def unload(self):
        """
        Unload the level resources and clean up the game state.
        1. Unload level-specific resources (e.g., images, sounds).
        2. Clean up any remaining entities, UI elements, and other level-specific configurations.
        """
        pass