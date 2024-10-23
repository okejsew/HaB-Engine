from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.base.object import BaseObject

class BaseComponent:
    def __init__(self):
        """Базовый класс для создания компонента"""
        self.owner: 'BaseObject' or None = None

    def __str__(self):
        return f'Component[t={self.__class__.__name__}]'
