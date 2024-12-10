import re

from engine.base.components.pointed import Pointed
from engine.data import TPoint
from engine.math import Vector2, Rotation

pattern = re.compile(r'^\s*(\S+)\s*;\s*(-?\d+)\s*,\s*(-?\d+)\s*$')


class Texture(Pointed):
    def __init__(self):
        super().__init__()
        self.points: list[TPoint] = []

    def get(self) -> list[TPoint]:
        return list(map(self.true_point, self.points))

    def true_point(self, point: TPoint):
        point_copy = point.copy()
        Rotation.apply_rotation(point_copy.vec, self.owner.transform.rotation)
        point_copy.vec += self.owner.transform.position
        return point_copy

    @staticmethod
    def load(path: str):
        texture = Texture()

        def parse_line(line: str):
            if not (line := line.strip()): return
            if match := pattern.match(line):
                sign, x, y = match.groups()
                texture.points.append(TPoint(Vector2(int(x), int(y)), sign))

        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                parse_line(line)

        return texture
