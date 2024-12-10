from dataclasses import dataclass

from engine.math import Vector2


@dataclass
class Point:
    vec: Vector2

    def copy(self):
        return Point(self.vec.copy())