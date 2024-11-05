from src.base.object import BaseObject
from src.components.rigidbody import Rigidbody
from src.components.texture import TextureFabric
from src.engine import Engine
from src.utils.vector import Vector2, Rotation

engine = Engine()
scene = engine.scene

obj = BaseObject()
obj.transform.position = Vector2(50, 10)
obj.transform.rotation = Rotation.right

obj.add_component(TextureFabric.load('src/assets/test.tx'))
obj.add_component(Rigidbody())

scene.add(obj)
engine.run()
