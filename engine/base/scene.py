from typing import TYPE_CHECKING, Type, Iterable
from engine.tools.typevar import T


class Scene:
    def __init__(self):
        from engine.base.camera import Camera
        self.objects: list['Object'] = []
        self.camera: Camera | None = Camera()
        self.add(self.camera)

    def add(self, obj: 'Object'):
        if obj not in self.objects:
            self.objects.append(obj)
            obj.scene = self

    def get_components(self, t: Type[T]) -> list[T]:
        components = []
        for obj in self:
            components += obj.get_components(t)
        return components

    def __iter__(self) -> Iterable['Object']:
        return iter(self.objects)


if TYPE_CHECKING:
    from engine.base.object import Object
