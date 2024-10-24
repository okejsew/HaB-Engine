import time

from src.base.object import BaseObject
from src.base.scene import Scene
from src.utils.vector import in_region, Vector2


class UniversalCore:
    frame_time: float = time.time()

    @staticmethod
    def destroy(obj: BaseObject):
        obj.scene.remove(obj)
        del obj

    @staticmethod
    def handle(scene: Scene):
        start_time = time.time()
        for obj in scene.objects:
            if not in_region(Vector2(-1000000000, -1000000000),
                             Vector2(1000000000, 1000000000), obj.position):
                UniversalCore.destroy(obj)
        UniversalCore.frame_time = time.time() - start_time

    @staticmethod
    def thread():
        from src.engine import Engine
        while Engine.is_working:

            UniversalCore.handle(Engine.current_scene)

