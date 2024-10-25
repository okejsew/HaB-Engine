from src.base.object import BaseObject
from src.base.scene import Scene
from src.utils.vector import in_region, Vector2


class UniversalCore:
    @staticmethod
    def destroy(obj: BaseObject):
        obj.scene.remove(obj)
        del obj

    @staticmethod
    def checking(obj: BaseObject):
        if not in_region(Vector2(-1000000000, -1000000000),
                         Vector2(1000000000, 1000000000), obj.position):
            UniversalCore.destroy(obj)

    @staticmethod
    def handle(scene: Scene):
        for obj in scene.objects:
            UniversalCore.checking(obj)