import random

from ursina import Entity, color


class Water:
    def __init__(self):
        self.entity = Entity(model='cube', color=color.blue, scale_y=0.1, scale_x=0.1)
        self.size = random.uniform(1, 100)
        self.depth = random.uniform(1, 100)

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

