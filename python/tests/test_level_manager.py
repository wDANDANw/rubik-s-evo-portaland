import pytest
from modules.level_manager import LevelManager, LevelState
from modules.base_level import BaseLevel


class TestLevel(BaseLevel):

    __test__ = False # Tell Pytest not to treat as test class

    def load(self):
        pass

    def update(self, dt):
        pass

    def render(self):
        pass

    def unload(self):
        pass


def test_level_manager_initialization():
    level_manager = LevelManager()

    assert level_manager.active_level is None
    assert len(level_manager.level_states) == 0

# Meaningless - this should be private
# def test_set_active_level():
#     level_manager = LevelManager()
#     test_level = TestLevel(1, {})

#     level_manager.set_active_level(test_level)

#     assert level_manager.active_level == test_level


def test_load_level():
    level_manager = LevelManager()
    test_level = TestLevel(1, {})

    level_manager.load_level(test_level)

    assert level_manager.active_level == test_level


def test_update():
    level_manager = LevelManager()
    test_level = TestLevel(1, {})

    level_manager.load_level(test_level)

    level_manager.update(0.1)
    assert level_manager.active_level is not None


def test_render():
    level_manager = LevelManager()
    test_level = TestLevel(1, {})

    level_manager.load_level(test_level)

    level_manager.render()
    assert level_manager.active_level is not None


def test_level_states():
    level_manager = LevelManager()
    level_data = {"level_name": "Test Level"}

    level_manager.level_states["test_level"] = LevelState(1, level_data)

    stored_level_states = level_manager.get_level_states()

    assert stored_level_states["test_level"]["level_name"] == "Test Level"

    new_level_data = {"level_name": "New Test Level"}
    level_manager.load_level_states({"new_test_level": new_level_data})

    assert level_manager.level_states["new_test_level"].level_data["level_name"] == "New Test Level"