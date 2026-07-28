from pathlib import Path

from xfinity_ai.tools.base_tool import BaseTool


class FileTool(BaseTool):

    name = "filesystem"


    def execute(self, path):

        location = Path(path).expanduser()

        if not location.exists():
            return "Path does not exist"


        return [
            item.name
            for item in location.iterdir()
        ]
