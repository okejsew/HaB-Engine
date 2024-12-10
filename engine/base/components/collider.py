from typing import TYPE_CHECKING

from engine.base.components.texture import Texture
from engine.base.components.pointed import Pointed
from engine.data import Collision, Point, TPoint
from engine.math import Vector2, Rotation

if TYPE_CHECKING:
    from engine.base.object import Object


class Collider(Pointed):
    def __init__(self):
        super().__init__()
        self.collisions: list[Collision] = []

    def get(self) -> list[TPoint]:
        if texture := self.owner.get_component(Texture):
            return texture.get()
        else:
            self.owner.remove_component(self)
            return []

    def check_direction(self, direction: Vector2):
        self.calculate()
        for collision in self.collisions:
            if collision.direction == direction:
                return collision

    def calculate(self):
        self.collisions.clear()
        if not self.get(): return
        for obj in self.owner.scene:
            if obj is not self.owner:
                self.check(obj)

    def check(self, obj: 'Object'):
        if collider := obj.get_component(Collider):
            self.check_object(collider)

    def check_object(self, collider: 'Collider'):
        if not collider.get(): return
        for point1 in self.get():
            for point2 in collider.get():
                self.check_point(point1, point2, collider.owner)

    def check_point(self, point1: Point, point2: Point, obj: 'Object'):
        for direction in [Rotation.default, Rotation.right, Rotation.left, Rotation.down]:
            if point1.vec + direction.value == point2.vec:
                c = Collision(obj, point1, point2, direction.value)
                self.collisions.append(c)
