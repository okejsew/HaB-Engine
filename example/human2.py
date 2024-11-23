from engine import Engine
from engine.base.cmp.rigidbody import Rigidbody
from engine.base.cmp.texture import Texture
from engine.base.common.vector import Vector2
from engine.base.object import Object

human = Object()
human.add_component(Texture.load('engine/assets/human.tx'))
human.add_component(Rigidbody())
human.transform.position = Vector2(50, 2)

Engine.scene.add(human)


def start_example():
    Engine.run()
