import pytest
from game_state import GameState, Item

# Test case for the GameState singleton
def test_game_state_singleton():
    game_state1 = GameState.get_instance()
    game_state2 = GameState.get_instance()

    assert game_state1 == game_state2

# Test case for color progression functionality
def test_color_progression():
    game_state = GameState.get_instance()

    colors = ["red", "blue", "green"]

    for color in colors:
        game_state.add_color(color)

    assert game_state.get_color_progression() == colors

# Test case for collected items functionality
def test_collected_items():
    game_state = GameState.get_instance()

    items = [Item(), Item(), Item()]

    for item in items:
        game_state.add_item(item)

    assert game_state.get_collected_items() == items