from engine.base.cmp.script import Script
from engine.base.scene import Scene
from engine.core import Core
from engine.tools.debug import Debug


class Scripting(Core):
    def __init__(self, scene: Scene):
        super().__init__(scene)

    def get_scripts(self) -> list[Script]:
        scripts = []
        for obj in self.scene.objects:
            scripts += obj.get_components(Script)
        Debug.log('scripts_count', f'Активных скриптов: {len(scripts)}')
        return scripts

    def awake(self):
        Debug.info('Запуск системы скриптов')
        super().awake()
        for script in self.get_scripts():
            script.awake()

    def update(self):
        for script in self.get_scripts():
            script.update()
