from typing import TYPE_CHECKING

from engine.base.common.point import Pointed, Point
from engine.base.common.vector import Vector2, Rotation
from engine.tools.debug import Debug

if TYPE_CHECKING:
    from engine.base.object import Object


class Collision:
    def __init__(self, obj: 'Object', point: Point, direction: Vector2):
        self.object, self.point, self.direction = obj, point, direction

class Collider(Pointed):
    def __init__(self):
        super().__init__()
        self.collisions: list[Collision] = []

    def add_collision(self, obj: 'Object', point: Point, direction: Vector2):
        self.collisions.append(Collision(obj, point, direction))

    def check_direction(self, direction: Vector2):
        self.calculate()
        for collision in self.collisions:
            if collision.direction == direction:
                return collision

    def calculate(self):
        self.collisions.clear()
        for obj in self.owner.scene.objects:
            if obj is self.owner: continue
            self.check(obj)

    def check(self, obj: 'Object'):
        collider = obj.get_component(Collider)
        if not collider: return
        for point1 in self.get():
            for point2 in collider.get():
                self._check(point1, point2, obj)

    def _check(self, point1: Point, point2: Point, obj: 'Object'):
        def __check(direction: Vector2):
            try:
                if point1.offset + direction == point2.offset:
                    self.add_collision(obj, point1, direction)
            except Exception as ex:
                Debug.error(str(ex))

        __check(Rotation.default.value)
        __check(Rotation.right.value)
        __check(Rotation.left.value)
        __check(Rotation.down.value)
