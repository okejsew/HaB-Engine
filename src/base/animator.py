import time
from threading import Thread
from typing import Optional

from src.base.component import BaseComponent
from src.base.errors import AnimationFileSyntaxIncorrect
from src.components.texture import Point, Texture
from src.utils.vector import Vector2


class Frame:
    def __init__(self):
        self.points: list[Point] = []
        self.time: float = 0


class Animator(BaseComponent):
    def __init__(self):
        super().__init__()
        self.loop: int = 1
        self.frames: list[Frame] = []
        self.is_animating: bool = False
        self.thread: Optional[Thread] = None

    def load(self, path: str):
        file = open(path, 'r', encoding='utf-8')

        current_frame = Frame()
        for line in file.readlines():
            line = line.strip()
            if line == '':
                continue
            elif line.startswith('#'):
                current_frame.time = float(line.replace('#', ''))
                self.frames.append(current_frame)
                current_frame = Frame()
            else:
                try:
                    sign, pos = line.split(';')
                    x, y = pos.split(',')
                except ValueError:
                    AnimationFileSyntaxIncorrect(line)
                else:
                    current_frame.points.append(Point(sign.strip(), Vector2(int(x), int(y))))

        file.close()

    def end(self):
        self.is_animating = False

    def start(self):
        self.is_animating = True
        Thread(target=self.animating).start()

    def set_frame(self, frame: Frame):
        t = self.owner.get_component(Texture)
        if t: t.points = frame.points.copy()

    def animating(self):
        def do_anim():
            for frame in self.frames:
                self.set_frame(frame)
                time.sleep(frame.time)

        if self.loop == -1:
            while self.is_animating:
                do_anim()
        else:
            i = 0
            while i < self.loop:
                if not self.is_animating:
                    break
                do_anim()
                i += 1
