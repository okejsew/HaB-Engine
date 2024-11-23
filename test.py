from engine import Engine
from engine.base.cmp.colliders.texture import TextureCollider
from engine.base.cmp.rigidbody import Rigidbody
from engine.base.cmp.texture import Texture
from engine.base.common.vector import Vector2, Rotation
from engine.base.object import Object

obj = Object()
obj.transform.position = Vector2(56, 10)
obj.transform.rotation = Rotation.down

obj2 = Object()
obj2.transform.position = Vector2(50, 20)

obj.add_component(Texture.load('engine/assets/test.tx'))
obj.add_component(Rigidbody())
obj.add_component(TextureCollider())
obj2.add_component(Texture.load('engine/assets/ground.tx'))
obj2.add_component(TextureCollider())

Engine.scene.add(obj)
Engine.scene.add(obj2)
Engine.run()
