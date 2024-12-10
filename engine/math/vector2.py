from dataclasses import dataclass
from typing import Self

@dataclass
class Vector2:
    x: int = 0
    y: int = 0

    def __add__(self, other: Self):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self):
        return Vector2(self.x - other.x, self.y - other.y)

    def __truediv__(self, scalar: float):
        return Vector2(round(self.x / scalar), round(self.y / scalar))

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def copy(self):
        return Vector2(self.x, self.y)

    def direction(self):
        next_x = self.x / abs(self.x) if self.x != 0 else 0
        next_y = self.y / abs(self.y) if self.y != 0 else 0
        return Vector2(next_x, next_y)
