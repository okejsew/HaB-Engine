import time

from src.components.rigidbody import Rigidbody
from src.base.errors import ComponentNotFound
from src.base.scene import Scene


class PhisycsCore:
    update_time: float = time.time()

    @staticmethod
    def handle(scene: Scene):
        start_time = time.time()
        for obj in scene.objects:
            try: rigidbody = obj.get_component(Rigidbody)
            except ComponentNotFound: continue
            else: rigidbody.update()
        PhisycsCore.update_time = time.time() - start_time
