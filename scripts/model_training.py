# src/train_model.py
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


def train_and_save_models(df: pd.DataFrame, target: str = "Appliances") -> None:
    """
    Train regression models and save them to disk.

    Args:
        df (pd.DataFrame): Dataset with features and target.
        target (str): Name of the target column.
    """
    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
        "XGBoost": XGBRegressor(n_estimators=100, random_state=42, verbosity=0)
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        with open(f"../models/{name}.pkl", "wb") as f:
            pickle.dump(model, f)
