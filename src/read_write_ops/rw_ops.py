import pandas as pd


def save_df_in_csv(df: pd.DataFrame, file_path: str):
    df.to_csv(file_path, index=False)
    return file_path


def read_df_from_csv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)
