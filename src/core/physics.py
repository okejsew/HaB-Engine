import time

from src.base.scene import Scene
from src.components.rigidbody import Rigidbody
from src.utils.error import Debug


class PhysicsCore:
    def __init__(self, scene: Scene):
        self.scene: Scene = scene
        self.is_working: bool = False

    def thread(self):
        while self.is_working:
            for obj in self.scene.objects:
                rigidbody = obj.get_component(Rigidbody)
                if rigidbody: rigidbody.update()
            Debug.update()
            time.sleep(0.016)
