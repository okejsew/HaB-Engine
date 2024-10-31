from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.base.object import BaseObject


class BaseComponent:
    def __init__(self):
        self.owner: Optional[BaseObject] = None
