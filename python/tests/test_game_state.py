import pytest

# Types
import json
from typing import Any, Dict, List, Type

# Classes
from modules.game_state import GameState, Item

def test_singleton_instance_creation():
    """
    Test the creation of the GameState singleton instance.
    """
    instance1 = GameState.get_instance()
    instance2 = GameState.get_instance()

    assert instance1 is not None
    assert instance2 is not None
    assert instance1 is instance2


def test_color_progression():
    """
    Test the addition of colors to the color progression and retrieval of the color progression.
    """
    game_state = GameState.get_instance()

    game_state.add_color("red")
    game_state.add_color("blue")

    color_progression = game_state.get_color_progression()

    assert len(color_progression) == 2
    assert "red" in color_progression
    assert "blue" in color_progression

# region Item

class TestItem(Item):

    __test__ = False # Tell Pytest not to treat as test class

    def __init__(self):
        super().__init__("TestItem")

    def on_collect(self, game_state: GameState, color):
        game_state.add_color(color)

    @staticmethod
    def from_dict(data: Dict) -> 'Item':
        return TestItem()

    def to_dict(self) -> Dict:
        return {"type": "TestItem"}


def test_item_on_collect():
    """
    Test the on_collect method of the TestItem class.
    """
    game_state = GameState.get_instance()
    game_state.reset()

    color_green = "green"

    test_item = TestItem()
    test_item.on_collect(game_state, color_green)

    color_progression = game_state.get_color_progression()

    assert len(color_progression) == 1
    assert color_green in color_progression


def test_item_to_dict():
    """
    Test the to_dict method of the TestItem class.
    """
    test_item = TestItem()
    item_data = test_item.to_dict()

    assert item_data["type"] == "TestItem"

# endregion