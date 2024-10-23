from src.base.object import BaseObject
from src.utils.vector import Vector2


class Camera(BaseObject):
    def __init__(self):
        super().__init__()
        self.size: Vector2 = Vector2(120, 30)
        self.position = Vector2(60, 15)
        self.name = 'Camera'