from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.base.object import BaseObject

class BaseComponent:
    def __init__(self):
        """Базовый класс для создания компонента"""
        self.owner: Optional['BaseObject'] = None

    def __str__(self):
        return f'Component[t={self.__class__.__name__}]'
