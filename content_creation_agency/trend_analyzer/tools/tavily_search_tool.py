from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
import json
from tavily import TavilyClient

load_dotenv()

class tavily_search_tool(BaseTool):
    """
    Performs web searches using the Tavily API to gather information about trends.
    """
    query: str = Field(
        ..., 
        description="The search query to find relevant information"
    )
    max_results: int = Field(
        default=5,
        description="Maximum number of search results to return"
    )

    def run(self):
        """
        Performs a web search using the Tavily API and returns relevant results.
        """
        # TODO: Implement actual Tavily search logic
        # This is a placeholder implementation
        return f"Search results for query: {self.query}"

if __name__ == "__main__":
    tool = tavily_search_tool(
        query="Latest AI trends 2024",
        max_results=3
    )
    print(tool.run()) 