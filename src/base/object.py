from typing import TYPE_CHECKING, TypeVar, Type, Optional

from src.components.transform import Transform
from src.base.errors import ComponentNotFound

if TYPE_CHECKING:
    from src.base.component import BaseComponent

T = TypeVar('T')

class BaseObject:
    def __init__(self):
        self.name: str = 'BaseObject'
        self.visible: bool = True
        self.__components: list['BaseComponent'] = []
        self.transform = Transform()
        self.transform.set_owner(self)

    def add_component(self, component: 'BaseComponent'):
        if component not in self.__components and not isinstance(component, Transform):
            self.__components.append(component)
            component.set_owner(self)

    def get_component(self, t: Type[T]) -> Optional[T]:
        for component in self.__components:
            if isinstance(component, t):
                return component
        raise ComponentNotFound(t, self)

    def remove_component(self, component: 'BaseComponent'):
        for c in self.__components:
            if c is component:
                self.__components.remove(c)
                return
        raise ComponentNotFound(component, self)

    def __str__(self):
        return f'BaseObject[{self.name=}]'
