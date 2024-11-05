import time
from threading import Thread
from typing import Optional

from src.base.scene import Scene
from src.core.physics import PhysicsCore
from src.core.render import RenderCore


class Engine:
    def __init__(self):
        self.current_scene: Optional[Scene] = None
        self.is_working: bool = False

        self.render: Optional[RenderCore] = None
        self.physic: Optional[PhysicsCore] = None

    def run(self):
        self.render = RenderCore(self.current_scene)
        self.physic = PhysicsCore(self.current_scene)

        self.is_working = True
        self.physic.is_working = True

        Thread(target=self.physic.thread).start()
        self.main_thread()

    def main_thread(self):
        while self.is_working:
            start_time = time.perf_counter()
            self.render.update()
            self.render.calc_fps(start_time)
