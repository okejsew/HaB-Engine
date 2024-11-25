import curses

from .base.object import Object
from .base.scene import Scene
from .core.physic import Physic
from .core.renderer import Renderer
from .core.scripter import Scripter
from .tools.console import window, Console
from .tools.debug import Debug


class Engine:
    scene = Scene()
    is_working = False

    @staticmethod
    def setup():
        Engine.is_working = True
        for core in [Renderer, Scripter, Physic]:
            core.setup()

    @staticmethod
    def run():
        Engine.setup()
        Physic.thread.start()
        while Engine.is_working:
            try:
                Console.update()
                Scripter.update()
            except Exception as ex:
                Engine.error(ex)

    @staticmethod
    def error(ex: Exception):
        Engine.is_working = False
        curses.endwin()
        try:
            Physic.thread.join()
        except Exception as exp:
            print(f'Ошибка не в главном потоке ({exp})')
        input(f'Произошла ошибка: {ex}')
