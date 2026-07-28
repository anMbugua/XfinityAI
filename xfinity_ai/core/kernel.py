from rich.console import Console
from xfinity_ai.config.config_manager import ConfigManager
from xfinity_ai.core.service_registry import ServiceRegistry
from xfinity_ai.core.lifecycle import Lifecycle
from xfinity_ai.utils.logger import Logger
from xfinity_ai.events.event_bus import EventBus

class Kernel:

    def __init__(self):

        self.console = Console()

        self.registry = ServiceRegistry()

        self.lifecycle = Lifecycle()


    def boot(self):

        self.console.rule("[bold cyan]Xfinity AI")

        logger = Logger()
        config = ConfigManager()
        config.load()
        event_bus = EventBus()

        self.registry.register(
            "events",
            event_bus
        )
        self.registry.register(
	    "config",
	    config
	)

        self.registry.register(
            "logger",
            logger
        )

        self.lifecycle.start()

        logger.info(
            "Logger initialized"
        )

        logger.info(
            "Kernel started"
        )

        self.console.print()

        self.console.print(
            "[bold green]System Ready."
        )
