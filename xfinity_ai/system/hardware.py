import os
import platform
import shutil
from pathlib import Path
import psutil

memory = psutil.virtual_memory()



class HardwareProfile:
    """Collect basic information about the current machine."""

    def __init__(self):
        self.info = {}

    def collect(self):
        disk = shutil.disk_usage(Path.home())

        self.info = {
            "hostname": platform.node(),
            "os": platform.system(),
            "release": platform.release(),
            "python": platform.python_version(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "cpu_cores": os.cpu_count(),
            "disk_total_gb": round(disk.total / (1024**3), 1),
            "disk_free_gb": round(disk.free / (1024**3), 1),
            "ram_total_gb": round(memory.total / (1024**3),1),
            "ram_available_gb": round(memory.available / (1024**3), 1),
            "ram_percent": memory.percent

      }

        return self.info

    def get(self, key, default=None):
        return self.info.get(key, default)

