import pandas as pd
from sklearn.ensemble import IsolationForest
from db import engine
from sqlalchemy import create_engine



def load_data():
    query = "SELECT * FROM transactions"
    df = pd.read_sql(query, engine)
    return df


def detect_anomalies(df):
    model = IsolationForest(
        contamination=0.05,  # 5% anomalies expected
        random_state=42
    )

    df['anomaly'] = model.fit_predict(df[['amount']])

    return df

def save_anomalies(df):
    anomalies = df[df['anomaly'] == -1]
    anomalies.to_sql("anomalies", con=engine, if_exists="replace", index=False)
    print(f"Saved {len(anomalies)} anomalies to DB")

def run_anomaly_detection():
    df = load_data()

    print(f"Loaded {len(df)} rows")

    df = detect_anomalies(df)

    anomalies = df[df['anomaly'] == -1]

    print("\n===== ANOMALIES DETECTED =====")
    print(anomalies)

    save_anomalies(df)

if __name__ == "__main__":
    run_anomaly_detection()
