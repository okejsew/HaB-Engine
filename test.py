from src.assets.objects.pospoint import PositionPoint
from src.assets.scripts.test_script import TestScript
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
r.add_component(TestScript())
scene.add(r)
Engine.run()
