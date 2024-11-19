from src.base.utils.point import Point, Pointed
from src.base.utils.vector import Vector2
from src.tools.debug import Debug


class TPoint(Point):
    def __init__(self, sign: str, offset: Vector2):
        super().__init__(offset)
        self.sign: str = sign

    def copy(self):
        return TPoint(self.sign, self.offset.copy())


class Texture(Pointed):
    def __init__(self):
        super().__init__()

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
                    txt.points.append(TPoint(sign.strip(), Vector2(int(x), int(y))))
                except ValueError:
                    Debug.error(f'Error while parsing texure >>> {line} <<<')
        return txt
