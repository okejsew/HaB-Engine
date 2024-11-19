from src.api import *


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

obj = Object()
obj.transform.position = Vector2(50, 10)
obj.transform.rotation = Rotation.right

obj.add_component(Texture.load('src/assets/test.tx'))
obj.add_component(Rigidbody())
obj.add_component(CustomScript())

scene.add(obj)
engine.run()
