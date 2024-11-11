from src.base.scene import Scene
from src.components.script import Script
from src.core import Core


class Scripting(Core):
    def __init__(self, scene: Scene):
        super().__init__(scene)

    def get_scripts(self) -> list[Script]:
        scripts = []
        for obj in self.scene.objects:
            scripts += obj.get_components(Script)
        return scripts

    def awake(self):
        super().awake()
        for script in self.get_scripts():
            script.awake()

    def update(self):
        for script in self.get_scripts():
            script.update()
