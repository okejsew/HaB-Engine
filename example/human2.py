from engine import Engine
from engine.base.object import Object
from engine.common.vector import Vector2
from engine.components.rigidbody import Rigidbody
from engine.components.texture import Texture

human = Object()
human.add_component(Texture.load('engine/assets/human.tx'))
human.add_component(Rigidbody())
human.transform.position = Vector2(50, 2)

Engine.scene.add(human)


def start_example():
    Engine.run()
