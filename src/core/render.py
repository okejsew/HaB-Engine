import time

from src.base.errors import MissingCameraOnScene
from src.base.scene import Scene
from src.components.texture import Texture, Point
from src.utils.console import window
from src.utils.vector import Vector2, in_region


class RenderSettings:
    camera_culling: bool = True
    show_fps: bool = True


class RenderCore:
    fps: float = time.time()

    @staticmethod
    def render_objects(scene: Scene):
        if scene.camera is None:
            MissingCameraOnScene(scene)

        # Определение региона камеры (границ)
        region_start: Vector2 = Vector2(scene.camera.position.x - round(scene.camera.size.x / 2),
                                        scene.camera.position.y - round(scene.camera.size.y / 2))
        region_end: Vector2 = Vector2(region_start.x + scene.camera.size.x,
                                      region_start.y + scene.camera.size.y)

        # Смещение камеры для правильной отрисовки объектов
        camera_offset = scene.camera.position - (scene.camera.size / 2)

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
            point_pos = point.offset - camera_offset
            window.addch(point_pos.y, point_pos.x, point.sign)

    @staticmethod
    def render_special():
        if RenderSettings.show_fps:
            window.addstr(window.getmaxyx()[0] - 1, 0, f'Кадров в секунду: ~{RenderCore.fps}')

    @staticmethod
    def calc_fps(start_time: float):
        t = time.time() - start_time
        RenderCore.fps = round(1 / t, 2) if t > 0 else RenderCore.fps

    @staticmethod
    def render(scene: Scene):
        window.clear()
        RenderCore.render_objects(scene)
        RenderCore.render_special()
        window.refresh()
