from dataclasses import dataclass
from enum import Enum
from math import floor


@dataclass
class Vector2:
    x: int = 0
    y: int = 0

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, scalar: float):
        return Vector2(round(self.x * scalar), round(self.y * scalar))

    def __truediv__(self, scalar: float):
        return Vector2(round(self.x / scalar), round(self.y / scalar))

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        return not self == other

    def copy(self):
        return Vector2(self.x, self.y)

    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def direction(self):
        next_x = self.x / abs(self.x) if self.x != 0 else 0
        next_y = self.y / abs(self.y) if self.y != 0 else 0
        return Vector2F(next_x, next_y)


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

    def __add__(self, other):
        return Vector2F(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2F(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return Vector2F(abs(self.x), abs(self.y))

    def __mul__(self, scalar: float):
        return Vector2F(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float):
        return Vector2F(self.x / scalar, self.y / scalar)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        return not self == other

    def to_int(self):
        return Vector2(floor(self.x), floor(self.y))

    def __str__(self):
        return f"Vector2F({self.x}, {self.y})"

    def copy(self):
        return Vector2F(self.x, self.y)


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
