from engine.components.collider import Collider
from engine.components.texture import Texture, TPoint
from engine.tools.debug import Debug


class TextureCollider(Collider):
    def __init__(self):
        super().__init__()

    def get(self) -> list[TPoint]:
        if texture := self.owner.get_component(Texture):
            return texture.get()
        else:
            Debug.error('У объекта нет текстуры, коллайдер не может работать')
            self.owner.remove_component(self)
            return []
