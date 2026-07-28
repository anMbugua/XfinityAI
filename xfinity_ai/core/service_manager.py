from xfinity_ai.utils.logger import Logger
from xfinity_ai.config.config_manager import ConfigManager
from xfinity_ai.events.event_bus import EventBus


class ServiceManager:

    def __init__(self, registry):

        self.registry = registry


    def initialize(self):

        config = ConfigManager()
        config.load()

        logger = Logger()

        events = EventBus()


        self.registry.register(
            "config",
            config
        )

        self.registry.register(
            "logger",
            logger
        )

        self.registry.register(
            "events",
            events
        )


    def list_services(self):

        return self.registry.list_services()
