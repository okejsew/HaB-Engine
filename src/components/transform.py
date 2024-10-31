from src.base.component import BaseComponent
from src.utils.vector import Vector2, Vector2F, Rotation


class Transform(BaseComponent):
    def __init__(self):
        super().__init__()
        self.position: Vector2 = Vector2()
        self.rotation: Rotation = Rotation.default
        self.moving_remainder: Vector2 = Vector2()

    def translate(self, moving_factor: Vector2 | Vector2F):
        moving_factor = Vector2F(self.moving_remainder.x + moving_factor.x,
                                 self.moving_remainder.y + moving_factor.y)
        int_vel = moving_factor.to_int()
        self.moving_remainder = moving_factor - int_vel
        self.position += int_vel
