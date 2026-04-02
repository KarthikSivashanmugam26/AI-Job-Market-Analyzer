from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def train_model(df):

    df_model = pd.get_dummies(df, columns=['location'])

    X = df_model.drop(columns=['salary','skills','job_title'])
    y = df_model['salary']

    X_train, X_test, y_train, y_test = train_test_split(
        X,y,test_size=0.2
    )

    model = RandomForestRegressor()

    model.fit(X_train,y_train)

    return model