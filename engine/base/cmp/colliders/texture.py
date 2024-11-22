from engine.base.cmp.collider import Collider
from engine.base.cmp.texture import Texture
from engine.base.common.point import Point
from engine.tools.debug import Debug


class TextureCollider(Collider):
    def __init__(self):
        super().__init__()

    def get(self) -> list[Point]:
        texture = self.owner.get_component(Texture)
        if texture:
            return texture.get()
        else:
            Debug.error('У объекта нет текстуры, коллайдер не может работать')
