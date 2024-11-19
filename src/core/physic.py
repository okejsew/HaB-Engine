import time

from src.base.cmp.rigidbody import Rigidbody
from src.base.scene import Scene
from src.core import Core
from src.tools.debug import Debug


class Physic(Core):
    def __init__(self, scene: Scene):
        super().__init__(scene)

    def update(self):
        for obj in self.scene.objects:
            rigidbody = obj.get_component(Rigidbody)
            if rigidbody: rigidbody.update()
        Debug.update()
        time.sleep(0.016)
