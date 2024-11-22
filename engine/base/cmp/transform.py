from engine.base.cmp.collider import Collider
from engine.base.cmp.rigidbody import Rigidbody
from engine.base.common.vector import Vector2, Vector2F, Rotation
from engine.base.component import Component
from engine.tools.debug import Debug


class Transform(Component):
    def __init__(self):
        super().__init__()
        self.position: Vector2 = Vector2()
        self.rotation: Rotation = Rotation.default
        self.moving_remainder: Vector2 = Vector2()

    def translate(self, delta: Vector2 | Vector2F):
        try:
            collider = self.owner.get_component(Collider)
            rigidbody = self.owner.get_component(Rigidbody)
            if collider:
                collision = collider.check_direction(Vector2(delta.x / abs(delta.x) if delta.x != 0 else 0,
                                                             delta.y / abs(delta.y) if delta.y != 0 else 0))
                if collision:
                    if rigidbody:
                        rigidbody.acceleration = 0
                    Debug.warn(
                        f'Не удается пройти: {collision.object.transform.position}, {collision.direction}, {collision.point.offset}')
                    return
            delta = Vector2F(self.moving_remainder.x + delta.x, self.moving_remainder.y + delta.y)
            int_vel = delta.to_int()
            self.moving_remainder = delta - int_vel
            self.position += int_vel
        except Exception as ex:
            Debug.error(str(ex))

    def translateX(self, factor: float):
        self.translate(Vector2F(factor, 0))

    def translateY(self, factor: float):
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
