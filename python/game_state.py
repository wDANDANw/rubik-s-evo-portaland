# Pseudo code for the Rubik's Evo Portaland game state

# Import necessary libraries
from typing import List

# Define an Item class that will represent collected items
class Item:
    pass

# Define a singleton GameState class to store and manage global game state information
class GameState:
    # Use a class attribute to store the single instance of the GameState class
    _instance = None

    # Define the __init__ method to initialize the game state
    def __init__(self):
        # Initialize a list to store color progression
        self._color_progression = []

        # Initialize a list to store collected items
        self._collected_items = []

    # Define a class method to get the singleton instance of the GameState class
    @classmethod
    def get_instance(cls):
        # If the _instance class attribute is None, create a new GameState instance
        if cls._instance is None:
            cls._instance = cls()

        # Return the singleton instance
        return cls._instance

    # Define a method to get the current color progression of the game
    def get_color_progression(self) -> List[str]:
        return self._color_progression

    # Define a method to add a color to the color progression
    def add_color(self, color: str):
        self._color_progression.append(color)

    # Define a method to get the list of collected items
    def get_collected_items(self) -> List[Item]:
        return self._collected_items

    # Define a method to add an item to the list of collected items
    def add_item(self, item: Item):
        self._collected_items.append(item)