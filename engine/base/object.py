from typing import TYPE_CHECKING, TypeVar, Type, Optional

from engine.components.transform import Transform
from engine.tools.debug import Debug

if TYPE_CHECKING:
    from engine.base.component import Component
    from engine.base.scene import Scene

T = TypeVar('T')

class Object:
    def __init__(self):
        self.name = 'BaseObject'
        self.visible = True
        self.components: list[Component] = []
        self.transform = Transform()
        self.transform.owner = self
        self.scene: Optional[Scene] = None

    def add_component(self, component: 'Component'):
        for comp in self.components:
            if type(component) is type(comp):
                Debug.warn(f'Компонент типа {type(component)} уже добавлен')
                return
        self.components.append(component)
        component.owner = self

    def get_component(self, t: Type[T]) -> Optional[T]:
        for component in self.components:
            if isinstance(component, t):
                return component

    def get_components(self, t: Type[T]) -> list[Optional[T]]:
        components = []
        for component in self.components:
            if isinstance(component, t):
                components.append(component)
        return components
