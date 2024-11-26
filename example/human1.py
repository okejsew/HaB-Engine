from engine import *

human = Object()
human.add_component(Texture.load('engine/assets/human.tx'))
human.transform.position = Vector2(50, 26)

ground = Object()
ground.add_component(Texture.load('engine/assets/ground.tx'))
ground.transform.position = Vector2(50, 28)

Application.add(human)
Application.add(ground)


def start_example():
    Application.run()
