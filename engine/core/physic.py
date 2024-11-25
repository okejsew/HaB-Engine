import time
from threading import Thread
from typing import Optional

from engine.base.cmp.rigidbody import Rigidbody
from engine.base.scene import Scene


class Physic:
    scene: Optional[Scene] = None
    thread: Optional[Thread] = None

    @staticmethod
    def setup():
        from engine import Engine
        Physic.scene = Engine.scene
        Physic.thread = Thread(target=Physic.__thread)

    @staticmethod
    def __thread():
        from engine import Engine
        while Engine.is_working:
            try:
                Physic.update()
            except Exception as ex:
                Engine.error(ex)

    @staticmethod
    def update():
        for obj in Physic.scene:
            rigidbody = obj.get_component(Rigidbody)
            if rigidbody: rigidbody.update()
        time.sleep(0.016)
