import time
from threading import Thread

from engine.base.scene import Scene
from engine.base.components import Rigidbody

scene: Scene | None
thread: Thread | None
state: dict[str, bool]


def update():
    for rigidbody in scene.get_components(Rigidbody):
        rigidbody.update()
    time.sleep(0.016)


def _thread():
    while state['work']:
        update()


def __init__(_scene: Scene, _state: dict):
    global scene, thread, state
    scene = _scene
    thread = Thread(target=_thread)
    state = _state
