from src.base.component import BaseComponent
from src.base.errors import TextureFileSyntaxIncorrect
from src.utils.vector import Vector2

class Point:
    def __init__(self, sign: str, offset: Vector2):
        self.sign: str = sign
        self.offset: Vector2 = offset

    def __str__(self):
        return f'Point[pos={self.offset}, sign={self.sign}]'

class Texture(BaseComponent):
    def __init__(self):
        super().__init__()
        self.points: list[Point] = []

    def get(self) -> list[Point]:
        return self.convert_to_global(self.points)

    def convert_to_global(self, points: list[Point]) -> list[Point]:
        return [Point(p.sign, p.offset + self.owner.position) for p in points]

    def load(self, path: str):
        self.points.clear()
        file = open(path, 'r', encoding='utf-8')
        for line in file.readlines():
            if not line.strip(): continue
            try:
                sign, pos = line.split(';')
                x, y = pos.split(',')
            except ValueError: TextureFileSyntaxIncorrect(line)
            else: self.points.append(Point(sign.strip(), Vector2(int(x), int(y))))
        file.close()
