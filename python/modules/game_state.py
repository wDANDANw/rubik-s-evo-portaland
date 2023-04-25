# Full code for the Rubik's Evo Portaland game state
"""
game_state.py

This file contains the GameState singleton class, which is responsible for managing
global game state information such as color progression, collected items, and other
gameplay-related data. It also provides methods for accessing and modifying the global
state data.

Additionally, this file contains the Item abstract class, which serves as the basis for
various collectible items in the game.
"""

import json
import inspect
from typing import Any, Dict, List, Type

from abc import ABC, abstractmethod

class GameState:
    """
    GameState singleton class that stores and manages global game state information.
    """
    
    __instance = None

    def __new__(cls):

        raise NotImplementedError("can not initialize via constructor.")

    def __init__(self):
        """
        Private constructor to initialize the GameState singleton instance.
        """
        self.color_progression = []
        self.collected_items = []

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

    
    def reset(self):
        """
        Reset the GameState instance to its initial state.
        """
        self.color_progression = []
        self.collected_items = []

    def get_color_progression(self) -> List[str]:
        """
        Get the current color progression of the game.

        Returns:
            List[str]: The list of collected colors.
        """
        return self.color_progression

    def add_color(self, color: str):
        """
        Add a color to the color progression.

        Args:
            color (str): The color to add to the progression.
        """
        self.color_progression.append(color)

    def get_collected_items(self) -> List['Item']:
        """
        Get the list of collected items.

        Returns:
            List[Item]: The list of collected items.
        """
        return self.collected_items

    def add_item(self, item: 'Item'):
        """
        Add an item to the list of collected items.

        Args:
            item (Item): The item to add to the list of collected items.
        """
        self.collected_items.append(item)

    def save_game(self, filepath: str):
        """
        Save the game state to a JSON file.

        Args:
            filepath (str): The path of the JSON file to save the game state.
        """
        print("Save Game Items: ", self.collected_items)
        print(bool(self.collected_items))
        print(inspect.getsource(self.collected_items[0].from_dict))
        with open(filepath, 'w') as file:
            json.dump({
                "color_progression": self.color_progression,
                "collected_items": [item.to_dict() for item in self.collected_items if self.collected_items]
            }, file)

    def load_game(self, filepath: str):
        """
        Load the game state from a JSON file and update the GameState instance.

        Args:
            filepath (str): The path of the JSON file to load the game state.
        """
        with open(filepath, 'r') as file:
            data = json.load(file)
            self.color_progression = data["color_progression"]
            self.collected_items = [Item.from_dict(item_data) for item_data in data["collected_items"]]


class Item:
    """
    Item class that serves as the basis for various collectible items in the game.
    """

    def __init__(self, type) -> None:
        self.type = type

    @abstractmethod
    def on_collect(self, game_state: GameState):
        """
        Abstract method to define the behavior when the item is collected by the player.

        Args:
            game_state (GameState): The instance of the GameState class.
        """
        raise NotImplementedError("on_collect method must be implemented in derived classes.")

    @staticmethod
    def from_dict(data: Dict) -> 'Item':
        """
        Create an Item instance from a dictionary.

        Args:
            data (Dict): The dictionary containing the item data.

        Returns:
            Item: The created Item instance.
        """
        item_subclasses = {cls.__name__: cls for cls in Item.__subclasses__()}
        item_type = data["type"]
        item_class = item_subclasses.get(item_type)
        if item_class:
            return item_class.from_dict(data)
        else:
            raise ValueError(f"Unknown item type '{item_type}'")

    @abstractmethod
    def to_dict(self) -> Dict:
        """
        Convert the Item instance to a dictionary.

        Returns:
            Dict: The dictionary containing the item data.
        """
        raise NotImplementedError("to_dict method must be implemented in derived classes.")