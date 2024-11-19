from src.base.component import Component


class Script(Component):
    def __init__(self):
        super().__init__()

    def awake(self): ...

    def update(self): ...
