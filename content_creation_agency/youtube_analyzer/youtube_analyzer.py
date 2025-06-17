from agency_swarm import Agent

class YouTubeAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            name="YouTube Analyzer",
            description="Analyzes YouTube channel performance, competitor content, and audience engagement to identify content opportunities.",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.5,
            max_prompt_tokens=25000
        ) 