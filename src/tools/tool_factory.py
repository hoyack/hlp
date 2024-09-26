from __future__ import annotations
from abc import ABC, abstractmethod
from crewai_tools import BaseTool, SerperDevTool
from src.utils.browserless_util import BrowserlessTool
from src.utils.exa_util import ExaGetContentsTool, ExaSearchTool, ExaFindSimilarTool
from src.utils.duckduckgo_util import DuckDuckGoSearchTool, DuckDuckGoCommunitySearchTool, DuckDuckGoNewsSearchTool

class ToolFactory(ABC):

    @abstractmethod
    def create_tool(self, name):
        pass

    def get_tool(self, name) -> BaseTool:
        tool = self.create_tool(name)
        return tool
    

class MainToolFactory(ToolFactory):
    
    def create_tool(self, name) -> BaseTool:
        tool = None
        if name == "BrowserlessTool":
            tool = BrowserlessTool()
        elif name == "SerperDevTool":
            tool = SerperDevTool()
        elif name == "DuckDuckGoSearchTool":
            tool = DuckDuckGoSearchTool()
        elif name == "DuckDuckGoCommunitySearchTool":
            tool = DuckDuckGoCommunitySearchTool()
        elif name == "DuckDuckGoNewsSearchTool":
            tool = DuckDuckGoNewsSearchTool()
        elif name == "ExaSearchTool":
            tool = ExaSearchTool()
        elif name == "ExaFindSimilarTool":
            tool = ExaFindSimilarTool()
        elif name == "ExaGetContentsTool":
            tool = ExaGetContentsTool()
        return tool


