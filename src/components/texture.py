from src.base.component import BaseComponent
from src.base.errors import TextureFileSyntaxIncorrect
from src.utils.vector import Vector2

class Point:
    def __init__(self, sign: str, offset: Vector2):
        self.sign: str = sign
        self.offset: Vector2 = offset
        color: str = 'white'

class Texture(BaseComponent):
    def __init__(self):
        super().__init__()
        self.__points: list[Point] = []

    def get(self):
        # Пока возвращаю текстуру, как она есть
        return self.__points

    def add_point(self, point: Point):
        self.__points.append(point)

    def load(self, path: str):
        self.__points.clear()
        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                if line.strip():
                    try:
                        sign, pos = line.split(';')
                        x, y = pos.split(',')
                    except ValueError: raise TextureFileSyntaxIncorrect(line)
                    else: self.__points.append(Point(sign.strip(), Vector2(int(x), int(y))))

