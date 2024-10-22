from src.components.rigidbody import Rigidbody
from src.base.scene import Scene


class PhisycsCore:
    @staticmethod
    def handle(scene: Scene):
        for obj in scene.objects:
            rigidbody = obj.get_component(Rigidbody)
            if rigidbody:
                rigidbody.update()
