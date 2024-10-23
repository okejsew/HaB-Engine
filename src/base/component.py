from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.base.object import BaseObject

class BaseComponent:
    def __init__(self):
        """
        Базовый класс для создания компонента\n
        """
        self.owner: 'BaseObject | None' = None

    def set_owner(self, owner: 'BaseObject'):
        self.owner = owner

    def __str__(self):
        return f'Component[t={self.__class__.__name__}]'
