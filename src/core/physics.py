import time

from src.components.rigidbody import Rigidbody
from src.base.scene import Scene


class PhisycsCore:
    """
    Ядро физики движка\n

    По сути всё просто - вызывается метод handle, и он обрабатывает
    все объекты на сцене у которых есть компонент Rigidbody
    """
    frame_time: float = time.time()

    @staticmethod
    def handle(scene: Scene):
        """
        Тут еще проще\n
        scene -- Сцена, которую нужно обработать\n
        Вызывает у всех объектов, у которых есть Rigidbody, его метод update
        """
        start_time = time.time()
        for obj in scene.objects:
            rigidbody = obj.get_component(Rigidbody)
            if rigidbody:
                rigidbody.update()
        PhisycsCore.frame_time = time.time() - start_time
