from engine import Engine
from engine.base.object import Object
from engine.common.vector import Vector2
from engine.components.texture import Texture

human = Object()
human.add_component(Texture.load('engine/assets/human.tx'))
human.transform.position = Vector2(50, 26)

ground = Object()
ground.add_component(Texture.load('engine/assets/ground.tx'))
ground.transform.position = Vector2(50, 28)

Engine.scene.add(human)
Engine.scene.add(ground)


def start_example():
    Engine.run()
