import curses
import time

from src.components.texture import Texture, Point
from src.base.errors import ComponentNotFound, MissingCameraOnScene
from src.base.object import BaseObject
from src.base.scene import Scene
from src.utils.console import window
from src.utils.vector import Vector2


def in_region(reg_start: Vector2, reg_end: Vector2, point: Vector2) -> bool:
    return (reg_start.x < point.x < reg_end.x) and (reg_start.y <= point.y < reg_end.y)

class RenderSettings:
    camera_culling: bool = True

class RenderCore:
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
        if scene.camera is None:
            raise MissingCameraOnScene(scene)

        # Определение региона камеры (границ)
        region_start: Vector2 = Vector2(scene.camera.transform.position.x - round(scene.camera.size.x / 2),
                                        scene.camera.transform.position.y - round(scene.camera.size.y / 2))
        region_end: Vector2 = Vector2(region_start.x + scene.camera.size.x,
                                      region_start.y + scene.camera.size.y)

        # Смещение камеры для правильной отрисовки объектов
        camera_offset = scene.camera.transform.position - (scene.camera.size / 2)

        visible_objects = [obj for obj in scene.objects if obj.visible]
        points_without_culling: list[Point] = []
        points_with_culling: list[Point] = []

        # Объекты у которых есть компонент текстуры
        for obj in visible_objects:
            texture = obj.get_component(Texture)
            if texture:
                points_without_culling += obj.get_component(Texture).get()

        # # Если включен параметр camera_culling, урезаем точки
        if RenderSettings.camera_culling:
            for point in points_without_culling:
                if in_region(region_start, region_end, point.offset):
                    points_with_culling.append(point)
        else:
            points_with_culling = points_without_culling.copy()

        # Рисуем точки
        for point in points_with_culling:
            RenderCore.__draw_point(Point(point.sign, point.offset - camera_offset))


    @staticmethod
    def __draw_point(point: Point):
        window.addch(point.offset.y, point.offset.x, point.sign)

    @staticmethod
    def __draw_object(obj: BaseObject):
        texture = obj.get_component(Texture)
        for point in texture.get():
            pos = obj.transform.position + point.offset
            try:
                window.addch(pos.y, pos.x, point.sign)
            except curses.error:
                continue
