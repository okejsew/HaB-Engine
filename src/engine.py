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
    frame_time: float = time.time()

    @staticmethod
    def debug_info() -> str:
        return f"""
Текущая сцена: {Engine.current_scene}
Кол-во объектов на сцене: {len(Engine.current_scene.objects)}
Время на кадр (Рендер) (Основной поток/1): {round(RenderCore.frame_time, 2)}
Время на кадр (УЯД)    (Основной поток/2): {round(UniversalCore.frame_time, 2)}
Время на кадр (Скрипты)(Основной поток/3): {round(ScriptCore.frame_time, 2)}
Время на кадр (Физика) (2 поток):          {round(PhisycsCore.frame_time, 2)}
Кадров в секунду: ~{round(1 / RenderCore.frame_time, 2) if RenderCore.frame_time != 0 else '?'}
"""


    @staticmethod
    def run():
        if Engine.current_scene is None:
            MissingSceneError()
        Engine.is_working = True
        Engine.start_thread(PhisycsCore.thread)
        Engine.main_thread()

    @staticmethod
    def main_thread():
        while Engine.is_working:
            RenderCore.render()
            UniversalCore.handle(Engine.current_scene)
            ScriptCore.handle(Engine.current_scene)

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
