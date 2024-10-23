from src.base.object import BaseObject
from src.components.texture import Texture, Point
from src.utils.vector import Vector2


class PositionPointTexture(Texture):
    def __init__(self):
        super().__init__()
        self.add_point(Point('*', Vector2(0, 0)))

    def get(self):
        pos = str(self.owner.position)
        self._points.clear()
        self._points.append(Point('*', Vector2(0, 0)))
        for i in range(len(pos)):
            self.add_point(Point(pos[i], Vector2(i+2, 0)))
        return self._convert_to_global()

class PositionPoint(BaseObject):
    def __init__(self):
        super().__init__()
        self.name = 'Position Point'
        self.add_component(PositionPointTexture())