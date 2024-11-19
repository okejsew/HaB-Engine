from src.base.object import BaseObject
from src.components.script import Script
from src.components.texture import TextureFabric
from src.engine import Engine
from src.utils.input import Input
from src.utils.vector import Vector2, Rotation


class CustomScript(Script):
    def __init__(self):
        super().__init__()

    def update(self):
        key = Input.get_key()
        if key == ord('d'):
            self.owner.transform.rotate_right()
        elif key == ord('a'):
            self.owner.transform.rotate_left()
        if key == ord('w'):
            self.owner.transform.translate(self.owner.transform.rotation.value)


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
