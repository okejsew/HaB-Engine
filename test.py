from src.base.object import BaseObject
from src.base.scene import Scene
from src.components.rigidbody import Rigidbody
from src.components.texture import TextureFabric
from src.engine import Engine
from src.utils.vector import Vector2, Rotation


scene = Scene()
Engine.current_scene = scene

obj = BaseObject()
obj.transform.position = Vector2(50, 10)
obj.transform.rotation = Rotation.down

obj.add_component(TextureFabric.load('src/assets/test.tx'))
obj.add_component(Rigidbody())

scene.add(obj)
Engine.run()
