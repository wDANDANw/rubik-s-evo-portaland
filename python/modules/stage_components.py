class Component:
    pass

class PositionComponent(Component):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class VelocityComponent(Component):
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

class HitboxComponent(Component):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class DrawableComponent(Component):
    def __init__(self, img, u, v, w, h, colkey):
        self.img = img
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.colkey = colkey

class InputControlComponent(Component):
    pass