import pyxel
import logging
import re

logging.basicConfig(filename="output.log", level=logging.DEBUG)

def parse_sprite_data(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    all_sprite_data = []
    sprite_data = None
    read_rows = 0
    width = None
    height = None

    for line in lines:
        line = line.strip().lower()

        # Read width and height if not already read
        if len(line) < 1:
            continue
        
        elif width is None:
            match = re.search(r'width\s*=\s*(\d+)', line)
            if match:
                width = int(match.group(1))

        elif height is None:
            match = re.search(r'height\s*=\s*(\d+)', line)
            if match:
                height = int(match.group(1))
                

        elif line.startswith("# frame"):

            read_rows = 0

            if sprite_data is None:
                sprite_data = []

            if len(sprite_data) > 1:  # Save the previous frame data if any
                if len(sprite_data) == height:
                    all_sprite_data.append(sprite_data)
                else:
                    print(f"Error: Sprite Data Wrong Length. Expected {height}, Actual: {len(sprite_data)} ")
                    logging.error("Error: Sprite Data Wrong Length")
                    return []

            # Check if width and height are read
            if width is None or height is None:
                print("Width or height not specified in the file.")
                logging.error("Width or height not specified in the file.")
                return []

            if sprite_data:  # Save the previous frame data if any
                all_sprite_data.append(sprite_data)
                sprite_data = []

            read_rows = 0
          
        elif height is not None and read_rows != -1 and read_rows < height:
            row_data = [int(x) for x in re.split(r'\s+', line) if x]
            sprite_data.append(row_data)
            read_rows += 1

            if read_rows == height:
                read_rows = -1

    if sprite_data:  # Save the previous frame data if any
        all_sprite_data.append(sprite_data)
        sprite_data = []

    print("Data:", all_sprite_data)
    return all_sprite_data

def pretty_print_sprite(sprite_data):
    for row in sprite_data:
        row_str = " ".join(str(x) for x in row)
        print(row_str)


def update_image_bank(image_bank, sprite_data):
    for y, row in enumerate(sprite_data):
        for x, color in enumerate(row):
            image_bank.pset(x, y, color)

pyxel.init(8, 8)
image_bank = pyxel.image(1)

sprites = parse_sprite_data("./egg_1.txt")
pretty_print_sprite(sprites[0])
update_image_bank(image_bank, sprites[0])
pyxel.save("test.pyxres")





# class App:
#     def __init__(self):
#         pyxel.init(160, 120, title="Hello Pyxel")
#         pyxel.load("assets/jump_game.pyxres")

#         image_bank = pyxel.image(0)
#         # print([hex(x) for x in pyxel.colors.to_list()])

#         # Get the image dimensions (width and height)
#         image_width = image_bank.width
#         image_height = image_bank.height

#         # Loop through the image's pixels and print their color values
#         # with open ("test.txt", "r") as f:
#         #     for y in range(16):
#         #         for x in range(16):
#         #             pixel_color = image_bank.pget(x, y)
                    
#         #             f.write(f"{pixel_color} ")
#         #         f.write("\n") # Start a new line for the next row of pixels

#         with open ("test.txt", "r") as f:
#             for x in range(8):
#                 for y in range (8):
#                     pixel_color = 
#         pyxel.run(self.update, self.draw)


#     def update(self):
#         if pyxel.btnp(pyxel.KEY_Q):
#             pyxel.quit()

#     def draw(self):
#         pyxel.cls(0)
#         pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
#         pyxel.blt(61, 66, 0, 0, 0, 8, 8)


# App()
