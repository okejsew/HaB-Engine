from .base.object import Object
from .base.scene import Scene
from .core.debug import DebugRenderer
from .core.physic import Physic
from .core.renderer import ObjectRenderer
from .core.scripter import Scripter
from .tools.console import window
from .tools.debug import Debug
from .tools.render import Renderer


class Engine:
    scene = Scene()
    debug_mode = False
    is_working = False

    def add_object(self, obj: Object):
        self.scene.add(obj)

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
        Physic.start_thread()
        while Engine.is_working:
            Renderer.update()
            Scripter.update()
            DebugRenderer.update()

    @staticmethod
    def switch_scene(new: Scene):
        Debug.warn('Смена сцены...')
        Engine.scene = new
        Engine.setup()

    @staticmethod
    def set_scene(new: Scene):
        Engine.scene = new

    @staticmethod
    def end():
        Engine.is_working = False
        Physic.thread.join()
