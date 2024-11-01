from typing import TYPE_CHECKING, TypeVar, Type, Optional

from src.components.transform import Transform
from src.utils.error import Errors

if TYPE_CHECKING:
    from src.base.component import BaseComponent
    from src.base.scene import Scene

T = TypeVar('T')


class BaseObject:
    def __init__(self):
        self.name: str = 'BaseObject'
        self.visible: bool = True
        self.components: list[BaseComponent] = []
        self.transform: Transform = Transform()
        self.scene: Optional[Scene] = None

    def add_component(self, component: 'BaseComponent'):
        for comp in self.components:
            if type(component) is type(comp):
                Errors.add(f'Warning: Component with type {type(component)} already added')
                return
        self.components.append(component)
        component.owner = self

    def get_component(self, t: Type[T]) -> Optional[T]:
        for component in self.components:
            if isinstance(component, t):
                return component
