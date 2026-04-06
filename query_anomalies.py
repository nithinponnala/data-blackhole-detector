import pandas as pd
from db import engine


def get_anomalies():
    query = "SELECT * FROM anomalies"
    df = pd.read_sql(query, engine)
    return df


def main():
    df = get_anomalies()
    print("===== ANOMALIES FROM DB =====")
    print(df)


if __name__ == "__main__":
    main()