from agency_swarm import Agent

class ContentManager(Agent):
    def __init__(self):
        super().__init__(
            name="Content Manager",
            description="Primary orchestrator that coordinates analysis requests, generates content ideas, and manages script creation based on insights from other agents.",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.7,
            max_prompt_tokens=25000
        ) 