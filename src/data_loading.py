import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Rename columns properly
    df.columns = ['id', 'topic', 'sentiment', 'text']

    print(df.head())
    print(df.info())
    return df
