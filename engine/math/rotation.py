from enum import Enum

from engine.math.vector2 import Vector2


class Rotation(Enum):
    default = Vector2(0, -1)
    down = Vector2(0, 1)
    left = Vector2(-1, 0)
    right = Vector2(1, 0)

    @staticmethod
    def apply_rotation(offset: Vector2, rotation: 'Rotation'):
        match rotation:
            case Rotation.default:
                offset.x, offset.y = offset.x, offset.y
            case Rotation.left:
                offset.x, offset.y = offset.y, -offset.x
            case Rotation.right:
                offset.x, offset.y = -offset.y, offset.x
            case Rotation.down:
                offset.x, offset.y = -offset.x, -offset.y
