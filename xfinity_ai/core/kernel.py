from rich.console import Console

from xfinity_ai.core.service_registry import ServiceRegistry
from xfinity_ai.core.lifecycle import Lifecycle
from xfinity_ai.core.service_manager import ServiceManager


class Kernel:

    def __init__(self):

        self.console = Console()

        self.registry = ServiceRegistry()

        self.lifecycle = Lifecycle()

        self.services = ServiceManager(
            self.registry
        )


    def boot(self):

        self.console.rule(
            "[bold cyan]Xfinity AI"
        )


        self.services.initialize()


        self.lifecycle.start()


        logger = self.registry.get(
            "logger"
        )


        logger.info(
            "Services initialized"
        )

        logger.info(
            "Kernel started"
        )


        self.console.print()

        self.console.print(
            "[bold green]System Ready."
        )
        logger.info(
            str(
                self.services.list_services()
            )
        )

        logger.info(
            str(
                self.registry.get("tools").list_tools()
            )
        )
