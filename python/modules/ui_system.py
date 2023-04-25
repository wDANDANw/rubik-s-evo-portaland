"""
File: ui_system.py
Description: This file contains the UISystem class and the UIComponent abstract class.
             The UISystem class is responsible for managing the user interface, including
             HUD elements, menus, and other UI-related components. The UIComponent class
             serves as a base class for all UI elements in the game.
"""

# Import necessary libraries and modules
import pyxel


class UIComponent:
    """
    UIComponent is an abstract class that serves as the base class for all UI elements in the game.
    """

    def __init__(self, x, y, width, height, visible=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible

    def update(self, dt: float):
        """
        Update the UIComponent state based on the elapsed time since the last frame.

        Args:
            dt (float): The elapsed time since the last frame.
        """
        pass

    def render(self):
        """
        Render the UIComponent on the screen.
        """
        pass


class UISystem:
    """
    UISystem is a class responsible for managing the user interface, including HUD elements,
    menus, and other UI-related components. It handles the addition, removal, and updates of
    UI components as well as user input related to UI components.
    """

    def __init__(self, game_state):
        """
        Initialize the UI system with a reference to the game state.

        Args:
            game_state (GameState): A reference to the game state.
        """
        self.game_state = game_state
        self.ui_components = []

    def add_ui_component(self, component: UIComponent):
        """
        Add a UI element to the system.

        Args:
            component (UIComponent): The UI component to be added.
        """
        self.ui_components.append(component)

    def remove_ui_component(self, component: UIComponent):
        """
        Remove a UI element from the system.

        Args:
            component (UIComponent): The UI component to be removed.
        """
        self.ui_components.remove(component)

    def update(self, dt: float):
        """
        Update the UI elements based on the elapsed time since the last frame.

        Args:
            dt (float): The elapsed time since the last frame.
        """
        for component in self.ui_components:
            if component.visible:
                component.update(dt)

    def render(self):
        """
        Render the UI elements on the screen.
        """
        for component in self.ui_components:
            if component.visible:
                component.render()