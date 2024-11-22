from typing import Optional, TYPE_CHECKING

from engine.base.common.point import Pointed, Point
from engine.base.common.vector import Vector2, Rotation
from engine.tools.debug import Debug

if TYPE_CHECKING:
    from engine.base.object import Object


class Collision:
    def __init__(self, obj: 'Object', point: Point, direction: Vector2):
        self.object: Optional[Object] = obj
        self.point: Point = point
        self.direction: Vector2 = direction


class Collider(Pointed):
    def __init__(self):
        super().__init__()
        self.points.append(Point(Vector2(0, 0)))
        self.collisions: list[Collision] = []
        self._object_: Optional[Object] = None

    def add_collision(self, obj: 'Object', point: Point, direction: Vector2):
        self.collisions.append(Collision(obj, point, direction))

    def check_direction(self, direction: Vector2):
        self.calculate()
        for collision in self.collisions:
            if collision.direction == direction:
                return collision

    def calculate(self):
        self.collisions.clear()
        objects = self.owner.scene.objects.copy()
        try:
            objects.remove(self.owner)
        except ValueError:
            pass
        for obj in objects:
            self._object_ = obj
            collider = obj.get_component(Collider)
            if not collider: continue
            for point1 in self.get():
                for point2 in collider.get():
                    self.check(point1, point2)

    def check(self, point1: Point, point2: Point):
        def _check(direction: Vector2):
            try:
                if point1.offset + direction == point2.offset:
                    self.add_collision(self._object_, point1, direction)
            except Exception as ex:
                Debug.error(str(ex))

        _check(Rotation.default.value)
        _check(Rotation.right.value)
        _check(Rotation.left.value)
        _check(Rotation.down.value)
