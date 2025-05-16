# src/data_loader.py
import pandas as pd

def load_energy_data(file_path: str) -> pd.DataFrame:
    """
    Load the energy dataset from a CSV file and parse the 'date' column as datetime.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned dataframe with datetime index.
    """
    df = pd.read_csv(file_path, parse_dates=["date"])
    df.set_index("date", inplace=True)
    df.sort_index(inplace=True)
    return df
