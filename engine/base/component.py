from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from engine.base.object import Object


class Component:
    def __init__(self):
        self.owner: Optional[Object] = None