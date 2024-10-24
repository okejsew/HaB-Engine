from src.base.script import Script

class TestScript(Script):
    def __init__(self):
        super().__init__()
    
    def fixed_update(self):
        if self.owner.position.y == 20:
            self.owner.position.y = 5