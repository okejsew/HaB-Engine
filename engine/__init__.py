from typing import Optional

from .base.scene import Scene
from .core.physic import Physic
from .core.render import Render
from .core.scripting import Scripting


class Engine:
    def __init__(self):
        self.scene: Scene = Scene()
        self.is_working: bool = False

        self.render: Optional[Render] = None
        self.physic: Optional[Physic] = None
        self.scripting: Optional[Scripting] = None
        
        self.setup_core()

    def setup_core(self):
        self.render = Render(self.scene)
        self.physic = Physic(self.scene)
        self.scripting = Scripting(self.scene)

    def awake(self):
        self.is_working = True
        self.render.awake()
        self.physic.awake()
        self.scripting.awake()

    def run(self):
        self.awake()
        self.physic.start_thread()
        self.thread()

    def switch_scene(self, new: Scene):
        self.end()
        self.scene = new
        self.setup_core()
        self.run()


    def thread(self):
        while True:
            self.render.update()
            self.scripting.update()

    def end(self):
        self.render.end()
        self.physic.end()
        self.scripting.end()
