from src.assets.objects.pospoint import PositionPoint
from src.components.rigidbody import Rigidbody
from src.utils.vector import Vector2
from src.base.scene import Scene
from src.engine import Engine


scene = Scene()
Engine.current_scene = scene
Engine.debug_mode = True
r = PositionPoint()
r.position = Vector2(10, 10)
r.add_component(Rigidbody())
rb = r.get_component(Rigidbody)
scene.add(r)
Engine.run()
