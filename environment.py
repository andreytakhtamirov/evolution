import random

from ursina import Entity, color

# WINDOW DIMENSIONS
WINDOW_X = 0
WINDOW_Y = 0


class Water:
    def __init__(self):
        self.size = random.uniform(1, 10)
        self.depth = random.uniform(1, 100)
        self.entity = Entity(model='cube', color=color.hex("#5583AD"), scale_y=self.size, scale_x=self.size,
                             position=(random.uniform(-WINDOW_X, WINDOW_X), random.uniform(-WINDOW_Y, WINDOW_Y), 0),
                             collider='box')

    def get_colour_from_depth(self):
        decimal = 40000 + self.depth * 60000
        return '#' + str(decimal)


class Food:
    def __init__(self):
        self.size = random.uniform(0.5, 3)
        self.nutrition = self.size
        self.entity = Entity(model='sphere', color=color.hex("#8BAA8B"), scale_y=self.size, scale_x=self.size,
                             position=(random.uniform(-WINDOW_X, WINDOW_X), random.uniform(-WINDOW_Y, WINDOW_Y), 0), collider='box')


class Sun:
    def __init__(self):
        entity = Entity(model='sphere', color=color.yellow)
        heat = random.uniform(1, 1000)
        uv = random.uniform(1, 1000)


class Terrain:
    def __init__(self):
        mountain = Entity(model='pyramid', color=color.green, scale_y=0.1, scale_x=0.1)
        forest = Entity(model='cylinder', color=color.green)
        rock = Entity(model='cube', color=color.gray)
        shrooms = Entity(model='circle', color=color.gray)
        grass = Entity(model='square', color=color.green)
        fire = Entity(model='triangle', color=color.red)


class Disease:
    def __init__(self):
        malaria = random.uniform(1, 100)
        typhus = random.uniform(1, 100)
        bubonic_plague = random.uniform(1, 100)
