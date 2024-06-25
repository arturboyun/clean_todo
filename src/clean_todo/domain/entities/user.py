from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class User:
    id: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    username: str
