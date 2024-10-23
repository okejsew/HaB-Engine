import time

from src.components.rigidbody import Rigidbody
from src.base.scene import Scene


class PhisycsCore:
    frame_time: float = time.time()

    @staticmethod
    def handle(scene: Scene):
        start_time = time.time()
        for obj in scene.objects:
            rigidbody = obj.get_component(Rigidbody)
            if rigidbody:
                rigidbody.update()
        PhisycsCore.frame_time = time.time() - start_time
