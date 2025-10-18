import numpy as np
from sentence_transformers import SentenceTransformer

class FeatureExtractor:
    """Extract features from tweets"""
    
    def __init__(self, method='embeddings'):
        self.method = method
        self.vocab = None
        
        if method == 'embeddings':
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def create_vocabulary(self, tweets):
        """Create vocabulary from training tweets"""
        vocab = set()
        for tweet in tweets:
            vocab.update(tweet.split())
        self.vocab = sorted(list(vocab))
        return self.vocab
    
    def create_bow_features(self, tweets):
        """Create Bag of Words features"""
        if self.vocab is None:
            self.create_vocabulary(tweets)
        
        features = np.ones((len(tweets), len(self.vocab)))
        for i, tweet in enumerate(tweets):
            words = tweet.split()
            for j, word in enumerate(self.vocab):
                features[i, j] += words.count(word)
        return features
    
    def create_embeddings(self, tweets):
        """Create sentence embeddings"""
        return self.model.encode(tweets)
