import pandas as pd
from db import engine


def load_data():
    query = "SELECT * FROM transactions"
    df = pd.read_sql(query, engine)
    print(f"Loaded {len(df)} rows from database")
    return df


def check_nulls(df):
    return df.isnull().sum()


def check_duplicates(df):
    return df.duplicated().sum()


def check_row_count(df):
    return len(df)


def check_negative_values(df):
    if "amount" in df.columns:
        return (df["amount"] < 0).sum()
    return 0


def run_validation():
    df = load_data()

    results = {}

    results["nulls"] = check_nulls(df).to_dict()
    results["duplicates"] = int(check_duplicates(df))
    results["row_count"] = int(check_row_count(df))
    results["negative_values"] = int(check_negative_values(df))

    print("\n===== DATA VALIDATION REPORT =====")
    for key, value in results.items():
        print(f"{key}: {value}")

    return results


if __name__ == "__main__":
    run_validation()