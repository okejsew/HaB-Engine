from src.base.scene import Scene
from src.core.physics import Physics
from src.core.render import Render


class Engine:
    def __init__(self):
        self.scene: Scene = Scene()
        self.is_working: bool = False

        self.render: Render = Render(self.scene)
        self.physic: Physics = Physics(self.scene)

    def awake(self):
        self.is_working = True
        self.render.awake()
        self.physic.awake()

    def run(self):
        self.awake()
        self.physic.start_thread()
        self.render.start_thread()

    def end(self):
        self.render.end()
        self.physic.end()
