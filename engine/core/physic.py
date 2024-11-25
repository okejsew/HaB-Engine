import time
from threading import Thread
from typing import Optional

from engine.base.scene import Scene
from engine.components.rigidbody import Rigidbody


class PhysicsCore:
    scene: Optional[Scene] = None
    thread: Optional[Thread] = None

    @staticmethod
    def setup(scene: Scene):
        PhysicsCore.scene = scene
        PhysicsCore.thread = Thread(target=PhysicsCore.__thread)

    @staticmethod
    def __thread():
        from engine import Engine
        while Engine.is_working:
            try:
                PhysicsCore.update()
            except Exception as ex:
                Engine.error(ex)

    @staticmethod
    def update():
        for obj in PhysicsCore.scene:
            rigidbody = obj.get_component(Rigidbody)
            if rigidbody: rigidbody.update()
        time.sleep(0.016)
