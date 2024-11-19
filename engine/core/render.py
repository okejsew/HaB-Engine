import time

from engine.base.cmp.texture import Texture, TPoint
from engine.base.common.vector import Vector2
from engine.base.scene import Scene
from engine.base.time import Time
from engine.core import Core
from engine.tools.console import window, set_point
from engine.tools.debug import Debug


class Render(Core):
    def __init__(self, scene: Scene):
        super().__init__(scene)
        self.fps: float = time.time()
        self.points: list[TPoint] = []

    def calc_fps(self, delta: float):
        self.fps = round(1 / delta, 2) if delta > 0 else self.fps

    def render_objects(self):
        self.points = []

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
                    pc.offset += obj.transform.position - camera_offset
                    self.points.append(pc)

        for point in self.points:
            if (cam_start.x < point.offset.x < cam_end.x) and (cam_start.y <= point.offset.y < cam_end.y):
                set_point(point.offset, point.sign)

    def render_fps(self):
        window.addstr(window.getmaxyx()[0] - 1, 0, f'Кадров в секунду: ~{self.fps}')

    def update(self):
        start_time = time.perf_counter()
        window.clear()
        self.render_objects()
        self.render_fps()
        Debug.render()
        window.refresh()
        Time.delta = time.perf_counter() - start_time
        self.calc_fps(Time.delta)
