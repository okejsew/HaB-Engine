input('Press enter to start')
from random import randint
from time import sleep
from src.assets.objects.rectangle import Rectangle
from src.components.rigidbody import Rigidbody
from src.utils.vector import Vector2
from src.base.scene import Scene
from src.engine import Engine


scene = Scene()
Engine.debug_mode = True
Engine.set_scene(scene)
Engine.run()


while True:
    rect = Rectangle(1, 1, '*')
    rect.transform.position = Vector2(randint(1, 173), randint(-50, -1))
    rect.add_component(Rigidbody())
    rect.get_component(Rigidbody).mass = 0.1
    scene.add(rect)
    sleep(0.05)
