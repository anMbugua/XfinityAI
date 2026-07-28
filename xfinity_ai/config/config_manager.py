import yaml
from pathlib import Path


class ConfigManager:

    def __init__(self, path="config/config.yaml"):
        self.path = Path(path)
        self.data = {}

    def load(self):
        with open(self.path, "r") as file:
            self.data = yaml.safe_load(file)

    def get(self, key, default=None):
        parts = key.split(".")

        value = self.data

        for part in parts:
            if part in value:
                value = value[part]
            else:
                return default

        return value
