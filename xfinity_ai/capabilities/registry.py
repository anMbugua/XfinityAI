from .capability import Capability


class CapabilityRegistry:

    def __init__(self):
        self._capabilities = {}

    def register(self, capability: Capability):
        self._capabilities[capability.name] = capability

    def unregister(self, name):
        self._capabilities.pop(name, None)

    def get(self, name):
        return self._capabilities.get(name)

    def list(self):
        return list(self._capabilities.values())

    def categories(self):
        return sorted(
            set(c.category for c in self._capabilities.values())
        )

    def by_category(self, category):
        return [
            c for c in self._capabilities.values()
            if c.category == category
        ]
