from src.base.component import BaseComponent
from src.utils.error import Errors
from src.utils.vector import Vector2


class Point:
    def __init__(self, sign: str, offset: Vector2):
        self.sign: str = sign
        self.offset: Vector2 = offset

    def __str__(self):
        return f'Point[pos={self.offset}, sign={self.sign}]'

    def copy(self):
        return Point(self.sign, self.offset.copy())


class Texture(BaseComponent):
    def __init__(self):
        super().__init__()
        self.points: list[Point] = []

    def get(self) -> list[Point]:
        return self.points


class TextureFabric:
    @staticmethod
    def load(path: str):
        txt = Texture()
        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                line = line.strip('\n')
                if not line.strip(): continue
                try:
                    sign, pos = line.split(';')
                    x, y = pos.split(',')
                    txt.points.append(Point(sign.strip(), Vector2(int(x), int(y))))
                except ValueError:
                    Errors.add(f'Error while parsing texure >>> {line} <<<')

        return txt
