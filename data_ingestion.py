import pandas as pd
from db import engine
from datetime import datetime
import random


def generate_data(n=100):
    data = []

    for i in range(n):
        amount = random.uniform(10, 500)

        # Add some anomalies
        if i % 20 == 0:
            amount = random.uniform(1000, 5000)

        data.append({
            "amount": amount,
            "timestamp": datetime.now(),
            "user_id": random.randint(1, 10)
        })

    df = pd.DataFrame(data)
    return df


def load_to_db(df):
    df.to_sql("transactions", con=engine, if_exists="append", index=False)


def run_ingestion():
    df = generate_data(200)
    print(f"Generated {len(df)} rows")

    load_to_db(df)
    print("Data inserted into database")


if __name__ == "__main__":
    run_ingestion()