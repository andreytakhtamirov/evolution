from ursina import *
import environment


class Animal:
    def __init__(self):
        self.speed_x = random.uniform(1, 100)
        self.speed_y = random.uniform(1, 100)
        self.strength = random.uniform(1, 100)
        self.swim = random.uniform(1, 100)
        self.max_uv_exposure = random.uniform(1, 100)
        self.size_x = random.uniform(1, 4)
        self.size_y = random.uniform(1, 4)
        self.entity = Entity(model='cube', color=color.hex("FFF000"),
                             scale_x=self.size_x, scale_y=self.size_x,
                             position=(random.uniform(-environment.WINDOW_X, environment.WINDOW_X),
                                       random.uniform(-environment.WINDOW_Y, environment.WINDOW_Y),
                                       0),
                             collider='box')

    def get_colour_from_size(self):
        decimal = 70000 + self.entity.scale_x * 65536
        return '#' + str(decimal)
