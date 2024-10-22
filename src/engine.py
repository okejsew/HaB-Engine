import curses
import time
from threading import Thread
from time import sleep
from typing import Callable
from src.base.errors import MissingSceneError
from src.base.scene import Scene
from src.core.physics import PhisycsCore
from src.core.render import RenderCore


class Engine:
    __current_scene: Scene | None = None
    is_working: bool = False
    debug_mode: bool = False
    frame_time: float = time.time()

    @staticmethod
    def set_scene(scene: Scene):
        Engine.__current_scene = scene

    @staticmethod
    def __check_scene(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            if Engine.__current_scene is None:
                raise MissingSceneError()
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def __debug_info():
        RenderCore.print(1, 1, f'Текущая сцена: {Engine.__current_scene}')
        RenderCore.print(2, 1, f'Кол-во объектов на сцене: {len(Engine.__current_scene.objects)}')



    @staticmethod
    @__check_scene
    def run():
        Engine.is_working = True
        Thread(target=Engine.__physics_thread).start()
        while Engine.is_working:
            RenderCore.clear()
            RenderCore.draw_objects(Engine.__current_scene)
            if Engine.debug_mode:
                Engine.__debug_info()
            RenderCore.refresh()

    @staticmethod
    def end():
        Engine.is_working = False
        curses.endwin()

    @staticmethod
    def __drawing_thread():
        while Engine.is_working:
            RenderCore.clear()
            RenderCore.draw_objects(Engine.__current_scene)
            if Engine.debug_mode:
                Engine.__debug_info()
            RenderCore.refresh()

    @staticmethod
    @__check_scene
    def __physics_thread():
        while Engine.is_working:
            PhisycsCore.handle(Engine.__current_scene)
            sleep(0.016)
