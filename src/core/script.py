from src.base.scene import Scene
from src.base.script import Script

class ScriptCore:
    @staticmethod
    def handle(scene: Scene):
        scripts = []
        for obj in scene.objects:
            scripts += obj.get_components(Script)
        for script in scripts:
            script.fixed_update()

