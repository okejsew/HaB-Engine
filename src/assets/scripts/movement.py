from src.base.script import Script
from src.utils.input import Input


class BasicMovement(Script):
    def __init__(self):
        super().__init__()

    def fixed_update(self):
        key = Input.get_key()
        if key == ord('a'):
            self.owner.position.x -= 1
        if key == ord('d'):
            self.owner.position.x += 1
        if key == ord('w'):
            self.owner.position.y -= 1
        if key == ord('s'):
            self.owner.position.y += 1
