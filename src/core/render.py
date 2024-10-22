import curses
import time

from src.components.texture import Texture
from src.base.errors import ComponentNotFound
from src.base.object import BaseObject
from src.base.scene import Scene
from src.utils.console import window


class RenderCore:
    update_time: float = time.time()

    @staticmethod
    def clear():
        window.clear()

    @staticmethod
    def refresh():
        window.refresh()

    @staticmethod
    def print(y: int, x: int, info: str):
        window.addstr(y, x, info)

    @staticmethod
    def draw_objects(scene: Scene):
        start_time = time.time()
        visible_objects = [obj for obj in scene.objects if obj.visible]
        objs_to_draw = []
        for obj in visible_objects:
            try: obj.get_component(Texture)
            except ComponentNotFound: continue
            else: objs_to_draw.append(obj)
        for obj in objs_to_draw:
            RenderCore.__draw_object(obj)
        RenderCore.update_time = time.time() - start_time


    @staticmethod
    def __draw_object(obj: BaseObject):
        texture = obj.get_component(Texture)
        for point in texture.get():
            pos = obj.transform.position + point.offset
            try:
                window.addch(pos.y, pos.x, point.sign)
            except curses.error:
                continue
