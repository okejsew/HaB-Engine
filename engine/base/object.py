from typing import Type, TYPE_CHECKING
from engine.tools.typevar import T
from engine.base.components import Transform


class Object:
    def __init__(self):
        self.name = 'BaseObject'
        self.visible = True
        self.components: list[Component] = []
        self.transform = Transform()
        self.transform.owner = self
        self.scene: Scene | None = None

    def remove_component(self, component: 'Component'):
        if component in self.components:
            self.components.remove(component)

    def add_component(self, component: 'Component'):
        for comp in self.components:
            if type(component) is type(comp):
                return
        self.components.append(component)
        component.owner = self

    def get_component(self, t: Type[T]) -> T | None:
        for component in self.components:
            if isinstance(component, t):
                return component

    def get_components(self, t: Type[T]) -> list[T]:
        components = []
        for component in self.components:
            if isinstance(component, t):
                components.append(component)
        return components


if TYPE_CHECKING:
    from engine.base.component import Component
    from engine.base.scene import Scene
