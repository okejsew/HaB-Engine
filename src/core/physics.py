import time

from src.components.rigidbody import Rigidbody


class PhisycsCore:
    @staticmethod
    def thread():
        from src.engine import Engine
        while Engine.is_working:
            for obj in Engine.current_scene.objects:
                rigidbody = obj.get_component(Rigidbody)
                if rigidbody: rigidbody.update()
            time.sleep(0.016)
