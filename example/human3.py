from engine import Engine
from engine.base.object import Object
from engine.common.vector import Vector2
from engine.components.rigidbody import Rigidbody
from engine.components.texture import Texture

human = Object()
human.add_component(Texture.load('engine/assets/human.tx'))
human.add_component(Rigidbody())
human.transform.position = Vector2(50, 5)

ground = Object()
ground.add_component(Texture.load('engine/assets/ground.tx'))
ground.add_component(Rigidbody())
ground.get_component(Rigidbody).gravity = 0.5
ground.transform.position = Vector2(50, 8)

Engine.scene.add(human)
Engine.scene.add(ground)


def start_example():
    Engine.run()
