from math import floor


class Vector2:
    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y

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

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"

class Vector2F:
    def __init__(self, x: float = 0, y: float = 0):
        self.x: float = x
        self.y: float = y

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

class Direction:
    up = Vector2(0, -1)
    down = Vector2(0, 1)
    right = Vector2(1, 0)
    left = Vector2(-1, 0)