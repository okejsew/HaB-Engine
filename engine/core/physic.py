import time
from threading import Thread
from typing import Optional

from engine.base.scene import Scene
from engine.components.rigidbody import Rigidbody
from engine.main import Engine


class PhysicsCore:
    scene: Optional[Scene] = None
    thread: Optional[Thread] = None

    @staticmethod
    def setup():
        PhysicsCore.scene = Engine.scene
        PhysicsCore.thread = Thread(target=PhysicsCore.__thread)

    @staticmethod
    def __thread():
        while Engine.is_working:
            try:
                PhysicsCore.update()
            except Exception as ex:
                Engine.error(ex)

    @staticmethod
    def update():
        for rigidbody in PhysicsCore.scene.get_components(Rigidbody):
            rigidbody.update()
        time.sleep(0.016)
