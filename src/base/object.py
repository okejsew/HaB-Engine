from typing import TYPE_CHECKING, TypeVar, Type, Optional

from src.base.errors import ComponentNotFound
from src.utils.vector import Vector2

if TYPE_CHECKING:
    from src.base.component import BaseComponent
    from src.base.scene import Scene

T = TypeVar('T')

class BaseObject:
    def __init__(self):
        """
        Базовый класс для объекта в движке\n
        name -- Имя объекта, отображается при дебаггинге\n
        visible -- будет ли объект отрисовываться (если у него конечно есть текстура)\n
        Можно добавлять, убирать и получать компоненты в зависимости от надобности
        """
        self.name: str = 'BaseObject'
        self.visible: bool = True
        self.__components: list['BaseComponent'] = []
        self.position: Vector2 = Vector2()
        self.scene: 'Scene' or None = None

    def add_component(self, component: 'BaseComponent'):
        if component not in self.__components:
            self.__components.append(component)
            component.owner = self

    def get_component(self, t: Type[T]) -> Optional[T] | None:
        for component in self.__components:
            if isinstance(component, t):
                return component

    def remove_component(self, component: 'BaseComponent'):
        for c in self.__components:
            if c is component:
                self.__components.remove(c)
                return
        ComponentNotFound(component, self)

    def __str__(self):
        return f'BaseObject[{self.name=}]'
