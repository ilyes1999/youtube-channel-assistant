from agency_swarm import Agent

class TrendAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            name="Trend Analyzer",
            description="Analyzes current AI trends and identifies content opportunities through web scraping and keyword analysis.",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.5,
            max_prompt_tokens=25000
        ) 