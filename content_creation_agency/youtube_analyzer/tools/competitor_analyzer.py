from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()

class competitor_analyzer(BaseTool):
    """
    Analyzes competitor YouTube channels and their content strategies.
    """
    competitor_channels: list = Field(
        ..., 
        description="List of competitor channel IDs to analyze"
    )
    analysis_type: str = Field(
        default="content",
        description="Type of analysis to perform (content, engagement, or growth)"
    )

    def run(self):
        """
        Analyzes competitor channels based on the specified analysis type.
        Returns channel information including channel ID.
        """
        try:
            # Initialize YouTube API client
            youtube = build('youtube', 'v3', developerKey=os.getenv('YOUTUBE_API_KEY'))
            
            results = []
            for channel_id in self.competitor_channels:
                try:
                    # Get channel details
                    channel_response = youtube.channels().list(
                        part='snippet,statistics',
                        id=channel_id
                    ).execute()

                    if not channel_response.get('items'):
                        results.append({
                            "channel_id": channel_id,
                            "error": "Channel not found"
                        })
                        continue

                    channel_info = channel_response['items'][0]
                    channel_data = {
                        "channel_id": channel_id,
                        "title": channel_info['snippet']['title'],
                        "description": channel_info['snippet']['description'],
                        "subscriber_count": channel_info['statistics'].get('subscriberCount', 'N/A'),
                        "video_count": channel_info['statistics'].get('videoCount', 'N/A'),
                        "view_count": channel_info['statistics'].get('viewCount', 'N/A'),
                        "analysis_type": self.analysis_type
                    }
                    results.append(channel_data)
                except HttpError as e:
                    results.append({
                        "channel_id": channel_id,
                        "error": f"Error fetching channel data: {str(e)}"
                    })

            return json.dumps(results, ensure_ascii=False, indent=2)

        except Exception as e:
            return json.dumps({
                "error": f"Failed to analyze channels: {str(e)}",
                "channels_analyzed": []
            }, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    # Use a real channel ID for testing
    tool = competitor_analyzer(
        competitor_channels=["UCdraIuwfdd-McqzBKZeGrEw"],  # Real channel ID from instructions
        analysis_type="content"
    )
    print(tool.run()) 