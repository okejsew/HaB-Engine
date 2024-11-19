from src.base.object import Object
from src.base.utils.vector import Vector2


class Camera(Object):
    def __init__(self):
        super().__init__()
        self.size: Vector2 = Vector2(120, 30)
        self.transform.position = Vector2(60, 15)
        self.name = 'Camera'
