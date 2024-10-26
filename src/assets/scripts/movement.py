from typing import Optional

from src.base.animator import Animator
from src.base.script import Script
from src.components.texture import Texture
from src.utils.input import Input


class BasicMovement(Script):
    def __init__(self):
        super().__init__()
        self.animator: Optional[Animator] = None
        self.texture: Optional[Texture] = None

    def awake(self):
        self.animator = self.owner.get_component(Animator)

    def fixed_update(self):
        key = Input.get_key()
        if key == ord('a'):
            self.owner.position.x -= 1
            if not self.animator.is_animating:
                self.animator.start()
        if key == ord('d'):
            self.owner.position.x += 1
            if not self.animator.is_animating:
                self.animator.start()
        if key == ord('w'):
            self.owner.position.y -= 1
            if not self.animator.is_animating:
                self.animator.start()
        if key == ord('s'):
            self.owner.position.y += 1
            if not self.animator.is_animating:
                self.animator.start()
        if key == -1:
            if self.animator.is_animating:
                self.animator.is_animating = False
                # self.texture.load('src/assets/textures/test.tx')
