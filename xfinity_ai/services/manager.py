from typing import Dict

from .base import BaseService


class ServiceManager:

    def __init__(self):
        self._services: Dict[str, BaseService] = {}

    def register(self, service: BaseService):
        self._services[service.name] = service

    def get(self, name):
        return self._services.get(name)

    def start_all(self):

        for service in self._services.values():
            service.start()

    def stop_all(self):

        for service in self._services.values():
            service.stop()

    def status(self):

        return {
            name: service.status()
            for name, service in self._services.items()
        }
