from .registry import CapabilityRegistry
from .capability import Capability


def create_registry():

    registry = CapabilityRegistry()

    registry.register(
        Capability(
            name="filesystem",
            category="tool",
            description="Read and write files",
            permissions=["read", "write"],
            tags=["storage"]
        )
    )

    registry.register(
        Capability(
            name="terminal",
            category="tool",
            description="Execute shell commands",
            permissions=["execute"],
            tags=["shell"]
        )
    )

    registry.register(
        Capability(
            name="qwen-local",
            category="model",
            description="Local Qwen 2.5 model",
            tags=["llm", "offline"]
        )
    )

    return registry
