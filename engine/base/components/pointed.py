from engine.base.component import Component
from engine.data import Point


class Pointed(Component):
    def __init__(self):
        super().__init__()
        self.points: list[Point] = []

    def get(self) -> list[Point]:
        return self.points
