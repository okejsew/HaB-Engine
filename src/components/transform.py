from src.base.component import BaseComponent
from src.utils.vector import Vector2, Vector2F, Rotation


class Transform(BaseComponent):
    def __init__(self):
        super().__init__()
        self.position: Vector2 = Vector2()
        self.rotation: Rotation = Rotation.default
        self.moving_remainder: Vector2 = Vector2()

    def translate(self, delta: Vector2 | Vector2F):
        delta = Vector2F(self.moving_remainder.x + delta.x, self.moving_remainder.y + delta.y)
        int_vel = delta.to_int()
        self.moving_remainder = delta - int_vel
        self.position += int_vel
