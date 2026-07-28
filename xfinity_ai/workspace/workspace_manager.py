from pathlib import Path


class WorkspaceManager:

    def __init__(self, root):
        self.root = Path(root).expanduser()


    def exists(self):
        return self.root.exists()


    def list_files(self):

        if not self.exists():
            return []

        return [
            item.name
            for item in self.root.iterdir()
        ]


    def get_root(self):
        return str(self.root)
