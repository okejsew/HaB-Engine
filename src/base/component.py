from typing import TYPE_CHECKING, Callable

from src.base.errors import MissingOwnerError

if TYPE_CHECKING:
    from src.base.object import BaseObject

class BaseComponent:
    def __init__(self):
        self.owner: 'BaseObject | None' = None

    def set_owner(self, owner: 'BaseObject'):
        self.owner = owner

    @staticmethod
    def check_owner(func: Callable) -> Callable:
        def wrapper(self, *args, **kwargs):
            if self.owner is None:
                raise MissingOwnerError(func, self)
            return func(self, *args, **kwargs)
        return wrapper

    def __str__(self):
        return f'Component[t={self.__class__.__name__}]'
