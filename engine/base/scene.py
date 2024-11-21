from typing import Optional

from engine.base.camera import Camera
from engine.base.object import Object


class Scene:
    def __init__(self, name: str = 'Scene'):
        self.name: str = name
        self.objects: list[Object] = []
        self.camera: Optional[Camera] = Camera()
        self.add(self.camera)

    def add(self, obj: Object):
        if obj not in self.objects:
            self.objects.append(obj)
            obj.scene = self

    def get(self, name: str) -> Object:
        for obj in self.objects:
            if obj.name == name:
                return obj

    def remove(self, obj: Object):
        if obj in self.objects:
            self.objects.remove(obj)
