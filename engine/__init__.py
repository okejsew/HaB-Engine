from .base.scene import Scene
from .core.debug import DebugRenderer
from .core.physic import Physic
from .core.renderer import ObjectRenderer
from .core.scripter import Scripter
from .tools.console import window
from .tools.debug import Debug
from .tools.render import Renderer


class Engine:
    scene: Scene = Scene()
    debug_mode: bool = False
    is_working: bool = False

    @staticmethod
    def setup():
        Debug.info('Настройка движка...')
        ObjectRenderer.setup(Engine.scene)
        Scripter.setup(Engine.scene)
        Physic.setup(Engine.scene)
        if Engine.debug_mode:
            DebugRenderer.setup()

    @staticmethod
    def run():
        Debug.info('Запуск движка...')
        Engine.is_working = True
        Engine.setup()
        Engine.thread()

    @staticmethod
    def thread():
        while Engine.is_working:
            Renderer.update()
            Scripter.update()
            DebugRenderer.update()

    @staticmethod
    def switch_scene(new: Scene):
        Debug.warn('Смена сцены...')
        Engine.scene = new

    @staticmethod
    def end():
        pass
