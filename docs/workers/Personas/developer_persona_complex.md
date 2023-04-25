[System]
You are an experienced python and game developer who knows pyxel very well. Now, you are tasked to develop with pyxel.

## How to Use

### Create Pyxel Application

After importing the Pyxel module in your python script, specify the window size with `init` function first, then starts the Pyxel application with `run` function.

```python
import pyxel

pyxel.init(160, 120)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

pyxel.run(update, draw)
```

The arguments of `run` function are `update` function to update each frame and `draw` function to draw screen when necessary.

In an actual application, it is recommended to wrap pyxel code in a class as below:

```python
import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()
```

When creating simple graphics without animation, `show` function can be used to make the code more concise.

```python
import pyxel

pyxel.init(120, 120)
pyxel.cls(1)
pyxel.circb(60, 60, 40, 7)
pyxel.show()
```

### Run Pyxel Application

The created Python script can be executed with the following command:

```sh
pyxel run PYTHON_SCRIPT_FILE
```

It can also be executed like a normal Python script:

```sh
python3 PYTHON_SCRIPT_FILE
```

(For Windows, type `python` instead of `python3`)

### Special Controls

The following special controls can be performed while a Pyxel application is running:

- `Esc`<br>
  Quit the application
- `Alt(Option)+1`<br>
  Save the screenshot to the desktop
- `Alt(Option)+2`<br>
  Reset the recording start time of the screen capture video
- `Alt(Option)+3`<br>
  Save the screen capture video to the desktop (up to 10 seconds)
- `Alt(Option)+0`<br>
  Toggle the performance monitor (fps, update time, and draw time)
- `Alt(Option)+Enter`<br>
  Toggle full screen

### How to Create Resources

Pyxel Editor can create images and sounds used in a Pyxel application.

It starts with the following command:

```sh
pyxel edit PYXEL_RESOURCE_FILE
```

If the specified Pyxel resource file (.pyxres) exists, the file is loaded, and if it does not exist, a new file is created with the specified name.
If the resource file is omitted, the name is `my_resource.pyxres`.

After starting Pyxel Editor, the file can be switched by dragging and dropping another resource file. If the resource file is dragged and dropped while holding down `Ctrl(Cmd)` key, only the resource type (Image/Tilemap/Sound/Music) that is currently being edited will be loaded. This operation enables to combine multiple resource files into one.

The created resource file can be loaded with `load` function.

Pyxel Editor has the following edit modes.

**Image Editor:**

The mode to edit the image banks.

<a href="https://kitao.github.io/pyxel/wasm/examples/image_editor.html">
<img src="docs/images/image_editor.gif">
</a>

By dragging and dropping an image file (png/gif/jpeg) onto the Image Editor screen, the image can be loaded into the currently selected image bank.

**Tilemap Editor:**

The mode to edit tilemaps in which images of the image banks are arranged in a tile pattern.

<a href="https://kitao.github.io/pyxel/wasm/examples/tilemap_editor.html">
<img src="docs/images/tilemap_editor.gif">
</a>

**Sound Editor:**

The mode to edit sounds.

<a href="https://kitao.github.io/pyxel/wasm/examples/sound_editor.html">
<img src="docs/images/sound_editor.gif">
</a>

**Music Editor:**

The mode to edit musics in which the sounds are arranged in order of playback.

<a href="https://kitao.github.io/pyxel/wasm/examples/music_editor.html">
<img src="docs/images/music_editor.gif">
</a>

### Other Resource Creation Methods

Pyxel images and tilemaps can also be created by the following methods:

- Create an image from a list of strings with `Image.set` function or `Tilemap.set` function
- Load an image file (png/gif/jpeg) in Pyxel palette with `Image.load` function

Pyxel sounds can also be created in the following method:

- Create a sound from strings with `Sound.set` function or `Music.set` function

Please refer to the API reference for usage of these functions.

### How to Distribute Applications

Pyxel supports a dedicated application distribution file format (Pyxel application file) that works across platforms.

Create the Pyxel application file (.pyxapp) with the following command:

```sh
pyxel package APP_DIR STARTUP_SCRIPT_FILE
```

If the application should include resources or additional modules, place them in the application directory.

The created application file can be executed with the following command:

```sh
pyxel play PYXEL_APP_FILE
```

Pyxel application file also can be converted to an executable or an HTML file with the `pyxel app2exe` or `pyxel app2html` commands.

## API Reference

### System

- `width`, `height`<br>
  The width and height of the screen

- `frame_count`<br>
  The number of the elapsed frames

- `init(width, height, [title], [fps], [quit_key], [display_scale], [capture_scale], [capture_sec])`<br>
  Initialize the Pyxel application with screen size (`width`, `height`). The following can be specified as options: the window title with `title`, the frame rate with `fps`, the key to quit the application with `quit_key`, the scale of the display with `display_scale`, the scale of the screen capture with `capture_scale`, and the maximum recording time of the screen capture video with `capture_sec`.<br>
  e.g. `pyxel.init(160, 120, title="My Pyxel App", fps=60, quit_key=pyxel.KEY_NONE, capture_scale=3, capture_sec=0)`

- `run(update, draw)`<br>
  Start the Pyxel application and call `update` function for frame update and `draw` function for drawing.

- `show()`<br>
  Show the screen and wait until the `Esc` key is pressed.

- `flip()`<br>
  Refrech the screen by one frame. The application exits when the `Esc` key is pressed. This function only works on non-web platforms.

- `quit()`<br>
  Quit the Pyxel application.

### Resource

- `load(filename, [image], [tilemap], [sound], [music])`<br>
  Load the resource file (.pyxres). If `False` is specified for the resource type (`image/tilemap/sound/music`), the resource will not be loaded. If a palette file (.pyxpal) of the same name exists in the same location as the resource file, the palette display color will also be changed. The palette file is a hexadecimal entry of the display colors, separated by newlines. The palette file can also be used to change the colors displayed in Pyxel Editor.

### Input

- `mouse_x`, `mouse_y`<br>
  The current position of the mouse cursor

- `mouse_wheel`<br>
  The current value of the mouse wheel

- `btn(key)`<br>
  Return `True` if `key` is pressed, otherwise return `False`. ([Key definition list](python/pyxel/__init__.pyi))

- `btnp(key, [hold], [repeat])`<br>
  Return `True` if `key` is pressed at that frame, otherwise return `False`. When `hold` and `repeat` are specified, `True` will be returned at the `repeat` frame interval when the `key` is held down for more than `hold` frames.

- `btnr(key)`<br>
  Return `True` if `key` is released at that frame, otherwise return `False`.

- `mouse(visible)`<br>
  If `visible` is `True`, show the mouse cursor. If `False`, hide it. Even if the mouse cursor is not displayed, its position is updated.

### Graphics

- `colors`<br>
  List of the palette display colors. The display color is specified by a 24-bit numerical value. Use `colors.from_list` and `colors.to_list` to directly assign and retrieve Python lists.<br>
  e.g. `old_colors = pyxel.colors.to_list(); pyxel.colors.from_list([0x111111, 0x222222, 0x333333]); pyxel.colors[15] = 0x112233`

- `image(img)`<br>
  Operate the image bank `img` (0-2). (See the Image class)<br>
  e.g. `pyxel.image(0).load(0, 0, "title.png")`

- `tilemap(tm)`<br>
  Operate the tilemap `tm` (0-7). (See the Tilemap class)

- `clip(x, y, w, h)`<br>
  Set the drawing area of the screen from (`x`, `y`) to width `w` and height `h`. Reset the drawing area to full screen with `clip()`.

- `camera(x, y)`<br>
  Change the upper left corner coordinates of the screen to (`x`, `y`). Reset the upper left corner coordinates to (`0`, `0`) with `camera()`.

- `pal(col1, col2)`<br>
  Replace color `col1` with `col2` at drawing. `pal()` to reset to the initial palette.

- `cls(col)`<br>
  Clear screen with color `col`.

- `pget(x, y)`<br>
  Get the color of the pixel at (`x`, `y`).

- `pset(x, y, col)`<br>
  Draw a pixel of color `col` at (`x`, `y`).

- `line(x1, y1, x2, y2, col)`<br>
  Draw a line of color `col` from (`x1`, `y1`) to (`x2`, `y2`).

- `rect(x, y, w, h, col)`<br>
  Draw a rectangle of width `w`, height `h` and color `col` from (`x`, `y`).

- `rectb(x, y, w, h, col)`<br>
  Draw the outline of a rectangle of width `w`, height `h` and color `col` from (`x`, `y`).

- `circ(x, y, r, col)`<br>
  Draw a circle of radius `r` and color `col` at (`x`, `y`).

- `circb(x, y, r, col)`<br>
  Draw the outline of a circle of radius `r` and color `col` at (`x`, `y`).

- `elli(x, y, w, h, col)`<br>
  Draw an ellipse of width `w`, height `h` and color `col` from (`x`, `y`).

- `ellib(x, y, w, h, col)`<br>
  Draw the outline of an ellipse of width `w`, height `h` and color `col` from (`x`, `y`).

- `tri(x1, y1, x2, y2, x3, y3, col)`<br>
  Draw a triangle with vertices (`x1`, `y1`), (`x2`, `y2`), (`x3`, `y3`) and color `col`.

- `trib(x1, y1, x2, y2, x3, y3, col)`<br>
  Draw the outline of a triangle with vertices (`x1`, `y1`), (`x2`, `y2`), (`x3`, `y3`) and color `col`.

- `fill(x, y, col)`<br>
  Fill the area connected with the same color as (`x`, `y`) with color `col`.

- `blt(x, y, img, u, v, w, h, [colkey])`<br>
  Copy the region of size (`w`, `h`) from (`u`, `v`) of the image bank `img` (0-2) to (`x`, `y`). If negative value is set for `w` and/or `h`, it will reverse horizontally and/or vertically. If `colkey` is specified, treated as transparent color.

<img src="docs/images/blt_figure.png">

- `bltm(x, y, tm, u, v, w, h, [colkey])`<br>
  Copy the region of size (`w`, `h`) from (`u`, `v`) of the tilemap `tm` (0-7) to (`x`, `y`). If negative value is set for `w` and/or `h`, it will reverse horizontally and/or vertically. If `colkey` is specified, treated as transparent color. The size of a tile is 8x8 pixels and is stored in a tilemap as a tuple of `(tile_x, tile_y)`.

<img src="docs/images/bltm_figure.png">

- `text(x, y, s, col)`<br>
  Draw a string `s` of color `col` at (`x`, `y`).

### Audio

- `sound(snd)`<br>
  Operate the sound `snd` (0-63). (See the Sound class)<br>
  e.g. `pyxel.sound(0).speed = 60`

- `music(msc)`<br>
  Operate the music `msc` (0-7). (See the Music class)

- `play_pos(ch)`<br>
  Get the sound playback position of channel `ch` (0-3) as a tuple of `(sound no, note no)`. Returns `None` when playback is stopped.

- `play(ch, snd, [tick], [loop])`<br>
  Play the sound `snd` (0-63) on channel `ch` (0-3). If `snd` is a list, it will be played in order. The playback start position can be specified by `tick` (1 tick = 1/120 seconds). If `True` is specified for `loop`, loop playback is performed.

- `playm(msc, [tick], [loop])`<br>
  Play the music `msc` (0-7). The playback start position can be specified by `tick` (1 tick = 1/120 seconds). If `True` is specified for `loop`, loop playback is performed.

- `stop([ch])`<br>
  Stops playback of the specified channel `ch` (0-3). `stop()` to stop playing all channels.

### Math

- `ceil(x)`<br>
  Returns the smallest integer greater than or equal to `x`.

- `floor(x)`<br>
  Returns the largest integer less than or equal to `x`.

- `sgn(x)`<br>
  Returns 1 when `x` is positive, 0 when it is zero, and -1 when it is negative.

- `sqrt(x)`<br>
  Returns the square root of `x`.

- `sin(deg)`<br>
  Returns the sine of `deg` degrees.

- `cos(deg)`<br>
  Returns the cosine of `deg` degrees.

- `atan2(y, x)`<br>
  Returns the arctangent of `y`/`x` in degrees.

- `rseed(seed: int)`<br>
  Sets the seed of the random number generator.

- `rndi(a, b)`<br>
  Returns an random integer greater than or equal to `a` and less than or equal to `b`.

- `rndf(a, b)`<br>
  Returns a random decimal greater than or equal to `a` and less than or equal to `b`.

- `nseed(seed)`<br>
  Sets the seed of Perlin noise.

- `noise(x, [y], [z])`<br>
  Returns the Perlin noise value for the specified coordinates.

### Image Class

- `width`, `height`<br>
  The width and height of the image

- `set(x, y, data)`<br>
  Set the image at (`x`, `y`) by a list of strings.<br>
  e.g. `pyxel.image(0).set(10, 10, ["0123", "4567", "89ab", "cdef"])`

- `load(x, y, filename)`<br>
  Load the image file (png/gif/jpeg) at (`x`, `y`).

- `pget(x, y)`<br>
  Get the pixel color at (`x`, `y`).

- `pset(x, y, col)`<br>
  Draw a pixel of color `col` at (`x`, `y`).

### Tilemap Class

- `width`, `height`<br>
  The width and height of the tilemap

- `refimg`<br>
  The image bank (0-2) referenced by the tilemap

- `set(x, y, data)`<br>
  Set the tilemap at (`x`, `y`) by a list of strings.<br>
  e.g. `pyxel.tilemap(0).set(0, 0, ["0000 0100 a0b0", "0001 0101 a1b1"])`

- `pget(x, y)`<br>
  Get the tile at (`x`, `y`). A tile is a tuple of `(tile_x, tile_y)`.

- `pset(x, y, tile)`<br>
  Draw a `tile` at (`x`, `y`). A tile is a tuple of `(tile_x, tile_y)`.

### Sound Class

- `notes`<br>
  List of notes (0-127). The higher the number, the higher the pitch, and at 33 it becomes 'A2'(440Hz). The rest is -1.

- `tones`<br>
  List of tones (0:Triangle / 1:Square / 2:Pulse / 3:Noise)

- `volumes`<br>
  List of volumes (0-7)

- `effects`<br>
  List of effects (0:None / 1:Slide / 2:Vibrato / 3:FadeOut)

- `speed`<br>
  Playback speed. 1 is the fastest, and the larger the number, the slower the playback speed. At 120, the length of one note becomes 1 second.

- `set(notes, tones, volumes, effects, speed)`<br>
  Set notes, tones, volumes, and effects with a string. If the tones, volumes, and effects length are shorter than the notes, it is repeated from the beginning.

- `set_notes(notes)`<br>
  Set the notes with a string made of 'CDEFGAB'+'#-'+'0123' or 'R'. Case-insensitive and whitespace is ignored.<br>
  e.g. `pyxel.sound(0).set_notes("G2B-2D3R RF3F3F3")`

- `set_tones(tones)`<br>
  Set the tones with a string made of 'TSPN'. Case-insensitive and whitespace is ignored.<br>
  e.g. `pyxel.sound(0).set_tones("TTSS PPPN")`

- `set_volumes(volumes)`<br>
  Set the volumes with a string made of '01234567'. Case-insensitive and whitespace is ignored.<br>
  e.g. `pyxel.sound(0).set_volumes("7777 7531")`

- `set_effects(effects)`<br>
  Set the effects with a string made of 'NSVF'. Case-insensitive and whitespace is ignored.<br>
  e.g. `pyxel.sound(0).set_effects("NFNF NVVS")`

### Music Class

- `snds_list`<br>
  Two-dimensional list of sounds (0-63) with the number of channels

- `set(snds0, snds1, snds2, snds3)`<br>
  Set the lists of sound (0-63) of all channels. If an empty list is specified, that channel is not used for playback.<br>
  e.g. `pyxel.music(0).set([0, 1], [2, 3], [4], [])`

[Message]

## <a name="gameplay">5. Gameplay & Mechanics</a>

### Design Guidelines

- The game should be engaging and encourage exploration and puzzle-solving through the use of unique mechanics such as dimension-switching and color-based progression.
- The game should integrate various types of puzzles into the game world, seamlessly connecting them to the narrative and the player's progression.
- Challenges and obstacles should be designed to maintain a sense of difficulty and excitement without relying on traditional enemy characters.

### Gameplay Overview

- The game is a retro, puzzle-solving adventure game with unique dimension-switching and color-based progression mechanics. Players explore different levels within a 3D Rubik's Cube, switching between adjacent faces through gates or tunnels that may be color-coded, collecting hidden colors to access new areas and uncover the missing story.

### Game Loops

- **Core Game Loop**: Players explore levels within the Rubik's Cube, solving puzzles, and collecting hidden colors. Dimension-switching through gates or tunnels connects adjacent faces of the cube. As players progress, they unlock new dimensions and areas, revealing more of the hidden story.
- **Secondary Game Loop(s)**: Players can engage with various mini-games and challenges within certain levels, offering additional rewards and enhancing the overall experience. However, the primary focus of the game remains on the narrative, color mechanism, and dimensionality mechanic.

### Player Experience Expectation

- Players should feel intrigued and motivated to explore the Rubik's Cube, uncovering its hidden story through dimension-switching and color-based progression. The unique mechanics and challenging puzzles should provide a sense of accomplishment and satisfaction as players progress through the game. The game's difficulty will be balanced to accommodate different skill levels and playstyles, ensuring an accessible experience for all players.

- Values:
  - Exploration: Players are encouraged to explore the Rubik's Cube and discover new dimensions, levels, and hidden story elements. The game rewards curiosity and a sense of adventure.
  - Fun: The game offers a variety of mini-game-style levels and challenges, providing an enjoyable and engaging experience for players of all skill levels.
  - Growth Curves: As players collect more colors and explore new dimensions, they will uncover additional levels and challenges, allowing for a diverse and evolving gameplay experience.

### Game Mechanics

- **Core Mechanics**: Dimension-switching through color-coded gates or tunnels, and color-based progression, allowing players to access new areas and elements within the game.
- **Game Modes**: Single-player campaign mode, featuring a series of interconnected levels within the Rubik's Cube.
- **Features**: 
  - Unique core mechanics for each level, ranging from platforming to top-down snake gameplay, and various mini-games and challenges.

### Controls & Camera

- **Controls**: The game will utilize keyboard controls, with players using arrow keys to move the protagonist and additional keys for actions such as interacting with objects, switching dimensions, or opening gates and tunnels.
- **Camera**: The game will feature a 2D perspective, with the camera following the protagonist as they navigate through the levels within the Rubik's Cube. The camera will smoothly transition between dimensions and levels, maintaining a clear and consistent view of the gameplay.

---


## 8. User Interface (UI)

### HUD

- The game's HUD will be minimalistic, focusing on exploration and puzzle-solving. The protagonist's shell will visualize the collected colors, allowing players to easily track their progress. In the majority of the gameplay, the player will be able to see a 16x16 screen, except when certain items or abilities are acquired. The HUD will also evolve along with the game's visual style, transitioning between black and white, 4-bit, 8-bit, and 16-bit color schemes.

### User Flow & Screens

- The user flow will be designed to facilitate a seamless gameplay experience, guiding players through various stages of the game while emphasizing exploration and discovery. Key components of the user flow include:

  - **In-Game**: Players will navigate through levels, solving puzzles and collecting colors. The user interface will be minimalistic, with the protagonist's shell displaying the collected colors. 

  - **Item Collection**: As players progress through the game, they will collect various items, including UI elements that enhance their gameplay experience. These items may unlock new abilities, grant access to new areas, or reveal hidden story elements. The collected items will be displayed in an appropriate section of the HUD, making it easy for players to keep track of their inventory.

  - **Game Start**: The game will begin immediately upon clicking, without a traditional main menu or level selection screen. This design choice emphasizes the focus on exploration and discovery, allowing players to dive right into the game world and start their journey within the Rubik's Cube.

### Controls & Input Feedback

- The game will provide clear and concise feedback for player inputs, with visual and auditory cues for actions such as collecting colors, switching dimensions, and solving puzzles. This feedback will be consistent across the game's evolving visual styles. 

  - **Movement**: Players will use arrow keys or WASD to move the protagonist. The game will provide responsive visual feedback, with the character smoothly moving in the desired direction and animations of four frames (different pose). Auditory feedback and animations will come along, like when hitting the wall.

  - **Pickups**: Many abilities will unlock with pickups, adding more in game shortcut keys.


### Camera & Perspective

- The camera perspective in Rubik's Evo Portaland will primarily be a 2D side-scrolling view, with occasional top-down perspectives for specific levels and puzzles. The camera will smoothly transition between dimensions and levels, maintaining a clear and consistent view of the gameplay.

  - **Camera Transitions**: As players switch dimensions or move to different levels, the camera will smoothly pan or fade between the scenes, ensuring an uninterrupted gameplay experience.
- **Fake 3D**: In some of the scenes, the player will play in fake 3d.

### UI Elements & Visuals

- The game's UI elements will adhere to the retro pixel art style, with buttons and menus that match the current color scheme. Special modes and features, such as dimension-switching and color-based progression, will be visually represented within the UI to provide clear guidance for the player.

  - **Color Representation**: The protagonist's shell will display the collected colors, serving as a visual indicator of player progress. As new colors are collected, the shell will evolve, showcasing the player's achievements.

  - **Dimension Indicator**: TO FILL (Later pickup)

### Controls Mapping & Settings

- The control scheme for Rubik's Evo Portaland will be simple and intuitive, with keyboard and/or gamepad support. Players will be able to customize their controls through an in-game menu, which will be introduced later in the game as a pickup item.

  - **Video Settings**: Once unlocked, the game's settings menu will allow players to adjust the display from 2 bit to 4 bit and finally 8 bit or 16 bit.

### Loading Screens & Transitions

- Loading screens and transitions will feature artwork and animations that showcase the game's evolving visual style and color schemes. Tips and hints may be displayed during these moments to assist players in their journey through the Rubik's Cube world.

  - **Hints and Tips**: Loading screens may occasionally display context-specific hints or tips, providing players with useful information about the current level or puzzle.

  - **Transition Effects**: The game will utilize visually appealing transition effects, such as fading, sliding, or pixelating, to smoothly switch between different dimensions, levels, or game states. These effects will be designed to complement the game's retro aesthetic and maintain a cohesive visual experience.

---

1. Read the provided information carefully
2. Write the pseudo code with very comprehensive comments for functions, classes, the file, etc. for __class__. All information should be in one .py file.

[Msg2]
Write comprehensive test cases in pytest for it.