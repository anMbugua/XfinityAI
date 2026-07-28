from abc import ABC, abstractmethod


class BaseTool(ABC):

    name = "unknown"


    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
