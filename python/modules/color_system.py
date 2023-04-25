import pyxel

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
        self.game_state = game_state
        self.init_manager()

    def init_manager(self):
        """
        Initialize the palette manager by converting the whole palette to black.
        """
        for i in range(16):
            pyxel.pal(i, 0)

    def enable_color(self, color):
        """
        Enable a single color in the palette.

        Args:
            color (int): The color to enable.
        """
        pyxel.pal(color, color)

    def update_protagonist_color(self):
        """
        Update the protagonist's shell color based on collected colors.
        """
        collected_colors = self.game_state.get_color_progression()
        # Update the protagonist's shell color based on the collected colors.
        # This can be done in multiple ways, depending on how the protagonist's
        # shell color is represented in the game. One example is to simply set
        # the protagonist's shell color to the last collected color.
        protagonist_shell_color = collected_colors[-1]

    def get_available_colors(self):
        """
        Get a list of available colors.

        Returns:
            List[int]: A list of available colors.
        """
        return self.game_state.get_color_progression()

    def on_color_pickup(self, color):
        """
        Enable the picked-up color and update the protagonist's color.

        Args:
            color (int): The picked-up color.
        """
        self.enable_color(color)
        self.update_protagonist_color()