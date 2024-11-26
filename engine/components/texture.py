import re
from dataclasses import dataclass

from engine.common.point import Point, Pointed
from engine.common.vector import Vector2, Rotation
from engine.tools.debug import Debug

pattern = re.compile(r'^\s*(\S+)\s*;\s*(-?\d+)\s*,\s*(-?\d+)\s*$')


@dataclass
class TPoint(Point):
    sign: str

    def copy(self):
        return TPoint(self.offset.copy(), self.sign)


class Texture(Pointed):
    def __init__(self):
        super().__init__()
        self.points: list[TPoint] = []

    def get(self) -> list[TPoint]:
        return list(map(self.true_point, self.points))

    def true_point(self, point: TPoint):
        point_copy = point.copy()
        Rotation.apply_rotation(point_copy.offset, self.owner.transform.rotation)
        point_copy.offset += self.owner.transform.position
        return point_copy

    @staticmethod
    def load(path: str):
        texture = Texture()

        def parse_line(line: str):
            if not (line := line.strip()): return
            if match := pattern.match(line):
                sign, x, y = match.groups()
                texture.points.append(TPoint(Vector2(int(x), int(y)), sign))
            else:
                Debug.error(f'{line} <- Ошибка синтаксиса в файле {path}')

        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                parse_line(line)

        Debug.info(f'Загружена текстура из файла "{path}"')
        return texture
