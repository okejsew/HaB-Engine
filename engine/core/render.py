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
        self.render_debug_info: bool = True

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
                    set_point(point.offset - self.scene.camera.region[0], point.sign)

    def render_info(self):
        max_y, _ = window.getmaxyx()
        camera_region = self.scene.camera.region
        Debug.log('fps', f'Кадров в секунду: ~{self.fps}')
        Debug.log('camera_position', f'Позиция камеры: {self.scene.camera.transform.position}')
        Debug.log('camera_region', f'Регион камеры: {camera_region[0]} - {camera_region[1]}')
        Debug.log('camera_size', f'Размер камеры: {self.scene.camera.size}')
        Debug.log('scene_objects', f'Объектов на сцене: {len(self.scene.objects)}')

    def update(self):
        start_time = time.perf_counter()
        window.clear()
        self.render_objects()
        self.render_info()
        if self.render_debug_info:
            Debug.render()
        window.refresh()
        Time.delta = time.perf_counter() - start_time
        self.calc_fps(Time.delta)
