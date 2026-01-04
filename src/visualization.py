import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def plot_sentiment_distribution(df):
    sns.countplot(x='sentiment', data=df)
    plt.title('Sentiment Distribution')
    plt.show()

def plot_sentiment_pie(df):
    df['sentiment'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title('Sentiment Share')
    plt.ylabel('')
    plt.show()

def wordcloud_positive(df):
    text = ' '.join(df[df['sentiment']=='positive']['clean_text'])
    wc = WordCloud(background_color='white').generate(text)
    plt.imshow(wc)
    plt.axis('off')
    plt.title('Positive Sentiment Word Cloud')
    plt.show()
