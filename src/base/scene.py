from src.base.errors import ObjectNotFound
from src.base.errors import ObjectAlreadyAdded
from src.base.object import BaseObject


class Scene:
    def __init__(self):
        self.objects: list[BaseObject] = []

    def add(self, obj: BaseObject):
        if obj not in self.objects:
            self.objects.append(obj)
        else:
            raise ObjectAlreadyAdded(obj, self)

    def remove(self, obj: BaseObject):
        if obj in self.objects:
            self.objects.remove(obj)
        else:
            raise ObjectNotFound(obj, self)
