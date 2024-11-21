import time

from engine.base.cmp.texture import Texture
from engine.base.scene import Scene
from engine.base.time import Time
from engine.core import Core
from engine.tools.console import window, set_point
from engine.tools.debug import Debug


class Render(Core):
    def __init__(self, scene: Scene):
        super().__init__(scene)
        self.fps: float = time.time()

    def calc_fps(self, delta: float):
        self.fps = round(1 / delta, 2) if delta > 0 else self.fps

    def render_objects(self):
        self.scene.camera.update()
        objects_to_draw = [obj for obj in self.scene.objects if obj.visible]

        for obj in objects_to_draw:
            texture = obj.get_component(Texture)
            if not texture: continue
            for raw_point in texture.get():
                point = self.scene.camera.true_point(raw_point, obj)
                if self.scene.camera.in_region(point):
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
