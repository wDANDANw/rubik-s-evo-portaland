Class: ABC
Docstring:
Helper class that provides a standard way to create an ABC using
    inheritance.
    
Methods:

Class: BaseLevel
Docstring:

    BaseLevel is a base class that serves as a foundation for each level in the game. It contains common functionality and properties, which can be extended by specific level implementations. It provides a common interface for all levels, implements shared functionality for level management, and enables level-specific customization through inheritance.
    
Methods:
  __init__(self, level_id, level_data)
  add_entity(self, entity)
  load(self)
  remove_entity(self, entity)
  render(self)
  unload(self)
  update(self, dt)

Class: ColorSystem
Docstring:

    The ColorSystem class is responsible for managing color progression,
    palette changes, and the protagonist's shell color updates.
    
Methods:
  __init__(self, game_state)
  enable_color(self, color)
  get_available_colors(self)
  init_manager(self)
  on_color_pickup(self, color)
  update_protagonist_color(self)

Class: DisplayManager
Docstring:
No docstring available
Methods:
  __init__(self, pyxel_instance)
  add_game_object_to_layer(self, game_object, layer)
  remove_game_object_from_layer(self, game_object, layer)
  render(self)
  update_game_object_layer(self, game_object, old_layer, new_layer)

Class: Game
Docstring:
No docstring available
Methods:
  __init__(self)
  draw(self)
  game_over(self)
  new_game(self)
  update(self, inputs)

Class: GameObject
Docstring:
No docstring available
Methods:
  __init__(self, properties, behaviors, parameters)
  add_behavior(self, name, behavior)
  get_parameter(self, name)
  get_property(self, name)
  remove_behavior(self, name)
  render(self)
  set_parameter(self, name, value)
  set_property(self, name, value)
  update(self, dt)

Class: ABC
Docstring:
Helper class that provides a standard way to create an ABC using
    inheritance.
    
Methods:

Class: GameState
Docstring:

    GameState singleton class that stores and manages global game state information.
    
Methods:
  __init__(self)
  add_color(self, color)
  add_item(self, item)
  get_collected_items(self)
  get_color_progression(self)
  get_instance()
  load_game(self, filepath)
  reset(self)
  save_game(self, filepath)

Class: Item
Docstring:

    Item class that serves as the basis for various collectible items in the game.
    
Methods:
  __init__(self, type)
  from_dict(data)
  on_collect(self, game_state)
  to_dict(self)

Class: BaseLevel
Docstring:

    BaseLevel is a base class that serves as a foundation for each level in the game. It contains common functionality and properties, which can be extended by specific level implementations. It provides a common interface for all levels, implements shared functionality for level management, and enables level-specific customization through inheritance.
    
Methods:
  __init__(self, level_id, level_data)
  add_entity(self, entity)
  load(self)
  remove_entity(self, entity)
  render(self)
  unload(self)
  update(self, dt)

Class: LevelManager
Docstring:
No docstring available
Methods:
  __init__(self)
  _set_active_level(self, level)
  get_active_level(self)
  get_level_states(self)
  load_level(self, level)
  load_level_states(self, level_states)
  render(self)
  update(self, dt)

Class: LevelState
Docstring:
No docstring available
Methods:
  __init__(self, level_id, level_data)

Class: AbilityPickup
Docstring:

    Subclass of Pickup for ability pickups.
    Contains properties and methods specific to ability pickups.
    
Methods:
  __init__(self, ability)
  effect1(self, game_state)
  effect2(self, game_state)
  effect_add_ability(self, game_state)
  effect_factory(self, effect_name)
  from_dict(data)
  on_collect(self, game_state)
  to_dict(self)

Class: ColorPickup
Docstring:

    Subclass of Pickup for color pickups.
    Contains properties and methods specific to color pickups.
    
Methods:
  __init__(self, color)
  effect1(self, game_state)
  effect2(self, game_state)
  effect_add_color(self, game_state)
  effect_factory(self, effect_name)
  from_dict(data)
  on_collect(self, game_state)
  to_dict(self)

Class: GameState
Docstring:

    GameState singleton class that stores and manages global game state information.
    
Methods:
  __init__(self)
  add_color(self, color)
  add_item(self, item)
  get_collected_items(self)
  get_color_progression(self)
  get_instance()
  load_game(self, filepath)
  reset(self)
  save_game(self, filepath)

Class: Item
Docstring:

    Item class that serves as the basis for various collectible items in the game.
    
Methods:
  __init__(self, type)
  from_dict(data)
  on_collect(self, game_state)
  to_dict(self)

Class: Pickup
Docstring:

    Base class for Pickups.
    Inherits from the Item class and contains properties and methods common to all pickups.
    
Methods:
  __init__(self, pickup_type, effect_name)
  effect1(self, game_state)
  effect2(self, game_state)
  effect_factory(self, effect_name)
  from_dict(data)
  on_collect(self, game_state)
  to_dict(self)

Class: PickupSystem
Docstring:

    The PickupSystem class is responsible for managing the collection, activation,
    and usage of various pickups throughout the game. It provides methods for
    collecting pickups, applying their effects to the game state, and registering
    new pickup types.
    
Methods:
  __init__(self, game_state)
  collect_pickup(self, pickup)
  load_pickups_from_data(self, pickups_data)
  register_pickup_type(self, pickup_class)
  save_pickups_to_data(self)

Class: UIPickup
Docstring:

    Subclass of Pickup for UI-related pickups.
    Contains properties and methods specific to UI pickups.
    
Methods:
  __init__(self, pickup_type, effect_name)
  effect1(self, game_state)
  effect2(self, game_state)
  effect_factory(self, effect_name)
  from_dict(data)
  on_collect(self, game_state)
  to_dict(self)

Class: UIComponent
Docstring:

    UIComponent is an abstract class that serves as the base class for all UI elements in the game.
    
Methods:
  __init__(self, x, y, width, height, visible)
  render(self)
  update(self, dt)

Class: UISystem
Docstring:

    UISystem is a class responsible for managing the user interface, including HUD elements,
    menus, and other UI-related components. It handles the addition, removal, and updates of
    UI components as well as user input related to UI components.
    
Methods:
  __init__(self, game_state)
  add_ui_component(self, component)
  remove_ui_component(self, component)
  render(self)
  update(self, dt)

