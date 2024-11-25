from typing import Optional

from engine.base.cmp.script import Script
from engine.base.scene import Scene


class Scripter:
    scene: Optional[Scene] = None

    @staticmethod
    def setup():
        from engine import Engine
        Scripter.scene = Engine.scene

    @staticmethod
    def get_scripts() -> list[Script]:
        scripts = []
        for obj in Scripter.scene:
            scripts += obj.get_components(Script)
        return scripts

    @staticmethod
    def awake():
        for script in Scripter.get_scripts():
            script.awake()

    @staticmethod
    def update():
        for script in Scripter.get_scripts():
            script.update()
