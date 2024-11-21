from engine.api import *


class CustomScript(Script):
    def __init__(self):
        super().__init__()

    def update(self):
        key = Input.get_key()
        if key == ord('d'):
            self.owner.transform.position.x += 1
        elif key == ord('a'):
            self.owner.transform.position.x -= 1
        if key == ord('w'):
            self.owner.transform.position.y -= 1
        if key == ord('s'):
            self.owner.transform.position.y += 1

engine = Engine()
scene = engine.scene

obj = Object()
obj.transform.position = Vector2(50, 10)
obj.transform.rotation = Rotation.right

obj.add_component(Texture.load('engine/assets/test.tx'))
# obj.add_component(Rigidbody())
obj.add_component(CustomScript())

scene.add(obj)
engine.run()
