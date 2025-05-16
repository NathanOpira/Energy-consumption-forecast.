# src/features.py
import pandas as pd

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate time-based and lag features from the dataset.

    Args:
        df (pd.DataFrame): DataFrame with datetime index.

    Returns:
        pd.DataFrame: DataFrame with new features.
    """
    df = df.copy()

    # Time-based features
    df["hour"] = df.index.hour
    df["day"] = df.index.day
    df["month"] = df.index.month
    df["weekday"] = df.index.weekday
    df["weekend"] = df["weekday"].isin([5, 6]).astype(int)

    # Lag features (example: 1-hour lag)
    df["lag_1"] = df["Appliances"].shift(1)
    df.dropna(inplace=True)

    return df
