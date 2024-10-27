from src.base.scene import Scene
from src.base.script import Script


class ScriptCore:
    @staticmethod
    def get_scripts(scene: Scene):
        scripts = []
        for obj in scene.objects:
            scripts += obj.get_components(Script)
        return scripts

    @staticmethod
    def handle(scene: Scene):
        for script in ScriptCore.get_scripts(scene):
            script.fixed_update()

    @staticmethod
    def awake(scene: Scene):
        for script in ScriptCore.get_scripts(scene):
            script.awake()
