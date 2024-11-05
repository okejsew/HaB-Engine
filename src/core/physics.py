import time

from src.base.scene import Scene
from src.components.rigidbody import Rigidbody
from src.core import Core
from src.utils.error import Debug


class Physics(Core):
    def __init__(self, scene: Scene):
        super().__init__(scene)

    def update(self):
        for obj in self.scene.objects:
            rigidbody = obj.get_component(Rigidbody)
            if rigidbody: rigidbody.update()
        Debug.update()
        time.sleep(0.016)
