import re
import pandas as pd

class TweetPreprocessor:
    """Preprocess tweets for authorship attribution"""
    
    def __init__(self):
        pass
    
    def clean_tweet(self, text):
        """Clean individual tweet"""
        # Remove URLs
        text = re.sub(r'http\S+|www.\S+', '', text)
        # Remove mentions and hashtags
        text = re.sub(r'@\w+|#\w+', '', text)
        # Remove special characters
        text = re.sub(r'[^A-Za-z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    def preprocess_dataframe(self, df):
        """Preprocess entire dataframe"""
        df = df.copy()
        df['Tweet'] = df['Tweet'].apply(self.clean_tweet)
        df = df[df['Tweet'].str.len() > 0]
        return df.reset_index(drop=True)
EOF