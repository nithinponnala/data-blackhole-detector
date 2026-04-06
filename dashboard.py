import streamlit as st
import pandas as pd
from db import engine

st.title(" Blackhole Anomaly Detector")

# Load data
query = "SELECT * FROM anomalies"
df = pd.read_sql(query, engine)

# Sidebar filters
st.sidebar.header("Filters")

user_id = st.sidebar.number_input("User ID", min_value=1, step=1)
min_amount = st.sidebar.number_input("Min Amount", min_value=0.0)

# Apply filters
if user_id:
    df = df[df['user_id'] == user_id]

if min_amount:
    df = df[df['amount'] >= min_amount]

# Show data
st.write("### Detected Anomalies")
st.dataframe(df)

# Chart
st.write("### Amount Distribution")
st.bar_chart(df['amount'])