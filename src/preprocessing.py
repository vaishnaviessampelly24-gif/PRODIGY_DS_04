import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def preprocess_data(df):
    df.dropna(inplace=True)
    df['clean_text'] = df['text'].apply(clean_text)
    return df
