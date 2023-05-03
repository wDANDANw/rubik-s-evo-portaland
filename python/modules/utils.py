import pyxel

def to_snake_case(name):
    snake_case = ''
    for index, char in enumerate(name):
        if char.isupper() and index > 0:
            snake_case += '_'
        snake_case += char.lower()
    return snake_case

def get_tile(tile_x, tile_y, tm=0):
    return pyxel.tilemap(tm).pget(tile_x, tile_y)