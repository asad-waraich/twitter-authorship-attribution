cat > data/README.md << 'EOF'
# Data Directory

## Structure
- `sample_data/`: Small sample datasets for testing
- `raw/`: Original scraped data (not tracked in git)
- `processed/`: Cleaned and processed data

## Getting the Full Dataset
Due to size and privacy considerations, the full dataset is not included in this repository.

To recreate the dataset:
1. Run the data collection script: `python scripts/collect_data.py`
2. Or download from [link to your data if hosted]

## Sample Data
Sample data includes 100 tweets per author for testing purposes.
EOF