from src.base.component import Component
from src.base.utils.vector import Vector2, Vector2F, Rotation


class Transform(Component):
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

    def rotate_right(self):
        match self.rotation:
            case Rotation.right:
                self.rotation = Rotation.down
            case Rotation.down:
                self.rotation = Rotation.left
            case Rotation.left:
                self.rotation = Rotation.default
            case Rotation.default:
                self.rotation = Rotation.right

    def rotate_left(self):
        match self.rotation:
            case Rotation.right:
                self.rotation = Rotation.default
            case Rotation.down:
                self.rotation = Rotation.right
            case Rotation.left:
                self.rotation = Rotation.down
            case Rotation.default:
                self.rotation = Rotation.left
