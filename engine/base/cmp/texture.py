import re

from engine.base.common.point import Point, Pointed
from engine.base.common.vector import Vector2
from engine.tools.debug import Debug

pattern = re.compile(r'^\s*(\S+)\s*;\s*(-?\d+)\s*,\s*(-?\d+)\s*$')


class TPoint(Point):
    def __init__(self, sign: str, offset: Vector2):
        super().__init__(offset)
        self.sign: str = sign

    def copy(self):
        return TPoint(self.sign, self.offset.copy())


class Texture(Pointed):
    def __init__(self):
        super().__init__()
        self.points: list[TPoint] = []

    def get(self) -> list[TPoint]:
        return self.points

    @staticmethod
    def load(path: str):
        texture = Texture()

        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                line = line.strip()
                if not line: continue
                match = pattern.match(line)
                if not match:
                    Debug.error(f'Texture file syntax error >>> {line} <<<')
                else:
                    sign, x, y = match.groups()
                    texture.points.append(TPoint(sign, Vector2(int(x), int(y))))
        Debug.warn(f'Загружена текстура из файла "{path}"')
        return texture
