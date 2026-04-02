import pandas as pd

def predict_skill_demand(df):

    skills = df['skills'].str.split(',')

    skills = skills.explode()

    trend = skills.value_counts()

    return trend.head(10)