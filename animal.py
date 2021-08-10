from ursina import *


class Animal:
    def __init__(self):
        self.speed_x = random.uniform(1, 100)
        self.speed_y = random.uniform(1, 100)
        self.strength = random.uniform(1, 100)
        self.swim = random.uniform(1, 100)
        self.max_uv_exposure = random.uniform(1, 100)
        self.size_x = random.uniform(1, 4)
        self.size_y = random.uniform(1, 4)
        self.entity = Entity(model='cube', color=color.random_color(), scale_x=self.size_x, scale_y=self.size_x,
                             position=(random.uniform(0, 50), random.uniform(0, 50), 0),
                             collider='box')
