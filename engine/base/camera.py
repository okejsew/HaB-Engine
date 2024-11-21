from engine.base.cmp.texture import TPoint
from engine.base.common.point import Point
from engine.base.common.vector import Vector2, Rotation
from engine.base.object import Object


class Camera(Object):
    def __init__(self):
        super().__init__()
        self.size: Vector2 = Vector2(120, 30)
        self.transform.position = Vector2(60, 15)
        self.name = 'Camera'

        self.__offset: Vector2 = self.get_offset()
        self.__region: tuple[Vector2, Vector2] = self.get_region()

    def update(self):
        self.__offset = self.get_offset()
        self.__region = self.get_region()

    def get_region(self) -> tuple[Vector2, Vector2]:
        start = self.transform.position - self.size / 2
        end = start + self.size
        return start, end

    def get_offset(self) -> Vector2:
        return self.transform.position - (self.size / 2)

    def true_point(self, p: Point, obj: Object) -> TPoint:
        point = p.copy()
        Rotation.apply_rotation(point.offset, obj.transform.rotation)
        point.offset += obj.transform.position + self.__offset
        return point

    def in_region(self, p: Point) -> bool:
        cam_start, cam_end = self.__region
        return (cam_start.x < p.offset.x < cam_end.x) and (cam_start.y <= p.offset.y < cam_end.y)
