import pyxel
from typing import Dict, Any

from abc import ABC, abstractmethod

class BaseLevel:
    """
    BaseLevel is a base class that serves as a foundation for each level in the game. It contains common functionality and properties, which can be extended by specific level implementations. It provides a common interface for all levels, implements shared functionality for level management, and enables level-specific customization through inheritance.
    """

    __instance = None

    def __new__(cls):

        raise NotImplementedError("can not initialize via constructor.")

    def __init__(self, level_id: int, level_data: Dict[str, Any]):
        """
        Initialize the base level with level ID and level-specific data.
        """
        self.level_id = level_id
        self.level_data = level_data
        self.entities = []

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


    @abstractmethod
    def load(self):
        """
        Load the level resources and set up the initial game state.
        This method should be implemented in the subclass with level-specific resource loading and game state setup.
        """
        raise NotImplementedError("load method should be implemented in the subclass.")

    @abstractmethod
    def update(self):
        """
        Update the level state based on the elapsed time since the last frame.
        This method should be implemented in the subclass with level-specific update logic.
        """
        raise NotImplementedError("update method should be implemented in the subclass.")

    @abstractmethod
    def render(self):
        """
        Render the level, including entities and UI elements.
        This method should be implemented in the subclass with level-specific rendering logic.
        """
        raise NotImplementedError("render method should be implemented in the subclass.")

    @abstractmethod
    def unload(self):
        """
        Unload the level resources and clean up the game state.
        This method should be implemented in the subclass with level-specific resource unloading and game state cleanup.
        """
        raise NotImplementedError("unload method should be implemented in the subclass.")

    def add_entity(self, entity):
        """
        Add an entity to the level's list of entities.
        """
        self.entities.append(entity)

    def remove_entity(self, entity):
        """
        Remove an entity from the level's list of entities.
        """
        self.entities.remove(entity)