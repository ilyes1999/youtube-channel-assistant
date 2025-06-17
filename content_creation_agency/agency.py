from agency_swarm import Agency
from content_creation_agency.content_manager.content_manager import ContentManager
from content_creation_agency.trend_analyzer.trend_analyzer import TrendAnalyzer
from content_creation_agency.youtube_analyzer.youtube_analyzer import YouTubeAnalyzer
from dotenv import load_dotenv

load_dotenv()

# Initialize agents
content_manager = ContentManager()
trend_analyzer = TrendAnalyzer()
youtube_analyzer = YouTubeAnalyzer()

# Create the agency with communication flows
agency = Agency(
    [
        content_manager,  # Content Manager will be the entry point
        [content_manager, trend_analyzer],  # Content Manager can talk to Trend Analyzer
        [content_manager, youtube_analyzer],  # Content Manager can talk to YouTube Analyzer
    ],
    shared_instructions="agency_manifesto.md",
    temperature=0.7,
    max_prompt_tokens=25000,
)

"""def process_single_message(message):
   
    # Use the content manager (entry point agent) to process the message
    response = content_manager.execute(message)
    return response"""

if __name__ == "__main__":
    agency.demo_gradio() 