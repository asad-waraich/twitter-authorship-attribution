import pandas as pd
import os

# Create sample data
sample_data = {
    'Tweet': [
        'Breaking news from India today',
        'This dish is absolutely terrible',
        'Love my fans so much',
        'Latest updates from CNN',
        'Rolling up with my crew'
    ] * 20,  # 100 samples
    'User': ['timesofindia', 'GordonRamsay', 'sonamakapoor', 'cnni', 'wizkhalifa'] * 20
}

df = pd.DataFrame(sample_data)
os.makedirs('data/sample_data', exist_ok=True)
df.to_csv('data/sample_data/sample_tweets.csv', index=False)
print("Sample data created successfully!")
