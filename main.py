from fastapi import FastAPI, Query
import pandas as pd
from db import engine

app = FastAPI()

@app.get("/anomalies")
def get_anomalies(
    user_id: int = None,
    min_amount: float = None
):
    query = "SELECT * FROM anomalies"
    df = pd.read_sql(query, engine)

    if user_id:
        df = df[df['user_id'] == user_id]

    if min_amount:
        df = df[df['amount'] >= min_amount]

    return df.to_dict(orient="records")