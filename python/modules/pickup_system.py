
from typing import Callable, Dict, Type
from modules.game_state import Item, GameState

class Pickup(Item):
    """
    Base class for Pickups.
    Inherits from the Item class and contains properties and methods common to all pickups.
    """

    def __init__(self, pickup_type: str, effect_name: str) -> None:
        super().__init__(pickup_type)
        self.effect_name = effect_name
        self.effect = self.effect_factory(effect_name)

    def effect_factory(self, effect_name: str) -> Callable:
        """
        A factory method that maps effect names to their corresponding effect functions.
        """
        effects = {
            "effect1": self.effect1,
            "effect2": self.effect2,
        }
        return effects.get(effect_name)

    def effect1(self, game_state: GameState):
        """
        Define the effect1 function.
        """
        pass

    def effect2(self, game_state: GameState):
        """
        Define the effect2 function.
        """
        pass

    def on_collect(self, game_state: GameState):
        """
        Apply the pickup's effect on the game state when collected.
        """
        self.effect(game_state)

    @staticmethod
    def from_dict(data: Dict) -> 'Pickup':
        return super().from_dict(data)

    def to_dict(self) -> Dict:
        data = {"type": self.type, "effect_name": self.effect_name}
        return data
class ColorPickup(Pickup):
    """
    Subclass of Pickup for color pickups.
    Contains properties and methods specific to color pickups.
    """

    def __init__(self, color: str) -> None:
        super().__init__("color", f"add_{color}")
        self.color = color

    def effect_add_color(self, game_state: GameState):
        """
        Define the effect function to add the color to the color progression in the game state.
        """
        game_state.add_color(self.color)

    def effect_factory(self, effect_name: str) -> Callable:
        """
        Extend the effect factory method to include color-specific effects.
        """
        effects = super().effect_factory(effect_name)
        effects.update({f"add_{self.color}": self.effect_add_color})
        return effects.get(effect_name)

    @staticmethod
    def from_dict(data: Dict) -> 'ColorPickup':
        return ColorPickup(color=data["color"])

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({"color": self.color})
        return data


class AbilityPickup(Pickup):
    """
    Subclass of Pickup for ability pickups.
    Contains properties and methods specific to ability pickups.
    """

    def __init__(self, ability: str) -> None:
        super().__init__("ability", f"add_{ability}")
        self.ability = ability

    def effect_add_ability(self, game_state: GameState):
        """
        Define the effect function to add the ability to the game state.
        """
        game_state.add_ability(self.ability)

    def effect_factory(self, effect_name: str) -> Callable:
        """
        Extend the effect factory method to include ability-specific effects.
        """
        effects = super().effect_factory(effect_name)
        effects.update({f"add_{self.ability}": self.effect_add_ability})
        return effects.get(effect_name)

    @staticmethod
    def from_dict(data: Dict) -> 'AbilityPickup':
        return AbilityPickup(ability=data["ability"])

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({"ability": self.ability})
        return data


class UIPickup(Pickup):
    """
    Subclass of Pickup for UI-related pickups.
    Contains properties and methods specific to UI pickups.
    """

    pass


class PickupSystem:
    """
    The PickupSystem class is responsible for managing the collection, activation,
    and usage of various pickups throughout the game. It provides methods for
    collecting pickups, applying their effects to the game state, and registering
    new pickup types.
    """

    def __init__(self, game_state: GameState):
        """
        Initialize the pickup system with a reference to the game state.
        """
        self.game_state = game_state
        self.collected_pickups = []

    def collect_pickup(self, pickup: Pickup):
        """
        Collect a pickup and apply its effects on the game state.
        """
        self.collected_pickups.append(pickup)
        pickup.on_collect(self.game_state)

    def register_pickup_type(self, pickup_class: Type[Pickup]):
        """
        Register a new pickup type with the system.
        This method can be used to add new pickup types as needed.
        """
        pass  # Implement the register_pickup_type method if necessary

    def load_pickups_from_data(self, pickups_data: Dict[str, Dict]):
        """
        Load pickups from a dictionary containing pickup data.
        This can be useful for loading pickups from a file or other external source.
        """
        for pickup_id, pickup_data in pickups_data.items():
            pickup = Pickup.from_dict(pickup_data)
            self.collected_pickups.append(pickup)

    def save_pickups_to_data(self) -> Dict[str, Dict]:
        """
        Save the current pickups to a dictionary that can be easily serialized.
        This can be useful for saving pickups to a file or other external source.
        """
        pickups_data = {}
        for pickup in self.collected_pickups:
            pickups_data[pickup.id] = pickup.to_dict()
        return pickups_data