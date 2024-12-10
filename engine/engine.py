from engine.base.object import Object
from engine.base.scene import Scene
import engine.core.physic as physic
import engine.core.render as render
import engine.tools.console as console


class Engine:
    def __init__(self):
        self.state = {'work': False, 'stop': True}
        self.scene: Scene = Scene()
        self.setup()

    def setup(self):
        render.__init__(self.scene)
        physic.__init__(self.scene, self.state)
        console.__init__()

    def end(self):
        self.state['work'] = False
        while not self.state['stop']:
            pass

    def run(self):
        self.state['stop'], self.state['work'] = False, True
        physic.thread.start()
        while self.state['work']:
            console.render()
        self.state['stop'] = True

    def switch_scene(self, new: Scene):
        self.end()
        self.scene = new
        self.setup()
        self.run()

    def add(self, obj: Object):
        self.scene.add(obj)
