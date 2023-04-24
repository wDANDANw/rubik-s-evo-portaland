## System Architecture Overview

This detailed and comprehensive description of the game's systems, components, and expected classes will guide the implementation process for the coder. Test cases are included to verify the functionality before the game starts and during gameplay.

### 1. GameState

**Description**: A singleton class that stores global game state information, such as color progression, collected items, and other gameplay-related data.

**Functionalities**:

- Store and manage global game state information
- Provide access to and modification of global state data

**Expected Classes / Instances / Entities**:

- `GameState` (Singleton Class)

**APIs / Signatures / Interfaces**:

- `get_instance() -> GameState`: Get the singleton instance of the `GameState` class.
- `get_color_progression() -> List[str]`: Get the current color progression of the game.
- `add_color(color: str)`: Add a color to the color progression.
- `get_collected_items() -> List[Item]`: Get the list of collected items.
- `add_item(item: Item)`: Add an item to the list of collected items.

### 2. BaseLevel

**Description**: An abstract class that serves as the foundation for each level, containing common functionality and properties that can be extended by specific level implementations.

**Functionalities**:

- Provide a common interface for all levels
- Implement shared functionality for level management
- Enable level-specific customization through inheritance

**Expected Classes / Instances / Entities**:

- `BaseLevel` (Abstract Class)

**APIs / Signatures / Interfaces**:

- `__init__(level_id: int, level_data: Dict[str, Any])`: Initialize the base level with level ID and level-specific data.
- `load()`: Load the level resources and set up the initial game state.
- `update(dt: float)`: Update the level state based on the elapsed time since the last frame.
- `render()`: Render the level, including entities and UI elements.
- `unload()`: Unload the level resources and clean up the game state.

### 3. SceneManager

**Description**: A class responsible for managing the active scene and handling transitions between scenes, such as loading and unloading levels, menus, or other game states.

**Functionalities**:

- Manage the active scene
- Handle transitions between scenes
- Load and unload scenes

**Expected Classes / Instances / Entities**:

- `SceneManager` (Class)

**APIs / Signatures / Interfaces**:

- `__init__()`: Initialize the scene manager.
- `get_active_scene() -> BaseLevel`: Get the currently active scene.
- `set_active_scene(scene: BaseLevel)`: Set the active scene.
- `load_scene(scene: BaseLevel)`: Load a scene, unloading the currently active scene if necessary.
- `update(dt: float)`: Update the active scene based on the elapsed time since the last frame.
- `render()`: Render the active scene, including entities and UI elements.

### 4. Display Manager

**Description**: A class that manages the rendering of game objects on multiple layers, utilizing Pyxel's layering functionality to prevent potential overdraws and optimize rendering performance.

**Functionalities**:

- Manage and organize renderable game objects into layers
- Render layers in the correct order using Pyxel's layering functionality
- Support adding, removing, and updating game objects within layers

**Expected Classes / Instances / Entities**:

- `DisplayManager` (Class)

**APIs / Signatures / Interfaces**:

- `__init__(pyxel_instance: Any)`: Initialize the display manager with a reference to the Pyxel instance.
- `add_game_object_to_layer(game_object: GameObject, layer: int)`: Add a game object to a specific layer for rendering.
- `remove_game_object_from_layer(game_object: GameObject, layer: int)`: Remove a game object from a specific layer.
- `update_game_object_layer(game_object: GameObject, old_layer: int, new_layer: int)`: Move a game object from one layer to another.
- `render()`: Render all layers in the correct order, utilizing Pyxel's layering functionality to prevent potential overdraws.

### 5. ColorSystem

**Description**: A class that manages color progression, palette changes, and the protagonist's shell color updates.

**Functionalities**:

- Manage color progression and palettes
- Update the protagonist's shell color based on the collected colors
- Determine if a specific color is available for use

**Expected Classes / Instances /Entities**:

- `ColorSystem` (Class)

**APIs / Signatures / Interfaces**:

- `__init__(game_state: GameState)`: Initialize the color system with a reference to the game state.
- `update_protagonist_color()`: Update the protagonist's shell color based on collected colors.
- `is_color_available(color: str) -> bool`: Check if a specific color is available for use.

### 6. MovementSystem

**Description**: A modular class that handles character movement for different levels, allowing for customization based on the level's requirements.

**Functionalities**:

- Handle character movement based on level-specific requirements
- Provide different movement modes (e.g., platformer, top-down)
- Update character positions based on movement capabilities

**Expected Classes / Instances / Entities**:

- `MovementSystem` (Class)

**APIs / Signatures / Interfaces**:

- `__init__(level: BaseLevel)`: Initialize the movement system with a reference to the current level.
- `set_movement_mode(mode: str)`: Set the movement mode for the level (e.g., 'platformer', 'top-down').
- `update(dt: float)`: Update character positions based on movement capabilities and elapsed time since the last frame.

### 7. PickupSystem

**Description**: A class that manages the collection, activation, and usage of various pickups throughout the game.

**Functionalities**:

- Manage pickup collection and activation
- Handle the effects of pickups on gameplay and game state
- Provide a way to add new pickup types

**Expected Classes / Instances / Entities**:

- `PickupSystem` (Class)
- `Pickup` (Base Class for Pickups)
- `ColorPickup`, `AbilityPickup`, `UIPickup` (Pickup Subclasses)

**APIs / Signatures / Interfaces**:

- `__init__(game_state: GameState)`: Initialize the pickup system with a reference to the game state.
- `collect_pickup(pickup: Pickup)`: Collect a pickup and apply its effects on the game state.
- `register_pickup_type(pickup_class: Type[Pickup])`: Register a new pickup type with the system.

### 8. AudioSystem

**Description**: A system to handle background music, sound effects, and other audio-related aspects of the game.

**Functionalities**:

- Play background music and sound effects
- Manage audio volume and settings
- Support different audio formats and sources

**Expected Classes / Instances / Entities**:

- `AudioSystem` (Class)

**APIs / Signatures / Interfaces**:

- `__init__()`: Initialize the audio system.
- `play_music(filename: str, loop: bool = True, volume: float = 1.0)`: Play background music from a file, with optional looping and volume settings.
- `play_sound(filename: str, volume: float = 1.0)`: Play a sound effect from a file, with an optional volume setting.
- `set_master_volume(volume: float)`: Set the master volume for all audio playback.

### 9. AnimationSystem

**Description**: A system responsible for managing animations for characters and objects in the game.

**Functionalities**:

- Play, pause, and stop animations
- Manage animation states and transitions
- Support various animation formats and sources

**Expected Classes / Instances / Entities**:

- `AnimationSystem` (Class)

**APIs / Signatures / Interfaces**:

- `__init__()`: Initialize the animation system.
- `play_animation(entity: Entity, animation_name: str)`: Play an animation for a specific entity.
- `pause_animation(entity: Entity)`: Pause the current animation for a specific entity.
- `stop_animation(entity: Entity)`: Stop the current animation for a specific entity and reset its state.
- `add_animation(entity: Entity, animation_name: str, frames: List[str], frame_duration: float)`: Add an animation to an entity with a name, a list of frame images, and frame duration.

### 10. UISystem

**Description**: A system to manage the user interface, including HUD elements, menus, and other UI-related components.

**Functionalities**:

- Manage UI elements and their states
- Handle user input related to UI components
- Support customizable UI themes and styles

**Expected Classes / Instances / Entities**:

- `UISystem` (Class)

**APIs / Signatures / Interfaces**:

- `__init__(game_state: GameState)`: Initialize the UI system with a reference to the game state.
- `add_ui_element(element: UIElement)`: Add a UI element to the system.
- `remove_ui_element(element: UIElement)`: Remove a UI element from the system.
- `update(dt: float)`: Update the UI elements based on the elapsed time since the last frame.
- `render()`: Render the UI elements on the screen.

### Test Cases

Before the game starts:

1. Test the initialization of the `GameState` singleton and ensure that it stores global state information correctly.
2. Test the creation and initialization of level instances, ensuring that they inherit from the `BaseLevel` class and implement the required methods.
3. Test the `SceneManager` by loading and unloading scenes, and verify that the active scene is updated correctly.

In-game:

1. Test the `ColorSystem` by collecting colors and verify that the protagonist's shell color and color progression are updated correctly.
2. Test the `MovementSystem` by moving the character in different levels and verify that the movement is accurate and responsive.
3. Test the `PickupSystem` by collecting various pickups and verify that their effects are applied to the game state and/or protagonist as expected.
4. Test the `AudioSystem` by playing background music and sound effects, and verify that the audio playback is correct and the volume settings work as expected.
5. Test the `AnimationSystem` by playing, pausing, and stopping animations, and verify that the animations are displayed correctly and the transitions between animation states work as expected.
6. Test the `UISystem` by interacting with UI elements and verify that user input is handled correctly and the UI elements are displayed and updated as expected.

By following these guidelines and test cases, the coder can implement the game's systems, components, and classes in a structured and efficient manner. Proper testing will ensure that the game's functionality is verified and validated before the game starts and during gameplay.



### Test Level 1: Basic Rendering and Interaction

**Description**: This test level will focus on verifying basic rendering, character movement, and simple interactions with the environment.

**Test Level Setup**:

1. Create a small level with a simple layout, including platforms, walls, and a few interactable objects.
2. Add the protagonist and a few NPCs to the level.
3. Set up basic movement mechanics, such as walking and jumping.

**Test Level Rendering**:

1. Verify that all game objects, including the protagonist, NPCs, platforms, and walls, are rendered correctly.
2. Verify that the background is rendered and visually separated from the foreground elements.
3. Verify that UI elements, such as the HUD, are rendered on top of the game scene.

**Testing**:

1. Test the protagonist's movement, ensuring that walking and jumping work as expected.
2. Test interactions with the environment, such as pushing objects or activating switches.
3. Test basic NPC behavior and animations.

### Test Level 2: Color System and Pickups

**Description**: This test level will focus on verifying the functionality of the color system and the collection and activation of various pickups.

**Test Level Setup**:

1. Create a level with multiple color-coded gates or tunnels, and color pickups scattered throughout the level.
2. Add a few pickups that grant new abilities or UI elements when collected.

**Test Level Rendering**:

1. Verify that color-coded gates or tunnels are rendered with their corresponding colors and change appearance when the required color is collected.
2. Verify that pickups are rendered correctly and visually distinguishable.

**Testing**:

1. Test the collection of color pickups and verify that the protagonist's shell color and color progression are updated correctly.
2. Test the activation of color-coded gates or tunnels and verify that they function as expected when the required color is collected.
3. Test the collection and activation of ability and UI pickups, ensuring that their effects are applied correctly.

### Test Level 3: Layered Rendering and Advanced Mechanics

**Description**: This test level will focus on verifying the functionality of the display manager's layered rendering and more advanced game mechanics, such as dimension-switching and complex puzzles.

**Test Level Setup**:

1. Create a level with multiple layers, including background, midground, and foreground elements.
2. Implement advanced game mechanics, such as dimension-switching or complex puzzles that require multiple steps to complete.

**Test Level Rendering**:

1. Verify that the display manager renders each layer correctly, preventing potential overdraws and optimizing performance.
2. Verify that the dimension-switching mechanic is visually represented, with smooth transitions between dimensions.

**Testing**:

1. Test the dimension-switching mechanic, ensuring that it functions as expected and updates the game state accordingly.
2. Test complex puzzles, verifying that the required steps are completed correctly and the puzzles are solvable.

These test levels, along with their specific rendering and testing sections, will help verify the functionality and performance of the game's systems, mechanics, and rendering. Ensuring that each test level passes the corresponding tests will help guarantee a smooth and polished gameplay experience.