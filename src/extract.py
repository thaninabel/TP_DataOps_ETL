import pandas as pd


def extract(csv_path: str) -> pd.DataFrame:

    """
    Lit le CSV sans transformation.
    """

    df = pd.read_csv(csv_path, dtype=str)

    print(f"[Extract] {len(df)} lignes lues")

    return df