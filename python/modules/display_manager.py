import pyxel


class DisplayManager:
    def __init__(self, pyxel_instance):
        """
        Initialize the display manager with a reference to the Pyxel instance.
        This is needed to access Pyxel's rendering functions.

        1. Initialize the layers dictionary to store game objects sorted by layers.
        2. Store the reference to the Pyxel instance.
        """
        self.layers = {}
        self.pyxel_instance = pyxel_instance

    def add_game_object_to_layer(self, game_object, layer):
        """
        Add a game object to a specific layer for rendering.

        Args:
            game_object (GameObject): The game object to add to the layer.
            layer (int): The layer index to add the game object to.

        1. Check if the layer exists in the layers dictionary.
        2. If the layer does not exist, create a new list for the layer.
        3. Append the game object to the layer's list.
        """
        if layer not in self.layers:
            self.layers[layer] = []

        self.layers[layer].append(game_object)

    def remove_game_object_from_layer(self, game_object, layer):
        """
        Remove a game object from a specific layer.

        Args:
            game_object (GameObject): The game object to remove from the layer.
            layer (int): The layer index to remove the game object from.

        1. Check if the layer exists in the layers dictionary.
        2. If the layer exists, remove the game object from the layer's list.
        """
        if layer in self.layers:
            self.layers[layer].remove(game_object)

    def update_game_object_layer(self, game_object, old_layer, new_layer):
        """
        Move a game object from one layer to another.

        Args:
            game_object (GameObject): The game object to move between layers.
            old_layer (int): The layer index to remove the game object from.
            new_layer (int): The layer index to add the game object to.

        1. Remove the game object from the old layer.
        2. Add the game object to the new layer.
        """
        self.remove_game_object_from_layer(game_object, old_layer)
        self.add_game_object_to_layer(game_object, new_layer)

    def render(self):
        """
        Render all layers in the correct order, utilizing Pyxel's layering
        functionality to prevent potential overdraws.

        1. Iterate through the layers dictionary in ascending order.
        2. For each layer, iterate through the game objects in the layer's list.
        3. Call the render method on each game object.
        """
        for layer in sorted(self.layers.keys()):
            for game_object in self.layers[layer]:
                game_object.render()