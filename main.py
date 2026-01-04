from src.data_loading import load_data
from src.preprocessing import preprocess_data
from src.sentiment_analysis import analyze_sentiment
from src.visualization import (
    plot_sentiment_distribution,
    plot_sentiment_pie,
    wordcloud_positive
)

# Load data
df = load_data('data/sentiment.csv')

# Clean data
df = preprocess_data(df)

# Sentiment analysis
df = analyze_sentiment(df)

# Visualizations
plot_sentiment_distribution(df)
plot_sentiment_pie(df)
wordcloud_positive(df)
