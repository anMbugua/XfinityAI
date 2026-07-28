class ServiceRegistry:
    """
    Stores and manages application services.
    """

    def __init__(self):
        self._services = {}

    def register(self, name, service):
        """
        Add a service to the registry.
        """
        self._services[name] = service

    def get(self, name):
        """
        Retrieve a service.
        """
        return self._services.get(name)

    def remove(self, name):
        """
        Remove a service.
        """
        if name in self._services:
            del self._services[name]

    def list_services(self):
        """
        Return available services.
        """
        return list(self._services.keys())

