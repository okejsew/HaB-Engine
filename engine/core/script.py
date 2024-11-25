from typing import Optional

from engine.base.scene import Scene
from engine.components.script import Script


class ScriptCore:
    scene: Optional[Scene] = None

    @staticmethod
    def setup(scene: Scene):
        ScriptCore.scene = scene

    @staticmethod
    def get_scripts() -> list[Script]:
        scripts = []
        for obj in ScriptCore.scene:
            scripts += obj.get_components(ScriptCore)
        return scripts

    @staticmethod
    def awake():
        for script in ScriptCore.get_scripts():
            script.awake()

    @staticmethod
    def update():
        for script in ScriptCore.get_scripts():
            script.update()
