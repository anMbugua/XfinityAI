from rich.console import Console

from xfinity_ai.core.service_registry import ServiceRegistry
from xfinity_ai.core.lifecycle import Lifecycle
from xfinity_ai.services.manager import ServiceManager

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
        hardware = self.registry.get("hardware")

        logger.info(f"OS: {hardware.get('os')}")
        logger.info(f"CPU cores: {hardware.get('cpu_cores')}")
        logger.info(f"Free disk: {hardware.get('disk_free_gb')} GB")
        logger.info(f"Available ram: {hardware.get('ram_available_gb')}")
        logger.info(f"Ram_total: {hardware.get('ram_total_gb')}")


