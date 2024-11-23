from typing import Optional

from engine.base.cmp.script import Script
from engine.base.scene import Scene
from engine.tools.debug import Debug


class Scripter:
    scene: Optional[Scene] = None

    @staticmethod
    def setup(scene: Scene):
        Scripter.scene = scene
        for script in Scripter.get_scripts():
            script.awake()

    @staticmethod
    def get_scripts() -> list[Script]:
        scripts = []
        for obj in Scripter.scene.objects:
            scripts += obj.get_components(Script)
        Debug.log('scripts_count', f'Активных скриптов: {len(scripts)}')
        return scripts

    @staticmethod
    def update():
        for script in Scripter.get_scripts():
            script.update()
