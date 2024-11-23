import time
from threading import Thread
from typing import Optional

from engine.base.cmp.rigidbody import Rigidbody
from engine.base.scene import Scene


class Physic:
    scene: Optional[Scene] = None
    thread: Optional[Thread] = None

    @staticmethod
    def setup(scene: Scene):
        Physic.scene = scene

    @staticmethod
    def start_thread():
        from engine import Engine

        def _thread():
            while Engine.is_working:
                Physic.update()

        Physic.thread = Thread(target=_thread)
        Physic.thread.start()

    @staticmethod
    def update():
        for obj in Physic.scene.objects:
            rigidbody = obj.get_component(Rigidbody)
            if rigidbody: rigidbody.update()
        time.sleep(0.016)
