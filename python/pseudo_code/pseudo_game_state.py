"""
game_state.py

This file contains the GameState singleton class, which is responsible for managing
global game state information such as color progression, collected items, and other
gameplay-related data. It also provides methods for accessing and modifying the global
state data.

Additionally, this file contains the Item abstract class, which serves as the basis for
various collectible items in the game.
"""

# Import required modules and classes
from typing import Any, Dict, List, Type

class GameState:
    """
    GameState singleton class that stores and manages global game state information.
    """
    
    def __init__(self):
        """
        Private constructor to initialize the GameState singleton instance.
        """
        pass

    @staticmethod
    def get_instance() -> 'GameState':
        """
        Get the singleton instance of the GameState class.
        
        Returns:
            GameState: The singleton instance of the GameState.
        """
        pass

    def get_color_progression(self) -> List[str]:
        """
        Get the current color progression of the game.

        Returns:
            List[str]: The list of collected colors.
        """
        pass

    def add_color(self, color: str):
        """
        Add a color to the color progression.

        Args:
            color (str): The color to add to the progression.
        """
        pass

    def get_collected_items(self) -> List['Item']:
        """
        Get the list of collected items.

        Returns:
            List[Item]: The list of collected items.
        """
        pass

    def add_item(self, item: 'Item'):
        """
        Add an item to the list of collected items.

        Args:
            item (Item): The item to add to the list of collected items.
        """
        pass

    def save_game(self, filepath: str):
        """
        Save the game state to a JSON file.

        Args:
            filepath (str): The path of the JSON file to save the game state.
        """
        pass

    def load_game(self, filepath: str):
        """
        Load the game state from a JSON file and update the GameState instance.

        Args:
            filepath (str): The path of the JSON file to load the game state.
        """
        pass


class Item:
    """
    Item abstract class that serves as the basis for various collectible items in the game.
    """

    def on_collect(self, game_state: GameState):
        """
        Abstract method to define the behavior when the item is collected by the player.

        Args:
            game_state (GameState): The instance of the GameState class.
        """
        pass
