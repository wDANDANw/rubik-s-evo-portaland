
import math
import pyxel

from typing import Dict, Any

from modules.base_level import BaseLevel
from modules.level_manager import LevelManager

from modules.globals import *

INTERLEAVE_RENDERING = True



DEFAULT_FOV = math.pi / 4
DEFAULT_DEPTH = 16

# MAP_WIDTH = 16
# MAP_HEIGHT = 16
# MAP_1 = """
# ################
# #..............#
# #..#....######.#
# #..............#
# #..............#
# #......##......#
# #......##......#
# #..............#
# ###....#####...#
# ##.............#
# #..............#
# #........###.###
# #........#.....#
# #..............#
# #........#.....#
# ################
# """

MAP_WIDTH = 5
MAP_HEIGHT = 16
MAP_SCALE = 2.5
MAP_2 = """
#...#
#...#
#...#
#...#
#...#
#...#
#...#
#...#
#...#
#...#
#...#
#...#
#...#
#...#
#...#
#####
"""

class Level_0(BaseLevel):
    def __init__(self):
        super().__init__(0, {})

    def load(self):
        # Load resources and set up the initial game state for level 1
        # pyxel.load("assets/level_1.pyxres")
        # ... other level-specific loading and game state setup
        
        # Player staring position and angle
        self.attempted = 0
        self.player_x = 2.5
        self.player_y = 12
        self.player_a = 3
        self.fov = DEFAULT_FOV
        self.depth = DEFAULT_DEPTH
        # Walking speed
        self.speed = 0.2
        # Load the world map
        self.world_map = MAP_2[1:-1].split("\n")

        self.tp1 = pyxel.frame_count
        self.tp2 = pyxel.frame_count
        self.interleave = INTERLEAVE_RENDERING
        self.render_alt = True
        self.player_run = False
        self.v_look = 0
        self.show_map = True
        self.show_boundries = True

        self.play_music(self.attempted)

    def update(self):
        # Update the level state based on the elapsed time since the last frame
        # ... level-specific update logic
                # Compute elapsed time
        
        self.tp2 = pyxel.frame_count
        ellapsed_time = self.tp2 - self.tp1
        self.tp1 = self.tp2

        # if self.attempted > 0:
        #     if (pyxel.mouse_x < SCREEN_WIDTH/2 - 30):
        #         mouse_move = -1 
        #     elif (pyxel.mouse_x > SCREEN_WIDTH/2 + 30):
        #         mouse_move = 1
        #     else:
        #         mouse_move = 0
        # else:
        #     mouse_move = 0


        # Handle player input
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        # Determine player speed
        if pyxel.btnp(pyxel.KEY_SHIFT):
            self.player_run = True
        if pyxel.btnr(pyxel.KEY_SHIFT):
            self.player_run = False
        if self.player_run:
            speed = self.speed
        else:
            speed = self.speed / 3

        if pyxel.btn(pyxel.KEY_W):
            self.move_forward(speed, ellapsed_time)
        if pyxel.btn(pyxel.KEY_S):
            self.move_backward(speed, ellapsed_time)
        if pyxel.btn(pyxel.KEY_A):
            self.player_a -= 0.04 * ellapsed_time
        if pyxel.btn(pyxel.KEY_D):
            self.player_a += 0.04 * ellapsed_time            
        if pyxel.btn(pyxel.KEY_Z):
            self.move_left(speed, ellapsed_time)
        if pyxel.btn(pyxel.KEY_C):
            self.move_right(speed, ellapsed_time)

        if self.player_a > 4.5: 
            self.player_a = 1.5
            self.increment_attempted()
        elif self.player_a < 1.5:
            self.player_a = 4.5
            self.increment_attempted()

        if pyxel.btnp(pyxel.KEY_P):
            print(f"x: {self.player_x}, ", end="")
            print(f"y: {self.player_y}, ", end="")
            print(f"a: {self.player_a}")

        if pyxel.btn(pyxel.KEY_1):
            self.fov += 0.01
        if pyxel.btn(pyxel.KEY_2):
            self.fov -= 0.01
        if pyxel.btn(pyxel.KEY_3):
            self.fov = DEFAULT_FOV
        if pyxel.btnp(pyxel.KEY_4):
            self.interleave = not self.interleave
        if pyxel.btn(pyxel.KEY_5):
            self.depth += 1
        if pyxel.btn(pyxel.KEY_6):
            self.depth -= 1
        if pyxel.btn(pyxel.KEY_7):
            self.depth = DEFAULT_DEPTH
        if pyxel.btnp(pyxel.KEY_8):
            self.show_boundries = not self.show_boundries

        if pyxel.btn(pyxel.KEY_Q):
            self.v_look += 1
        if pyxel.btn(pyxel.KEY_E):
            self.v_look -= 1
        if pyxel.btn(pyxel.KEY_X):
            self.v_look = 0

        if pyxel.btnp(pyxel.KEY_M):
            self.show_map = not self.show_map

    def render(self):
        # Render the level, including entities and UI elements
        # ... level-specific rendering logic

        if self.interleave:
            inc = 2
            start = 0
            if self.render_alt:
                start = 1
            self.render_alt = not self.render_alt
        else:
            pyxel.cls(0)
            start = 0
            inc = 1

        for x in range(start, SCREEN_WIDTH, inc):

            dist_to_wall, boundary = self.cast_ray(x)

            if dist_to_wall == 0:
                dist_to_wall = 0.0001

            # Calculate distance to ceiling and floor
            ceiling = SCREEN_HEIGHT / 2 - SCREEN_HEIGHT / dist_to_wall
            floor = SCREEN_HEIGHT - ceiling

            # Modify the ceiling and floor for the vertical look position
            ceiling += self.v_look
            floor += self.v_look
            shade = 0

            for y in range(SCREEN_HEIGHT):
                if y < ceiling:
                    shade = 6 # ceiling shade
                elif y > ceiling and y <= floor:
                    shade = self.compute_wall_shade(x, y, dist_to_wall, boundary)
                else:
                    shade = self.compute_floor_shade(x, y)
                pyxel.image(1).pset(x, y, shade)

        # Blt the screen from the image bank being used as the display buffer
        pyxel.blt(0, 0, 1, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        # Draw map
        if self.show_map:
            w = MAP_WIDTH / MAP_SCALE
            h = MAP_HEIGHT / MAP_SCALE
            startx = 0
            starty = SCREEN_HEIGHT - MAP_HEIGHT * w
            for nx in range(MAP_WIDTH):
                for ny in range(MAP_HEIGHT):
                    cell = self.world_map[ny][nx]
                    if cell == "#":
                        col = 6
                    else:
                        col = 7
                    pyxel.rect(w * nx + startx, h * ny + starty, w, h, col)
            px = int(self.player_x)
            py = int(self.player_y)
            pyxel.rect(w * px + startx, w * py + starty, w, w, 12)

    def unload(self):
        # Unload the level resources and clean up the game state for level 1
        # ... level-specific resource unloading and game state cleanup
        pass


    def cast_ray(self, x):
        # https://www.youtube.com/watch?v=NbSee-XM7WA
        # https://lodev.org/cgtutor/raycasting.html

        ray_start_x = self.player_x
        ray_start_y = self.player_y

        ray_angle = (self.player_a - self.fov / 2) + (x / SCREEN_WIDTH) * self.fov
        ray_dir_x = math.sin(ray_angle)
        ray_dir_y = math.cos(ray_angle)

        ray_unit_step_x = math.sqrt(
            1 + (ray_dir_y / ray_dir_x) * (ray_dir_y / ray_dir_x)
        )
        ray_unit_step_y = math.sqrt(
            1 + (ray_dir_x / ray_dir_y) * (ray_dir_x / ray_dir_y)
        )

        map_check_x = int(ray_start_x)
        map_check_y = int(ray_start_y)

        ray_len_x = 0
        ray_len_y = 0

        step_x = 0
        step_y = 0

        if ray_dir_x < 0:
            step_x = -1
            ray_len_x = (ray_start_x - float(map_check_x)) * ray_unit_step_x
        else:
            step_x = 1
            ray_len_x = (float(map_check_x + 1) - ray_start_x) * ray_unit_step_x

        if ray_dir_y < 0:
            step_y = -1
            ray_len_y = (ray_start_y - float(map_check_y)) * ray_unit_step_y
        else:
            step_y = 1
            ray_len_y = (float(map_check_y + 1) - ray_start_y) * ray_unit_step_y

        tile_found = False
        max_dist = 64.0
        dist = 0.0
        boundary = False

        while not tile_found and dist < max_dist:

            if ray_len_x < ray_len_y:
                map_check_x += step_x
                dist = ray_len_x
                ray_len_x += ray_unit_step_x
            else:
                map_check_y += step_y
                dist = ray_len_y
                ray_len_y += ray_unit_step_y

            if self.check_collision(map_check_x, map_check_y):

                tile_found = True

                if self.show_boundries:
                    # Cast rays from each corner of the wall to find the boundaries
                    p = []
                    for tx in range(2):
                        for ty in range(2):
                            vy = map_check_y + ty - self.player_y
                            vx = map_check_x + tx - self.player_x                            
                            d = math.sqrt(vx * vx + vy * vy)
                            if (d == 0):
                                continue; 

                            dot = (ray_dir_x * vx / d) + (ray_dir_y * vy / d)
                            p.append((d, dot))
                    # Sort the pairs to find the closest
                    p.sort()
                    # Looking for very small angles with closest corners
                    bound = 0.01
                    if math.acos(p[0][1]) < bound:
                        boundary = True
                    if math.acos(p[1][1]) < bound:
                        boundary = True

        return dist, boundary

    def compute_wall_shade(self, x, y, dist_to_wall, boundary=False):
        if dist_to_wall <= self.depth / 7:
            shade = 7
        elif dist_to_wall < self.depth / 6:
            if x % 2:
                shade = 6 if y % 2 else 13
            else:
                shade = 13 if y % 2 else 6
        elif dist_to_wall < self.depth / 5:
            shade = 13
        elif dist_to_wall < self.depth / 4:
            if x % 2:
                shade = 13 if y % 2 else 1
            else:
                shade = 1 if y % 2 else 13
        elif dist_to_wall < self.depth / 3:
            shade = 1
        elif dist_to_wall < self.depth / 2:
            if x % 2:
                shade = 1 if y % 2 else 0
            else:
                shade = 0 if y % 2 else 1
        elif dist_to_wall < self.depth:
            shade = 0
        if self.show_boundries and boundary:
            shade = 0
        return shade

    def compute_floor_shade(self, x, y):
        # v_look changes where the floor starts rendering
        b = 1 - (y - self.v_look - SCREEN_HEIGHT / 2) / (SCREEN_HEIGHT / 2)
        if b < 0.25:
            shade = 15
        elif b < 0.5:
            if x % 2:
                shade = 15 if y % 2 else 10
            else:
                shade = 15 if y % 2 else 15
        elif b < 0.75:
            shade = 9
        elif b < 0.9:
            if x % 2:
                shade = 9 if y % 2 else 0
            else:
                shade = 0 if y % 2 else 9
        else:
            shade = 0
        return shade

    def move_forward(self, speed, time_delta):
        new_x = self.player_x + math.sin(self.player_a) * speed * time_delta
        new_y = self.player_y + math.cos(self.player_a) * speed * time_delta

        if new_y < 6.5:
            new_y = 12.5
            self.increment_attempted()

        if not self.check_collision(new_x, new_y):
            self.player_x = new_x
            self.player_y = new_y

    def move_backward(self, speed, time_delta):
        new_x = self.player_x - math.sin(self.player_a) * speed * time_delta
        new_y = self.player_y - math.cos(self.player_a) * speed * time_delta
        if not self.check_collision(new_x, new_y):
            self.player_x = new_x
            self.player_y = new_y

    def move_left(self, speed, time_delta):
        new_x = (
            self.player_x + math.sin(self.player_a - math.pi / 2) * speed * time_delta
        )
        new_y = (
            self.player_y + math.cos(self.player_a - math.pi / 2) * speed * time_delta
        )
        if not self.check_collision(new_x, new_y):
            self.player_x = new_x
            self.player_y = new_y

    def move_right(self, speed, time_delta):
        new_x = (
            self.player_x + math.sin(self.player_a + math.pi / 2) * speed * time_delta
        )
        new_y = (
            self.player_y + math.cos(self.player_a + math.pi / 2) * speed * time_delta
        )
        if not self.check_collision(new_x, new_y):
            self.player_x = new_x
            self.player_y = new_y

    def check_collision(self, x, y):
        if (x < 0 or x >= MAP_WIDTH) or (y < 0 or y >= MAP_HEIGHT):
            return True
        return self.world_map[int(y)][int(x)] == "#"
    
    def play_music(self, attempted):
        if attempted < 1:
            self._play_starting_music(45, 0)
        elif attempted < 2:
            self._play_starting_music(35, 45)
        elif attempted < 3:
            self._play_starting_music(25, 35)
        elif attempted < 4:
            self._play_weird_music()
        else:
            self._play_dropped()
            LevelManager.get_instance().load_level(1)
            
            

    def increment_attempted(self):
        self.attempted += 1
        self.play_music(self.attempted)

    def _play_starting_music(self, speed, prev_speed):
        pyxel.sound(35).speed = speed
        pyxel.sound(36).speed = speed
        pyxel.sound(37).speed = speed

        if prev_speed == 0:
            tick = 0
        else:
            seconds = float(pyxel.frame_count / FPS)
            sound_notes_in_one_sec = 120 / prev_speed
            tick = int(seconds * sound_notes_in_one_sec % 16)

        pyxel.play(0, 35, tick=tick, loop=True)
        pyxel.play(1, 36, tick=tick, loop=True)
        pyxel.play(2, 37, tick=tick, loop=True)

    def _play_weird_music(self):
        pyxel.playm(2)

    def _play_dropped(self):
        pyxel.stop()
        pyxel.play(0, [38, 39])