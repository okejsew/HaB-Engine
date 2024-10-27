from typing import TYPE_CHECKING, TypeVar, Type, Optional

from src.base.errors import ComponentNotFound
from src.utils.vector import Vector2

if TYPE_CHECKING:
    from src.base.component import BaseComponent
    from src.base.scene import Scene

T = TypeVar('T')


class BaseObject:
    def __init__(self):
        self.name: str = 'BaseObject'
        self.visible: bool = True
        self.components: list['BaseComponent'] = []
        self.position: Vector2 = Vector2()
        self.scene: 'Scene' or None = None

    def add_component(self, component: 'BaseComponent'):
        if component not in self.components:
            self.components.append(component)
            component.owner = self

    def get_component(self, t: Type[T]) -> Optional[T]:
        for component in self.components:
            if isinstance(component, t):
                return component

    def get_components(self, t: Type[T]) -> list[Optional[T]]:
        result: list[Optional[T]] = []
        for component in self.components:
            if isinstance(component, t):
                result.append(component)
        return result

    def remove_component(self, component: 'BaseComponent', ignore: bool = False):
        for c in self.components:
            if c is component:
                return self.components.remove(c)
        if ignore: ComponentNotFound(component, self)

    def __str__(self):
        return f'BaseObject[{self.name=}]'
