from dataclasses import dataclass
from typing import TYPE_CHECKING

from engine.data import Point
from engine.math import Vector2

if TYPE_CHECKING:
    from engine.base.object import Object


@dataclass
class Collision:
    obj: 'Object'
    self_point: Point
    collision_point: Point
    direction: Vector2
