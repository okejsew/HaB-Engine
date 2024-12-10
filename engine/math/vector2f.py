from dataclasses import dataclass
from math import floor
from typing import Self
from engine.math.vector2 import Vector2

@dataclass
class Vector2F:
    x: float = 0
    y: float = 0

    def direction(self):
        next_x = self.x / abs(self.x) if self.x != 0 else 0
        next_y = self.y / abs(self.y) if self.y != 0 else 0
        return Vector2F(next_x, next_y)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalized(self):
        vec_length = self.length()
        if vec_length != 0:
            return Vector2F(self.x / vec_length, self.y / vec_length)  # Нормализуем
        return Vector2F()

    def __sub__(self, other):
        return Vector2F(self.x - other.x, self.y - other.y)

    def __iadd__(self, other: Self):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, scalar: float):
        return Vector2F(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float):
        return Vector2F(self.x / scalar, self.y / scalar)

    def to_int(self):
        return Vector2(floor(self.x), floor(self.y))

    def __repr__(self):
        return f"Vector2F({self.x}, {self.y})"
