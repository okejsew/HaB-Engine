from typing import Optional

from src.base.object import BaseObject
from src.base.script import Script


class CameraTracking(Script):
    def __init__(self):
        super().__init__()
        self.target: Optional[BaseObject] = None

    def fixed_update(self):
        if self.target is not None:
            self.owner.position = self.target.position.copy()
