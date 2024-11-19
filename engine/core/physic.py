import time

from engine.base.cmp.rigidbody import Rigidbody
from engine.base.scene import Scene
from engine.core import Core
from engine.tools.debug import Debug


class Physic(Core):
    def __init__(self, scene: Scene):
        super().__init__(scene)

    def update(self):
        for obj in self.scene.objects:
            rigidbody = obj.get_component(Rigidbody)
            if rigidbody: rigidbody.update()
        Debug.update()
        time.sleep(0.016)
