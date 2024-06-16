# tools/hello_tool.py
from crewai_tools import BaseTool

class HelloTool(BaseTool):
    name: str = "HelloTool"
    description: str = "A simple tool that returns a greeting."

    def _run(self, name: str) -> str:
        return f"Hello, {name}! Do your best and you will get a $100 tip!"

    def _arun(self, name: str):
        raise NotImplementedError("HelloTool does not support async")

    def _cache_key(self, *args, **kwargs) -> str:
        return f"{self.name}:{args[0]}"
