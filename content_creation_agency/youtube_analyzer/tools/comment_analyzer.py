from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter

# Download required NLTK data
nltk.download('vader_lexicon')

load_dotenv()

class comment_analyzer(BaseTool):
    """
    Analyzes sentiment and topics in video comments using YouTube Data API and NLTK.
    Provides insights about audience feedback and engagement.
    """
    video_id: str = Field(
        ..., description="YouTube video ID to analyze"
    )
    max_comments: int = Field(
        default=100, description="Maximum number of comments to analyze"
    )

    def run(self):
        """
        Fetch and analyze video comments using YouTube Data API and NLTK.
        """
        try:
            # Initialize YouTube API client and NLTK sentiment analyzer
            youtube = build('youtube', 'v3', developerKey=os.getenv('YOUTUBE_API_KEY'))
            sia = SentimentIntensityAnalyzer()
            
            comments = []
            next_page_token = None
            
            while len(comments) < self.max_comments:
                # Get comments
                comment_response = youtube.commentThreads().list(
                    part='snippet',
                    videoId=self.video_id,
                    maxResults=min(100, self.max_comments - len(comments)),
                    pageToken=next_page_token,
                    textFormat='plainText'
                ).execute()
                
                for item in comment_response['items']:
                    comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    
                    # Analyze sentiment
                    sentiment_scores = sia.polarity_scores(comment_text)
                    
                    # Determine overall sentiment
                    if sentiment_scores['compound'] >= 0.05:
                        sentiment = 'positive'
                    elif sentiment_scores['compound'] <= -0.05:
                        sentiment = 'negative'
                    else:
                        sentiment = 'neutral'
                    
                    comment_data = {
                        "text": comment_text,
                        "author": item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                        "likes": item['snippet']['topLevelComment']['snippet']['likeCount'],
                        "published_at": item['snippet']['topLevelComment']['snippet']['publishedAt'],
                        "sentiment": sentiment,
                        "sentiment_scores": sentiment_scores
                    }
                    
                    comments.append(comment_data)
                
                next_page_token = comment_response.get('nextPageToken')
                if not next_page_token:
                    break
            
            # Analyze sentiment distribution
            sentiment_distribution = Counter(c['sentiment'] for c in comments)
            
            # Calculate engagement metrics
            total_likes = sum(c['likes'] for c in comments)
            
            # Extract common phrases (simple implementation)
            words = [word.lower() for c in comments for word in c['text'].split()]
            common_words = Counter(words).most_common(20)
            
            analysis_results = {
                "total_comments_analyzed": len(comments),
                "sentiment_distribution": dict(sentiment_distribution),
                "average_likes_per_comment": total_likes / len(comments) if comments else 0,
                "common_words": dict(common_words),
                "comments": comments
            }
            
            return json.dumps(analysis_results, ensure_ascii=False, indent=2)

        except HttpError as e:
            return json.dumps({
                "error": f"YouTube API error: {str(e)}",
                "total_comments_analyzed": 0,
                "sentiment_distribution": {},
                "comments": []
            }, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({
                "error": str(e),
                "total_comments_analyzed": 0,
                "sentiment_distribution": {},
                "comments": []
            }, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    # Test the tool with a video ID
    test_video_id = "YOUR_TEST_VIDEO_ID"  # Replace with an actual video ID
    tool = comment_analyzer(video_id=test_video_id, max_comments=10)
    print(tool.run()) 