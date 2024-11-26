from engine.base.object import Object
from engine.core.physic import PhysicsCore
from engine.core.render import RenderCore
from engine.core.script import ScriptCore
from engine.main import Engine
from engine.tools.console import Console


class Application:
    @staticmethod
    def setup():
        for core in [RenderCore, ScriptCore, PhysicsCore]:
            try:
                core.setup()
            except Exception as ex:
                Engine.error(ex)

    @staticmethod
    def add(obj: Object):
        Engine.scene.add(obj)

    @staticmethod
    def run():
        Application.setup()
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
