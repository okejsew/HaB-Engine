from src.base.object import BaseObject
from src.components.texture import Texture, Point
from src.utils.vector import Vector2


class PositionPointTexture(Texture):
    def __init__(self):
        super().__init__()

    def get(self):
        pos = str(self.owner.transform.position)
        points: list[Point] = [Point('*', Vector2(0, 0))]
        for i in range(len(pos)):
            points.append(Point(pos[i], Vector2(i + 2, 0)))
        return self.convert_to_global(points)


class PositionPoint(BaseObject):
    def __init__(self):
        super().__init__()
        self.name = 'Position Point'
        self.add_component(PositionPointTexture())
