import pytest
from typing import Any, Callable, Dict

from modules.game_object import GameObject

class TestGameObject:

    @staticmethod
    def sample_behavior(dt: float):
        return dt * 2

    @pytest.fixture
    def game_object(self):
        properties = {"position": (0, 0), "size": (10, 10)}
        behaviors = {"double_dt": TestGameObject.sample_behavior}
        parameters = {"speed": 5}
        return GameObject(properties, behaviors, parameters)

    def test_update(self, game_object):
        dt = 0.5
        game_object.update(dt)
        assert game_object.behaviors["double_dt"](dt) == 1.0

    def test_add_behavior(self, game_object):
        def new_behavior(dt: float):
            return dt * 3

        game_object.add_behavior("triple_dt", new_behavior)
        assert "triple_dt" in game_object.behaviors
        assert game_object.behaviors["triple_dt"](0.5) == 1.5

    def test_remove_behavior(self, game_object):
        game_object.remove_behavior("double_dt")
        assert "double_dt" not in game_object.behaviors

    def test_set_property(self, game_object):
        game_object.set_property("position", (5, 5))
        assert game_object.get_property("position") == (5, 5)

    def test_get_property(self, game_object):
        assert game_object.get_property("position") == (0, 0)
        assert game_object.get_property("size") == (10, 10)

    def test_set_parameter(self, game_object):
        game_object.set_parameter("speed", 10)
        assert game_object.get_parameter("speed") == 10

    def test_get_parameter(self, game_object):
        assert game_object.get_parameter("speed") == 5