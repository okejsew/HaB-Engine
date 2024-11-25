from engine.base.object import Object
from engine.common.point import Point
from engine.common.vector import Vector2


class Camera(Object):
    def __init__(self):
        super().__init__()
        self.size = Vector2(120, 30)
        self.transform.position = Vector2(60, 15)
        self.name = 'Camera'
        self.region = self.get_region()

    def update(self):
        self.region = self.get_region()

    def get_region(self) -> tuple[Vector2, Vector2]:
        start = self.transform.position - self.size / 2
        end = start + self.size
        return start, end

    def in_region(self, p: Point) -> bool:
        cam_start, cam_end = self.region
        return (cam_start.x <= p.offset.x < cam_end.x) and (cam_start.y <= p.offset.y < cam_end.y)
