from src.base.object import BaseObject
from src.components.texture import Texture, Point
from src.utils.vector import Vector2


class PositionPointTexture(Texture):
    def __init__(self):
        """
        Текстура для позиционной точки\n
        Всё просто - каждый раз как рендеркор запрашивает готовые точки текстуры,
        этот компонент возвращает точки в виде надписи координат объекта\n
        Простой пример написания своей текстуры
        """
        super().__init__()

    def get(self):
        pos = str(self.owner.position)
        points: list[Point] = [Point('*', Vector2(0, 0))]
        for i in range(len(pos)):
            points.append(Point(pos[i], Vector2(i+20, 10)))
        return points

class PositionPoint(BaseObject):
    def __init__(self):
        """Объект, который выглядит как точка и рядом с ней ее координаты"""
        super().__init__()
        self.name = 'Position Point'
        self.add_component(PositionPointTexture())