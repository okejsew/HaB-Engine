from src.base.component import Component
from src.base.utils.vector import Vector2


class Point:
    def __init__(self, offset: Vector2 = Vector2()):
        self.offset: Vector2 = offset

    def copy(self):
        return Point(self.offset.copy())


class Pointed(Component):
    def __init__(self):
        super().__init__()
        self.points: list[Point] = []

    def get(self) -> list[Point]:
        return self.points
