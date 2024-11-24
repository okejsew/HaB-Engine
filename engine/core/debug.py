from engine.tools.debug import Debug
from engine.tools.render import Renderer


class DebugRenderer:
    tick = 0

    def __init__(self):
        self.render = True
        super().__init__()

    @staticmethod
    def setup():
        Renderer.register(Debug.render)

    @staticmethod
    def update():
        Debug.update()
