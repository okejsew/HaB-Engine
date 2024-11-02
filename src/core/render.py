import time

from src.base.scene import Scene
from src.components.texture import Texture, Point
from src.utils.console import window
from src.utils.vector import Vector2


class RenderCore:
    fps: float = time.time()
    points_without_culling: list[Point] = []
    points_with_culling: list[Point] = []

    @staticmethod
    def calc_fps(start_time: float):
        t = time.perf_counter() - start_time
        RenderCore.fps = round(1 / t, 2) if t > 0 else RenderCore.fps

    @staticmethod
    def set_point(pos: Vector2, sign: str):
        try:
            window.addch(pos.y, pos.x, sign)
        finally:
            ...

    @staticmethod
    def render_objects(scene: Scene):
        del RenderCore.points_without_culling[:]
        del RenderCore.points_with_culling[:]
        RenderCore.points_without_culling.clear()
        RenderCore.points_with_culling.clear()

        cam_start: Vector2 = Vector2(scene.camera.transform.position.x - round(scene.camera.size.x / 2),
                                     scene.camera.transform.position.y - round(scene.camera.size.y / 2))
        cam_end: Vector2 = Vector2(cam_start.x + scene.camera.size.x, cam_start.y + scene.camera.size.y)

        camera_offset = scene.camera.transform.position - (scene.camera.size / 2)
        objects_to_draw = [obj for obj in scene.objects if obj.visible]

        for obj in objects_to_draw:
            texture = obj.get_component(Texture)
            if texture:
                for point in texture.get():
                    pc = point.copy()
                    obj.transform.rotation.rotate_offset(pc.offset, obj.transform.rotation)
                    pc.offset += obj.transform.position
                    pc.offset -= camera_offset
                    RenderCore.points_without_culling.append(pc)

        for point in RenderCore.points_without_culling:
            if (cam_start.x < point.offset.x < cam_end.x) and (cam_start.y <= point.offset.y < cam_end.y):
                RenderCore.points_with_culling.append(point)

        for point in RenderCore.points_with_culling:
            RenderCore.set_point(point.offset, point.sign)

    @staticmethod
    def render_fps():
        window.addstr(window.getmaxyx()[0] - 1, 0, f'Кадров в секунду: ~{RenderCore.fps}')

    @staticmethod
    def render_errors():
        from src.utils.error import Debug
        for i, report in enumerate(Debug.stack):
            window.addstr(i, 0, report.message, report.color)

    @staticmethod
    def render(scene: Scene):
        window.clear()
        RenderCore.render_objects(scene)
        RenderCore.render_fps()
        RenderCore.render_errors()
        window.refresh()
