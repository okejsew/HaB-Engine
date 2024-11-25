from engine.components.collider import Collider
from engine.components.texture import Texture, TPoint
from engine.tools.debug import Debug


class TextureCollider(Collider):
    def __init__(self):
        super().__init__()

    def get(self) -> list[TPoint]:
        texture = self.owner.get_component(Texture)
        if texture:
            return texture.get()
        else:
            Debug.error('У объекта нет текстуры, коллайдер не может работать')
