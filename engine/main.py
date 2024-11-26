import traceback

from engine.base.scene import Scene


class Engine:
    scene = Scene()
    is_working = False
    debug_mode = True

    @staticmethod
    def error(ex: Exception):
        from engine.app import Application
        Engine.is_working = False
        Application.end()
        traceback.print_exception(ex)
        input()
