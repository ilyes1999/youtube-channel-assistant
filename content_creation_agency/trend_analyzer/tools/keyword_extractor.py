from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import Counter
import os
from dotenv import load_dotenv

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

load_dotenv()

class keyword_extractor(BaseTool):
    """
    Extracts relevant keywords and phrases from text content.
    """
    text: str = Field(
        ..., 
        description="The text content to extract keywords from"
    )
    max_keywords: int = Field(
        default=10,
        description="Maximum number of keywords to extract"
    )

    def run(self):
        """
        Extracts keywords from the provided text content.
        """
        # TODO: Implement actual keyword extraction logic
        # This is a placeholder implementation
        return f"Extracted {self.max_keywords} keywords from the text"

if __name__ == "__main__":
    tool = keyword_extractor(
        text="This is a sample text about artificial intelligence and machine learning.",
        max_keywords=5
    )
    print(tool.run()) 