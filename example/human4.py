from engine import *

human = Object()
human.add_component(Texture.load('engine/assets/human.tx'))
human.add_component(Rigidbody())
human.add_component(TextureCollider())
human.transform.position = Vector2(50, 5)

ground = Object()
ground.add_component(Texture.load('engine/assets/ground.tx'))
ground.add_component(TextureCollider())
ground.transform.position = Vector2(50, 26)

Application.add(human)
Application.add(ground)


def start_example():
    Application.run()
