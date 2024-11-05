from threading import Thread
from typing import Optional

from src.base.scene import Scene


class Core:
    def __init__(self, scene: Scene):
        self.scene = scene
        self.thread: Optional[Thread] = None
        self.is_working: bool = False

    def start_thread(self):
        def thrd():
            while self.is_working:
                self.update()

        t = Thread(target=thrd)
        t.start()
        self.thread = t

    def awake(self):
        self.is_working = True

    def end(self):
        self.is_working = False
        if self.thread:
            self.thread.join()
            self.thread = None

    def update(self):
        pass
