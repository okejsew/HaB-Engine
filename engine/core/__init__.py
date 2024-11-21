from threading import Thread
from typing import Optional

from engine.base.scene import Scene
from engine.tools.debug import Debug


class Core:
    def __init__(self, scene: Scene):
        self.scene = scene
        self.thread: Optional[Thread] = None
        self.is_working: bool = False

    def start_thread(self):
        Debug.warn(f'Запуск потока для "{self.__class__.__name__}"')

        def thrd():
            while self.is_working:
                self.update()

        t = Thread(target=thrd)
        t.start()
        self.thread = t

    def awake(self):
        self.is_working = True

    def end(self):
        Debug.warn(f'Завершение потока для "{self.__class__.__name__}"')
        self.is_working = False
        if self.thread:
            self.thread.join()
            self.thread = None

    def update(self):
        pass
