import pytest
from modules.base_level import BaseLevel

class TestLevel(BaseLevel):

    __test__ = False # Tell Pytest not to treat as test class
    
    def load(self):
        pass

    def update(self, dt: float):
        pass

    def render(self):
        pass

    def unload(self):
        pass

@pytest.fixture
def test_level():
    level_data = {"player_start": (10, 10)}
    return TestLevel(1, level_data)

def test_init(test_level):
    assert test_level.level_id == 1
    assert test_level.level_data == {"player_start": (10, 10)}
    assert test_level.entities == []

def test_add_entity(test_level):
    entity = {"type": "player", "position": (10, 10)}
    test_level.add_entity(entity)
    assert entity in test_level.entities
    assert len(test_level.entities) == 1

def test_remove_entity(test_level):
    entity = {"type": "player", "position": (10, 10)}
    test_level.add_entity(entity)
    assert entity in test_level.entities
    assert len(test_level.entities) == 1

    test_level.remove_entity(entity)
    assert entity not in test_level.entities
    assert len(test_level.entities) == 0

def test_load_method_error():
    with pytest.raises(NotImplementedError):
        base_level = BaseLevel(1, {})
        base_level.load()

def test_update_method_error():
    with pytest.raises(NotImplementedError):
        base_level = BaseLevel(1, {})
        base_level.update(0)

def test_render_method_error():
    with pytest.raises(NotImplementedError):
        base_level = BaseLevel(1, {})
        base_level.render()

def test_unload_method_error():
    with pytest.raises(NotImplementedError):
        base_level = BaseLevel(1, {})
        base_level.unload()