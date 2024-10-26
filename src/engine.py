import time
from threading import Thread
from typing import Callable, Optional

from src.base.scene import Scene
from src.base.errors import MissingSceneError

from src.core.render import RenderCore
from src.core.physics import PhisycsCore
from src.core.script import ScriptCore
from src.core.universal import UniversalCore

class Engine:
    current_scene: Optional[Scene] = None
    threads: list[Thread] = []
    is_working: bool = False
    debug_mode: bool = False

    @staticmethod
    def run():
        if Engine.current_scene is None:
            MissingSceneError()
        Engine.is_working = True
        Engine.start_thread(PhisycsCore.thread)
        Engine.main_thread()

    @staticmethod
    def main_thread():
        ScriptCore.awake(Engine.current_scene)
        while Engine.is_working:
            start_time = time.time()
            RenderCore.render(Engine.current_scene)
            UniversalCore.handle(Engine.current_scene)
            ScriptCore.handle(Engine.current_scene)
            RenderCore.calc_fps(start_time)

    @staticmethod
    def start_thread(func: Callable):
        thread = Thread(target=func)
        Engine.threads.append(thread)
        thread.start()

    @staticmethod
    def end_all_threads():
        for thread in Engine.threads:
            thread.join()
        Engine.threads.clear()
