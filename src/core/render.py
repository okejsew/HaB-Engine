import time

from src.base.scene import Scene
from src.components.texture import Texture, Point
from src.utils.console import window, set_point
from src.utils.error import Debug
from src.utils.vector import Vector2


class RenderCore:
    def __init__(self, scene: Scene):
        self.scene = scene
        self.fps: float = time.time()
        self.points_without_culling: list[Point] = []
        self.points_with_culling: list[Point] = []

    def calc_fps(self, start_time: float):
        t = time.perf_counter() - start_time
        self.fps = round(1 / t, 2) if t > 0 else self.fps

    def render_objects(self):
        del self.points_without_culling[:]
        del self.points_with_culling[:]
        self.points_without_culling.clear()
        self.points_with_culling.clear()

        cam_start: Vector2 = Vector2(self.scene.camera.transform.position.x - round(self.scene.camera.size.x / 2),
                                     self.scene.camera.transform.position.y - round(self.scene.camera.size.y / 2))
        cam_end: Vector2 = Vector2(cam_start.x + self.scene.camera.size.x, cam_start.y + self.scene.camera.size.y)

        camera_offset = self.scene.camera.transform.position - (self.scene.camera.size / 2)
        objects_to_draw = [obj for obj in self.scene.objects if obj.visible]

        for obj in objects_to_draw:
            texture = obj.get_component(Texture)
            if texture:
                for point in texture.get():
                    pc = point.copy()
                    obj.transform.rotation.rotate_offset(pc.offset, obj.transform.rotation)
                    pc.offset += obj.transform.position
                    pc.offset -= camera_offset
                    self.points_without_culling.append(pc)

        for point in self.points_without_culling:
            if (cam_start.x < point.offset.x < cam_end.x) and (cam_start.y <= point.offset.y < cam_end.y):
                self.points_with_culling.append(point)

        for point in self.points_with_culling:
            set_point(point.offset, point.sign)

    def render_fps(self):
        window.addstr(window.getmaxyx()[0] - 1, 0, f'Кадров в секунду: ~{self.fps}')

    def update(self):
        window.clear()
        self.render_objects()
        self.render_fps()
        Debug.render()
        window.refresh()
