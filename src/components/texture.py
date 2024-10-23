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
        self._points: list[Point] = []

    def get(self) -> list[Point]:
        """Возвращает текстуру по параметрам (например, размер), но пока ничего.
        Как бы должен обновлять выводимую текстуру для как раз таки вывода"""
        return self._convert_to_global()

    def _convert_to_global(self) -> list[Point]:
        """Переводит все точки в глобальную систему координат"""
        return [Point(p.sign, p.offset + self.owner.position) for p in self._points]

    def add_point(self, point: Point):
        self._points.append(point)

    def load(self, path: str):
        self._points.clear()
        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                if line.strip():
                    try:
                        sign, pos = line.split(';')
                        x, y = pos.split(',')
                    except ValueError: raise TextureFileSyntaxIncorrect(line)
                    else: self._points.append(Point(sign.strip(), Vector2(int(x), int(y))))
