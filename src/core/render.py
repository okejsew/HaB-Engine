import time

from src.base.object import BaseObject
from src.base.scene import Scene
from src.components.texture import Texture, Point
from src.utils.console import window
from src.utils.vector import Vector2, in_region


class RenderCore:
    fps: float = time.time()
    points_without_culling: list[Point] = []
    points_with_culling: list[Point] = []

    @staticmethod
    def render_objects(scene: Scene):
        for p in RenderCore.points_without_culling:
            del p
        for p in RenderCore.points_with_culling:
            del p
        RenderCore.points_without_culling.clear()
        RenderCore.points_with_culling.clear()

        region_start: Vector2 = Vector2(scene.camera.transform.position.x - round(scene.camera.size.x / 2),
                                        scene.camera.transform.position.y - round(scene.camera.size.y / 2))
        region_end: Vector2 = Vector2(region_start.x + scene.camera.size.x,
                                      region_start.y + scene.camera.size.y)

        camera_offset = scene.camera.transform.position - (scene.camera.size / 2)

        def calc_point(obj: BaseObject, point: Point):
            pc = point.copy()
            obj.transform.rotation.rotate(pc.offset, obj.transform.rotation)
            pc.offset += obj.transform.position
            pc.offset -= camera_offset
            RenderCore.points_without_culling.append(pc)

        objects_to_draw = [obj for obj in scene.objects if obj.visible]

        for obj in objects_to_draw:
            texture = obj.get_component(Texture)
            if texture:
                for point in texture.get():
                    calc_point(obj, point)

        for point in RenderCore.points_without_culling:
            if in_region(region_start, region_end, point.offset):
                RenderCore.points_with_culling.append(point)

        for point in RenderCore.points_with_culling:
            RenderCore.set_point(point.offset, point.sign)

    @staticmethod
    def set_point(pos: Vector2, sign: str):
        try:
            window.addch(pos.y, pos.x, sign)
        finally:
            ...

    @staticmethod
    def render_fps():
        window.addstr(window.getmaxyx()[0] - 1, 0, f'Кадров в секунду: ~{RenderCore.fps}')

    @staticmethod
    def calc_fps(start_time: float):
        t = time.perf_counter() - start_time
        RenderCore.fps = round(1 / t, 2) if t > 0 else RenderCore.fps

    @staticmethod
    def render(scene: Scene):
        window.clear()
        RenderCore.render_objects(scene)
        RenderCore.render_fps()
        window.refresh()
