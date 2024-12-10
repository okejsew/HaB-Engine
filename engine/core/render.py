from engine.base.scene import Scene
from engine.base.components import Texture
import engine.tools.console as console
from engine.math import Vector2

scene: Scene | None


def __init__(_scene: Scene):
    global scene
    scene = _scene
    console.register(render)

def render():
    scene.camera.update()
    for txt in scene.get_components(Texture):
        if txt.owner.visible:
            render_object(txt)

def render_object(txt: Texture):
    camera_offset = scene.camera.region[0]
    for point in txt.get():
        vec = point.vec - camera_offset
        if scene.camera.in_region(point):
            console.addch(vec.y, vec.x, point.sign)

