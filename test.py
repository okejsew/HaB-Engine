from src.assets.objects.pospoint import PositionPoint
from src.components.rigidbody import Rigidbody
from src.utils.vector import Vector2
from src.base.scene import Scene
from src.engine import Engine


scene = Scene()
Engine.set_scene(scene)
Engine.debug_mode = True
r = PositionPoint()
r.transform.position = Vector2(10, 10)
r.add_component(Rigidbody())
scene.add(r)
Engine.run()


# while True:
#     rect = Rectangle(1, 1, '*')
#     rect.transform.position = Vector2(randint(1, 119), randint(-5, -1))
#     rect.add_component(Rigidbody())
#     rect.get_component(Rigidbody).mass = randint(1, 100) / 10
#     rect.get_component(Rigidbody).max_fall_speed = 100
#     scene.add(rect)
#     sleep(3)
