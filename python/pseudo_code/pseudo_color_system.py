"""
File: color_system.py
Description: This file contains the implementation of the ColorSystem class, which
manages color progression, palette changes, and protagonist's shell color updates.
"""

# Import required classes and libraries
# from game_state import GameState

FULL_PALETTE = [
    # Add the full palette colors here, e.g., 0x000000, 0xFFFFFF, ...
]

class ColorSystem:
    """
    The ColorSystem class is responsible for managing color progression,
    palette changes, and the protagonist's shell color updates.
    """

    def __init__(self, game_state):
        """
        Initialize the ColorSystem with a reference to the game state.

        Args:
            game_state (GameState): A reference to the game state.
        """
        # Initialize and store the reference to the game state
        pass

    def init_manager(self):
        """
        Initialize the palette manager by converting the whole palette to black.

        Steps:
            1. Iterate through the full palette.
            2. Replace each color with black using Pyxel's pal() function.
        """
        pass

    def enable_color(self, color):
        """
        Enable a single color in the palette.

        Args:
            color (int): The color to enable.

        Steps:
            1. Replace the black color with the given color in the palette using Pyxel's pal() function.
        """
        pass

    def update_protagonist_color(self):
        """
        Update the protagonist's shell color based on collected colors.

        Steps:
            1. Retrieve the list of collected colors from the game state.
            2. Update the protagonist's shell color based on the collected colors.
        """
        pass

    def get_available_colors(self):
        """
        Get a list of available colors.

        Returns:
            List[int]: A list of available colors.

        Steps:
            1. Retrieve the list of collected colors from the game state.
            2. Return the list of available colors.
        """
        pass

    def on_color_pickup(self, color):
        """
        Enable the picked-up color and update the protagonist's color.
        
        Args:
            color (int): The picked-up color.

        Steps:
            1. Call enable_color() with the picked-up color.
            2. Call update_protagonist_color().
        """