from engine.base.common.point import Point, Pointed
from engine.base.common.vector import Vector2


class CPoint(Point):
    def __init__(self, offset: Vector2):
        super().__init__(offset)


class Collider(Pointed):
    def __init__(self):
        super().__init__()
