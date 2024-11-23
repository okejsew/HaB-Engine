import time
from typing import Callable

from engine.tools.console import window
from engine.tools.debug import Debug


class Renderer:
    fps: float = 0
    listeners: list[Callable[[], None]] = []

    @staticmethod
    def register(listener: Callable[[], None]):
        Renderer.listeners.append(listener)

    @staticmethod
    def update():
        start = time.perf_counter()
        window.clear()
        for listener in Renderer.listeners:
            listener()
        window.refresh()
        delta = time.perf_counter() - start
        Renderer.fps = round(1 / delta, 2) if delta != 0 else Renderer.fps
        Debug.log('delta', f'Кадров в секунду: {Renderer.fps}')
