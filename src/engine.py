import time
from threading import Thread
from typing import Callable

from src.base.scene import Scene
from src.base.errors import MissingSceneError

from src.core.render import RenderCore
from src.core.physics import PhisycsCore


class Engine:
    __current_scene: Scene | None = None
    __threads: list[Thread] = []
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
        RenderCore.print(3, 1, f'Время на кадр (Рендер)(Основной поток): {round(Engine.frame_time, 2)}')
        RenderCore.print(4, 1, f'Время на кадр (Физика)(Второй поток): {round(PhisycsCore.frame_time, 2)}')

    @staticmethod
    @__check_scene
    def run():
        Engine.is_working = True
        Engine.__start_physic()
        while Engine.is_working:
            start_time = time.time()
            Engine.__draw_frame()
            Engine.frame_time = time.time() - start_time

    @staticmethod
    def __draw_frame():
        RenderCore.clear()
        if Engine.debug_mode: Engine.__debug_info()
        RenderCore.draw_objects(Engine.__current_scene)
        RenderCore.refresh()

    @staticmethod
    def __close_threads():
        for thread in Engine.__threads:
            thread.join()

    @staticmethod
    def __start_physic():
        pt = Thread(target=Engine.__physics_thread)
        Engine.__threads.append(pt)
        pt.start()

    @staticmethod
    @__check_scene
    def __physics_thread():
        while Engine.is_working:
            PhisycsCore.handle(Engine.__current_scene)
            time.sleep(0.016)
