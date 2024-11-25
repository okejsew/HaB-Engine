from typing import Optional

from engine.base.object import Object
from engine.base.scene import Scene
from engine.components.texture import Texture
from engine.tools.console import set_point, Console


class RenderCore:
    scene: Optional[Scene] = None

    @staticmethod
    def setup(scene: Scene):
        RenderCore.scene = scene
        Console.register(RenderCore.render)

    @staticmethod
    def render():
        RenderCore.scene.camera.update()
        for obj in RenderCore.scene:
            if not obj.visible:
                continue
            RenderCore.render_object(obj)

    @staticmethod
    def render_object(obj: Object):
        texture = obj.get_component(Texture)
        if not texture: return
        for point in texture.get():
            if not RenderCore.scene.camera.in_region(point):
                continue
            set_point(point.offset - RenderCore.scene.camera.region[0], point.sign)
