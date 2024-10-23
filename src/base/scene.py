from src.assets.objects.camera import Camera
from src.base.errors import ObjectNotFound
from src.base.errors import ObjectAlreadyAdded
from src.base.object import BaseObject


class Scene:
    def __init__(self):
        """
        Сцена - просто коробка для хранения объектов\n
        Но также есть camera, отвечает за текущую камеру, которой как раз таки и будет всё отрисовываться
        """
        self.objects: list[BaseObject] = []
        self.camera: Camera | None = Camera()
        self.objects.append(self.camera)

    def add(self, obj: BaseObject):
        if obj not in self.objects:
            self.objects.append(obj)
            obj.scene = self
        else: ObjectAlreadyAdded(obj, self)

    def get(self, name: str) -> BaseObject:
        for obj in self.objects:
            if obj.name == name:
                return obj
        ObjectNotFound(name, self)

    def remove(self, obj: BaseObject):
        if obj in self.objects:
            self.objects.remove(obj)
        else: ObjectNotFound(obj, self)
