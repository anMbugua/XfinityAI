from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Message:

    role: str
    content: str
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()


    def to_dict(self):

        return asdict(self)
