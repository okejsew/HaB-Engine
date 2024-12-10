from dataclasses import dataclass
from engine.data.point import Point


@dataclass
class TPoint(Point):
    sign: str

    def copy(self):
        return TPoint(self.vec.copy(), self.sign)