from ursina import *


class Animal:
    speed_x = 0
    speed_y = 0
    strength = 0
    swim = 0
    max_uv_exposure = 0
    size_x = 0
    size_y = 0
    entity = None

    def __init__(self):
        self.speed_x = random.uniform(1, 100)
        self.speed_y = random.uniform(1, 100)
        self.strength = random.uniform(1, 100)
        self.swim = random.uniform(1, 100)
        self.max_uv_exposure = random.uniform(1, 100)
        self.size_x = random.uniform(0.01, 1)
        self.size_y = random.uniform(0.01, 1)
        self.entity = Entity(model='cube', color=color.orange, scale_x=self.size_x, scale_y=self.size_x, texture="white_cube")
