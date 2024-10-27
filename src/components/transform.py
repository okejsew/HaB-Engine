from src.base.component import BaseComponent
from src.utils.vector import Vector2


class Transform(BaseComponent):
    def __init__(self):
        super().__init__()
        self.position: Vector2 = Vector2()