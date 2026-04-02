import pandas as pd

def get_top_locations(df):
    return df['location'].value_counts().head(10)

def get_top_skills(df):
    skills_series = df['skills'].str.split(',')
    all_skills = skills_series.explode()
    return all_skills.value_counts().head(10)