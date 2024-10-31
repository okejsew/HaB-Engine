import time
from threading import Thread
from typing import Optional

from src.base.scene import Scene
from src.core.physics import PhisycsCore
from src.core.render import RenderCore


class Engine:
    current_scene: Optional[Scene] = None
    threads: list[Thread] = []
    is_working: bool = False
    debug_mode: bool = False

    @staticmethod
    def run():
        Engine.is_working = True
        Thread(target=PhisycsCore.thread).start()
        Engine.main_thread()

    @staticmethod
    def main_thread():
        while Engine.is_working:
            start_time = time.perf_counter()
            RenderCore.render(Engine.current_scene)
            RenderCore.calc_fps(start_time)
