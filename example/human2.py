from engine import *

human = Object()
human.add_component(Texture.load('engine/assets/human.tx'))
human.add_component(Rigidbody())
human.transform.position = Vector2(50, 2)

Application.add(human)


def start_example():
    Application.run()
