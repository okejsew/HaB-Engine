from engine import Engine
from engine.base.cmp.colliders.texture import TextureCollider
from engine.base.cmp.rigidbody import Rigidbody
from engine.base.cmp.texture import Texture
from engine.base.common.vector import Vector2
from engine.base.object import Object

human = Object()
human.add_component(Texture.load('engine/assets/human.tx'))
human.add_component(Rigidbody())
human.add_component(TextureCollider())
human.transform.position = Vector2(50, 5)

ground = Object()
ground.add_component(Texture.load('engine/assets/ground.tx'))
ground.add_component(TextureCollider())
ground.transform.position = Vector2(50, 26)

Engine.scene.add(human)
Engine.scene.add(ground)


def start_example():
    Engine.run()
