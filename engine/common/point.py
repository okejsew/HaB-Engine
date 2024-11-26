from dataclasses import dataclass

from engine.base.component import Component
from engine.common.vector import Vector2


@dataclass
class Point:
    offset: Vector2

    def copy(self):
        return Point(self.offset.copy())


class Pointed(Component):
    def __init__(self):
        super().__init__()
        self.points: list[Point] = []

    def get(self) -> list[Point]:
        return self.points
