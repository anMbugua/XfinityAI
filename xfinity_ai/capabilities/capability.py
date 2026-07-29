from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Capability:
    name: str
    category: str
    description: str

    permissions: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)

    enabled: bool = True

    def info(self):
        return {
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "permissions": self.permissions,
            "tags": self.tags,
            "enabled": self.enabled,
        }
