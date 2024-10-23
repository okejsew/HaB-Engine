from src.base.component import BaseComponent
from src.base.errors import TextureFileSyntaxIncorrect
from src.utils.vector import Vector2

class Point:
    def __init__(self, sign: str, offset: Vector2):
        """
        Точка текстуры\n
        sign -- ее как бы знак, символ, что вполне логично\n
        offset -- позиция относительно центра объекта (формально),
        так может быть просто позицией в мире, просто названа офсет\n
        т.е. если Point('@', Vector2(0, -1)), то точка @ будет на одну клетку выше центра объекта
        """
        self.sign: str = sign
        self.offset: Vector2 = offset

    def __str__(self):
        return f'Point[pos={self.offset}, sign={self.sign}]'

class Texture(BaseComponent):
    def __init__(self):
        """
        Компонент текстуры\n
        Можно пользоваться базовым функционалом, а можно
        наследоваться от этого класса и создавать свой рендер текстуры,
        переопределяя метод get - он должен возвращать текстуру как она выглядит в мире\n
        Например, можно создать кубик, размер текстуры которого будет зависеть от его размера
        (создать доп. поле например). Вообщем, хоть шейдеры пишите\n
        __points нужен для хранения загруженной текстуры, а вообще можете спокойно
        им не пользоваться, как например в PosPoint, там текстура зависит от позиции объекта
        """
        super().__init__()
        self.points: list[Point] = []

    def get(self) -> list[Point]:
        """Возвращает текстуру как она выглядит в мире"""
        return self._convert_to_global(self.points)

    def _convert_to_global(self, points: list[Point]) -> list[Point]:
        """Переводит точки в глобальную систему координат, в зависимости от позиции объекта"""
        return [Point(p.sign, p.offset + self.owner.position) for p in points]

    def load(self, path: str):
        self.points.clear()
        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                if not line.strip():
                    continue
                try:
                    sign, pos = line.split(';')
                    x, y = pos.split(',')
                except ValueError: raise TextureFileSyntaxIncorrect(line)
                else: self.points.append(Point(sign.strip(), Vector2(int(x), int(y))))
