import time

from src.base.scene import Scene
from src.base.script import Script


class ScriptCore:
    frame_time: float = time.time()

    @staticmethod
    def handle(scene: Scene):
        start_time = time.time()
        for obj in scene.objects:
            scripts = obj.get_all_component(Script)
            for script in scripts:
                script.fixed_update()
        ScriptCore.frame_time = time.time() - start_time

    @staticmethod
    def thread():
        from src.engine import Engine
        while Engine.is_working:
            ScriptCore.handle(Engine.current_scene)
