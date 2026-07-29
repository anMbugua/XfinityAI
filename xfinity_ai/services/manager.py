from xfinity_ai.config.config_manager import ConfigManager
from xfinity_ai.events.event_bus import EventBus
from xfinity_ai.system.hardware import HardwareProfile
from xfinity_ai.tools.file_tool import FileTool
from xfinity_ai.tools.tool_registry import ToolRegistry
from xfinity_ai.utils.logger import Logger
from xfinity_ai.workspace.workspace_manager import WorkspaceManager


class ServiceManager:

    def __init__(self, registry):
        self.registry = registry

    def initialize(self):

        config = ConfigManager()
        config.load()

        logger = Logger()

        events = EventBus()

        workspace = WorkspaceManager(
            "~/Development"
        )

        hardware = HardwareProfile()
        hardware.collect()

        tools = ToolRegistry()
        tools.register(FileTool())

        self.registry.register("config", config)
        self.registry.register("logger", logger)
        self.registry.register("events", events)
        self.registry.register("workspace", workspace)
        self.registry.register("hardware", hardware)
        self.registry.register("tools", tools)

    def list_services(self):
        return self.registry.list_services()
