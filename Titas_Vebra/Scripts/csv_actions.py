import pandas as pd

def remove_empty_rows_and_columns(df: pd.DataFrame) -> pd.DataFrame:
    # Work on a copy so you don't mutate original by accident
    df_clean = df.copy()

    # 1. Turn pure-whitespace cells into NaN (but keep other values)
    df_clean = df_clean.replace(r'^\s*$', pd.NA, regex=True)

    # 2. Show how many rows/cols are fully empty
    empty_row_mask = df_clean.isna().all(axis=1)
    empty_col_mask = df_clean.isna().all(axis=0)

    print(f"Completely empty rows found: {empty_row_mask.sum()}")
    print(f"Completely empty columns found: {empty_col_mask.sum()}")

    # Optional: preview them before dropping
    if empty_row_mask.sum() > 0:
        print("\nSample of rows that will be removed:")
        print(df_clean[empty_row_mask].head())

    if empty_col_mask.sum() > 0:
        print("\nColumns that will be removed:")
        print(list(df_clean.columns[empty_col_mask]))

    # 3. Drop only fully-empty rows/columns
    df_clean = df_clean.loc[~empty_row_mask, ~empty_col_mask]

    return df_clean