from dataclasses import dataclass, field
from uuid import uuid4

from clean_todo.domain.exceptions.business import BusinessError


@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    name: str
    description: str | None = None
    done: bool = False
    parent_id: str | None = None

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise BusinessError("Task name must be a string")
        
        if self.description is not None and not isinstance(self.description, str):
            raise BusinessError("Task description must be a string")
        
        if not isinstance(self.done, bool):
            raise BusinessError("Task done must be a boolean")
        
        if self.parent_id is not None and not isinstance(self.parent_id, str):
            raise BusinessError("Task parent_id must be a string")
        
        if self.parent_id is not None and self.parent_id == self.id:
            raise BusinessError("Task cannot be parent of itself")
