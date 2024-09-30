from pydantic.v1 import BaseModel, Field
from langchain_core.tools import StructuredTool
from src.utils.logger import logger
from src.utils.browserless_util import Browserless_Tool
from src.utils.duckduckgo_util import DuckDuckGoSearch_Tool, DuckDuckGoCommunitySearch_Tool, DuckDuckGoNewsSearch_Tool
from src.utils.exa_util import ExaSearch_Tool, ExaFindSimilar_Tool, ExaGetContents_Tool


def load_crewai_tools(name):
    import importlib
    try:
        module = importlib.import_module("crewai_tools")
        tool_class = getattr(module, name)
        tool = tool_class()
        return tool
    except Exception as e:
        logger.error(f"Failed to load crewai tools {name}: {str(e)}")


class UrlSchema(BaseModel):
    url: str = Field(description="url to scrape")

class QuerySchema(BaseModel):
    query: str = Field(description="query string to search")

class IDsSchema(BaseModel):
    ids: str = Field(description="ids to search")


def get_args_schema(name):
    if name == "UrlSchema":
        return UrlSchema
    elif name == "QuerySchema":
        return QuerySchema
    elif name == "IDsSchema":
        return IDsSchema
    return None


def get_tool_func(toolname):
    if toolname == "BrowserlessTool":
        return Browserless_Tool
    elif toolname == "DuckDuckGoSearchTool":
        return DuckDuckGoSearch_Tool
    elif toolname == "DuckDuckGoCommunitySearchTool":
        return DuckDuckGoCommunitySearch_Tool
    elif toolname == "DuckDuckGoNewsSearchTool":
        return DuckDuckGoNewsSearch_Tool
    elif toolname == "ExaSearchTool":
        return ExaSearch_Tool
    elif toolname == "ExaFindSimilarTool":
        return ExaFindSimilar_Tool
    elif toolname == "ExaGetContentsTool":
        return ExaGetContents_Tool


def create_tool(tool_config):
    """
    Create a tool based on the tool configuration.

    Args:
        tool_config (dict): The configuration for the tool.

    Returns:
        Tool: The created tool instance.
    """
    if tool_config["type"] == "crewai":
        return load_crewai_tools(tool_config["name"])

    args_schema = get_args_schema(tool_config["args_schema"])
    if not args_schema:
        logger.error(f"Can't find args_schema: {tool_config["args_schema"]}")
        return
    func = get_tool_func(tool_config["name"])
    if not func:
        logger.error(f"Can't find func: {tool_config["name"]}")
        return
    
    tool = StructuredTool.from_function(
        func=func,
        name=tool_config["name"],
        description=tool_config["description"],
        args_schema=args_schema,
        return_direct=True,
        coroutine=None
    )
    
    return tool