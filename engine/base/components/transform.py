from engine.base.component import Component
from engine.math import Vector2, Vector2F, Rotation
from engine.base.components import Collider


class Transform(Component):
    def __init__(self):
        super().__init__()
        self.position = Vector2()
        self.rotation = Rotation.default
        self.moving_remainder = Vector2()

    def translate(self, delta: Vector2 | Vector2F):
        try:
            if collider := self.owner.get_component(Collider):
                direction = delta.direction()
                if collider.check_direction(Vector2(direction.x, direction.y)):
                    return
            delta = Vector2F(self.moving_remainder.x + delta.x, self.moving_remainder.y + delta.y)
            int_vel = delta.to_int()
            self.moving_remainder = delta - int_vel
            self.position += int_vel
        except Exception as ex:
            print(ex)

    def translate_x(self, factor: float):
        self.translate(Vector2F(factor, 0))

    def translate_y(self, factor: float):
        self.translate(Vector2F(0, factor))

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
