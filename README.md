# Twitter Authorship Attribution using Machine Learning

## 🎯 Overview
Machine Learning system for identifying tweet authors with 91% accuracy using advanced NLP techniques and ensemble methods.

## 📊 Performance

| Model | Bag of Words | Embeddings |
|-------|-------------|------------|
| KNN | 67.8% | 76.3% |
| Neural Network | 71.2% | 85.4% |
| **Gradient Boosting** | 83.6% | **91.0%** ⭐ |
| Random Forest | 65.3% | 77.2% |
| Bagging | 68.1% | 79.5% |

## 🚀 Quick Start
```bash
# Clone and setup
git clone https://github.com/yourusername/twitter-authorship-attribution.git
cd twitter-authorship-attribution
pip install -r requirements.txt

# Train all models
python scripts/train_all_models.py

# Make predictions
python scripts/predict.py --text "Your tweet text here"
```

## 📁 Dataset
- 5 Twitter accounts (1000 tweets each)
- Authors: @timesofindia, @GordonRamsay, @sonamakapoor, @cnni, @wizkhalifa
- Collected using snscrape (2022)

**Note**: Twitter API changes post-2023 may affect data collection scripts.

## 🛠️ Technical Implementation

### Feature Extraction
1. **Bag of Words**: Vocabulary-based with Laplace smoothing
2. **Sentence Embeddings**: 384-dimensional vectors (all-MiniLM-L6-v2)

### Models
- K-Nearest Neighbors (optimized k=1)
- Neural Networks (500x300 architecture)
- Gradient Boosting (100 estimators)
- Random Forest (1000 trees)
- Bagging with Logistic Regression

### Evaluation
- 5-fold cross-validation
- 80/20 train-test split
- Stratified sampling

## 📈 Visualizations
![Model Comparison](results/figures/model_comparison.png)
![Confusion Matrix](results/figures/confusion_matrix.png)

## 🔬 Key Findings
- Embeddings outperform BoW by 10-15% across all models
- Gradient Boosting captures non-linear patterns most effectively
- Performance degrades with 150+ authors (research indicates ~60% accuracy)

## 📝 Applications
- Plagiarism detection
- Digital forensics
- Security & intelligence
- Copyright verification
- Bot detection

## 🚧 Future Work
- BERT-based transformers
- Real-time API deployment
- Cross-platform analysis
- Stylometric features
- Active learning pipeline

## 📄 License
MIT

## 🤝 Contributors
- Asad Ullah Waraich
