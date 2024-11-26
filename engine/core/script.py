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
        return ScriptCore.scene.get_components(Script)

    @staticmethod
    def awake(): map(lambda s: s.awake(), ScriptCore.get_scripts())

    @staticmethod
    def update(): map(lambda s: s.update(), ScriptCore.get_scripts())
