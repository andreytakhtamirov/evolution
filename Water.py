import random

from ursina import Entity, color


class water:
    entity = Entity(model='cube', color=color.blue, scale_y=0.1, scale_x=0.1)
    size = random.uniform(1,100)
    depth = random.uniform(1,100)

class sun:
    entity = Entity(model='sphere', color=color.yellow)
    heat = random.uniform(1,1000)
    uv = random.uniform(1,1000)

class terrain:
    mountain = Entity(model='pyramid', color=color.green, scale_y=0.1, scale_x=0.1)
    forest = Entity(model='cylinder',color=color.green)
    rock = Entity(model='cube',color=color.gray)
    shrooms = Entity(model='circle',color=color.gray)
    grass = Entity(model='square',color=color.green)
    fire = Entity(model='triangle',color=color.red)

class disease:
    malaria = random.uniform(1,100)
    typhus = random.uniform(1,100)
    bubonic_plague = random.uniform(1,100)