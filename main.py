from ursina import *
from animal import Animal

app = Ursina()
app.set_background_color(color.white50)

camera.orthographic = True
camera.position = (25, 25)
camera.fov = 80

animals = []

for k in range(11):
    animals.append(Animal())


def update():
    for i in range(len(animals)):
        perform_movement(animals[i])
        handle_animal_collisions(animals[i], animals)


def perform_movement(animal_to_move):
    move_dir = random.randint(1, 4)
    move_vel = random.uniform(0.01, 0.7)

    if move_dir == 1:
        animal_to_move.entity.x += move_vel
    elif move_dir == 2:
        animal_to_move.entity.x -= move_vel
    elif move_dir == 3:
        animal_to_move.entity.y += move_vel
    else:
        animal_to_move.entity.y -= move_vel


def handle_animal_collisions(animal, arr_of_animals):
    # Check collisions between animals, smaller animals will be eaten by larger animals
    for j in range(len(arr_of_animals)):
        if arr_of_animals[j].entity != animal.entity and arr_of_animals[j].entity.intersects(animal.entity).hit:
            if arr_of_animals[j].entity.scale_x > animal.entity.scale_x:
                # animal j eats i
                animal_eats_another(arr_of_animals[j], animal)
            else:
                # animal i eats j
                animal_eats_another(animal, arr_of_animals[j])
            break


def animal_eats_another(eater, eaten):
    eaten.entity.disable()
    eaten.entity.collision = False
    eater.entity.scale_x += eaten.entity.scale_x
    eater.entity.scale_y += eaten.entity.scale_y
    eater.entity.animate_color(color.random_color())


app.run()
