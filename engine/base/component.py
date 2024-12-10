class Component:
    def __init__(self):
        self.owner: Object | None = None


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.base.object import Object
