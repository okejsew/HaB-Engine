import time
from threading import Thread
from typing import Callable

from src.base.scene import Scene
from src.base.errors import MissingSceneError

from src.core.render import RenderCore
from src.core.physics import PhisycsCore
from src.core.universal import UniversalCore

class Engine:
    current_scene: Scene | None = None
    threads: list[Thread] = []
    is_working: bool = False
    debug_mode: bool = False
    frame_time: float = time.time()

    @staticmethod
    def debug_info() -> str:
        return f"""
Текущая сцена: {Engine.current_scene}
Кол-во объектов на сцене: {len(Engine.current_scene.objects)}
Время на кадр (Рендер) (Основной поток): {round(RenderCore.frame_time, 2)}
Время на кадр (Физика) (2 поток):        {round(PhisycsCore.frame_time, 2)}
Время на кадр (УЯД)    (3 поток):        {round(UniversalCore.frame_time, 2)}
Кадров в секунду: ~{round(1 / RenderCore.frame_time, 2)}
"""


    @staticmethod
    def run():
        if Engine.current_scene is None:
            MissingSceneError()
        Engine.is_working = True
        Engine.start_thread(PhisycsCore.thread)
        Engine.start_thread(UniversalCore.thread)
        Engine.main_thread()

    @staticmethod
    def main_thread():
        while Engine.is_working:
            RenderCore.render()

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
