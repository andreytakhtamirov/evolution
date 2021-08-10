from ursina import *

from animal import Animal

app = Ursina()

camera.orthographic = True
camera.position = (25, 25)
camera.fov = 80

animals = []
app.set_background_color(color.white50)

for k in range(11):
    animals.append(Animal())


def update():
    for i in range(len(animals)):
        move_dir = random.randint(1, 4)
        move_vel = random.uniform(0.01, 1)

        if move_dir == 1:
            animals[i].entity.x += move_vel
        elif move_dir == 2:
            animals[i].entity.x -= move_vel
        elif move_dir == 3:
            animals[i].entity.y += move_vel
        else:
            animals[i].entity.y -= move_vel

        # Collision
        for j in range(len(animals)):
            if animals[j].entity != animals[i].entity and animals[i].entity.visible and animals[j].entity.visible \
                    and animals[j].entity.intersects(animals[i].entity).hit:
                print(str(i) + " collision with " + str(j))
                if animals[j].entity.scale_x > animals[i].entity.scale_x:
                    # animal j eats i
                    animal_eats_another(animals[j], animals[i])
                else:
                    # animal i eats j
                    animal_eats_another(animals[i], animals[j])
                break


def animal_eats_another(eater, eaten):
    eater.entity.disable()
    eater.entity.collision = False
    eaten.entity.scale_x += eaten.entity.scale_x
    eaten.entity.scale_y += eaten.entity.scale_y
    eaten.entity.animate_color(color.random_color())


app.run()
