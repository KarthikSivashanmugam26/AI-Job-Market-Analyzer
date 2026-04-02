import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):

    df = df.drop_duplicates()

    df.columns = df.columns.str.lower()

    if 'salary' in df.columns:
        df['salary'] = df['salary'].fillna(df['salary'].median())

    df = df.fillna("Unknown")

    return df