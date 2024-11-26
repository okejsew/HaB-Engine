import traceback

from .base.scene import Scene
from .core.physic import PhysicsCore
from .core.render import RenderCore
from .core.script import ScriptCore
from .tools.console import Console
from .tools.debug import Debug


class Engine:
    scene = Scene()
    is_working = False

    @staticmethod
    def setup():
        try:
            for core in [RenderCore, ScriptCore, PhysicsCore]:
                core.setup(Engine.scene)
            Debug.setup()
        except Exception as ex:
            Engine.error(ex)

    @staticmethod
    def run():
        Engine.setup()
        ScriptCore.awake()
        Engine.is_working = True
        PhysicsCore.thread.start()
        while Engine.is_working:
            try:
                Console.update()
                ScriptCore.update()
            except Exception as ex:
                Engine.error(ex)

    @staticmethod
    def end():
        Engine.is_working = False
        Console.end()
        try:
            PhysicsCore.thread.join()
        except Exception as exp:
            print(f'Ошибка в потоке физики ({exp})')

    @staticmethod
    def error(ex: Exception):
        Engine.end()
        print(ex)
        traceback.print_exc()
        input()
