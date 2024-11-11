from src.base.object import BaseObject
from src.components.script import Script
from src.components.texture import TextureFabric
from src.engine import Engine
from src.utils.time import Time
from src.utils.vector import Vector2, Rotation, Vector2F


class CustomScript(Script):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.tick = 0

    def update(self):
        self.owner.transform.translate(Vector2F(self.speed * Time.delta, 0))
        self.tick += 1
        if self.tick % 1500 == 0:
            self.owner.transform.rotate_left()


engine = Engine()
scene = engine.scene

obj = BaseObject()
obj.transform.position = Vector2(50, 10)
obj.transform.rotation = Rotation.right

obj.add_component(TextureFabric.load('src/assets/test.tx'))
# obj.add_component(Rigidbody())
obj.add_component(CustomScript())

scene.add(obj)
engine.run()
