from typing import Optional

from engine.base.cmp.texture import Texture
from engine.base.object import Object
from engine.base.scene import Scene
from engine.tools.console import set_point, Console


class Renderer:
    scene: Optional[Scene] = None

    @staticmethod
    def setup():
        from engine import Engine
        Renderer.scene = Engine.scene
        Console.register(Renderer.render_objects)

    @staticmethod
    def render_objects():
        Renderer.scene.camera.update()
        for obj in Renderer.scene:
            if not obj.visible:
                continue
            Renderer.render_object(obj)

    @staticmethod
    def render_object(obj: Object):
        texture = obj.get_component(Texture)
        if not texture: return
        for point in texture.get():
            if not Renderer.scene.camera.in_region(point):
                continue
            set_point(point.offset - Renderer.scene.camera.region[0], point.sign)
