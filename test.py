from engine.api import *
from engine.base.cmp.collider import Collider
from engine.base.cmp.colliders.texture import TextureCollider
from engine.base.common.vector import Vector2F
from engine.tools.debug import Debug


class CustomScript(Script):
    def __init__(self):
        super().__init__()

    def update(self):
        key = Input.get_key()
        if key == ord('d'):
            self.owner.transform.translateX(1)
        elif key == ord('a'):
            self.owner.transform.translateX(-1)
        if key == ord('w'):
            self.owner.get_component(Rigidbody).add_force(Vector2F(0, -100))
        if key == ord('s'):
            self.owner.transform.translateY(1)
        if key == ord(' '):
            self.owner.get_component(Collider).calculate()
            Debug.log('collisions', f'Колизий: {len(self.owner.get_component(Collider).collisions)}')


engine = Engine()
scene = engine.scene

obj = Object()
obj.transform.position = Vector2(50, 10)
obj.transform.rotation = Rotation.down

obj2 = Object()
obj2.transform.position = Vector2(50, 20)

obj.add_component(Texture.load('engine/assets/ground.tx'))
obj.add_component(TextureCollider())
obj.add_component(Rigidbody())
obj.add_component(CustomScript())
obj2.add_component(Texture.load('engine/assets/ground.tx'))
obj2.add_component(TextureCollider())

scene.add(obj)
scene.add(obj2)
engine.run()
