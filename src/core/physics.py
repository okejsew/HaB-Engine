import time

from src.base.scene import Scene
from src.components.rigidbody import Rigidbody


class PhisycsCore:
    @staticmethod
    def handle(scene: Scene):
        for obj in scene.objects:
            rigidbody = obj.get_component(Rigidbody)
            if rigidbody: rigidbody.update()

    @staticmethod
    def thread():
        from src.engine import Engine
        while Engine.is_working:
            PhisycsCore.handle(Engine.current_scene)
            time.sleep(0.016)
