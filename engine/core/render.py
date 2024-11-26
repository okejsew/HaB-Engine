from typing import Optional

from engine.base.scene import Scene
from engine.components.texture import Texture
from engine.main import Engine
from engine.tools.console import set_point, Console
from engine.tools.debug import Debug


class RenderCore:
    scene: Optional[Scene] = None

    @staticmethod
    def setup():
        RenderCore.scene = Engine.scene
        Console.register(RenderCore.render)
        if Engine.debug_mode:
            Console.register(Debug.render)

    @staticmethod
    def render():
        RenderCore.scene.camera.update()
        for txt in RenderCore.scene.get_components(Texture):
            if txt.owner.visible:
                RenderCore.render_object(txt)

    @staticmethod
    def render_object(txt: Texture):
        camera_offset = RenderCore.scene.camera.region[0]
        for point in txt.get():
            if RenderCore.scene.camera.in_region(point):
                set_point(point.offset - camera_offset, point.sign)
