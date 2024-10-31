from typing import Optional

from src.base.camera import Camera
from src.base.object import BaseObject


class Scene:
    def __init__(self):
        self.objects: list[BaseObject] = []
        self.camera: Optional[Camera] = Camera()
        self.objects.append(self.camera)

    def add(self, obj: BaseObject):
        if obj not in self.objects:
            self.objects.append(obj)
            obj.scene = self

    def get(self, name: str) -> BaseObject:
        for obj in self.objects:
            if obj.name == name:
                return obj

    def remove(self, obj: BaseObject):
        if obj in self.objects:
            self.objects.remove(obj)

scene = Scene()
