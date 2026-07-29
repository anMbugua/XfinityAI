from abc import ABC
from datetime import datetime


class BaseService(ABC):

    def __init__(self, name: str):
        self.name = name
        self.running = False
        self.started_at = None

    def start(self):
        self.running = True
        self.started_at = datetime.now()

    def stop(self):
        self.running = False

    def status(self):
        return {
            "name": self.name,
            "running": self.running,
            "started_at": self.started_at,
        }

    def health(self):
        return {
            "healthy": self.running
        }
