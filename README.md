# Blackhole Anomaly Detector

A complete anomaly detection project that identifies unusual financial transactions, stores the results in PostgreSQL, and visualizes them through a Streamlit dashboard.

---

## Overview
This repository demonstrates an end-to-end workflow for data anomaly detection:
- ingest and store transaction data in PostgreSQL
- run anomaly detection using Isolation Forest
- persist anomalies in a dedicated database table
- explore results through a Streamlit dashboard
- optionally expose anomaly data via a FastAPI endpoint

---

## Features
- Detects transaction anomalies using Isolation Forest
- Persists anomaly results into PostgreSQL
- Streamlit dashboard with filtering and charts
- Dockerized deployment for app and database
- FastAPI endpoint for anomaly queries

---

## Tech Stack
- Python 3.10
- Pandas
- Scikit-learn
- SQLAlchemy
- PostgreSQL
- Streamlit
- FastAPI
- Docker Compose

---

## Quick Start
### Recommended: Docker
From the project root, run:

```bash
docker compose up --build
```

Then open the dashboard:

```text
http://localhost:8501
```

Stop the services with:

```bash
docker compose down
```

### Local development
Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run dashboard.py
```

(Optional) Start the API:

```bash
uvicorn main:app --reload
```

---

## Project Structure
- `anomaly_detection.py` — runs anomaly detection and stores results
- `dashboard.py` — Streamlit app showing detected anomalies
- `main.py` — FastAPI endpoint returning anomaly records
- `db.py` — database connection configuration
- `sql/dump.sql` — database schema and sample data
- `docker-compose.yml` — app and PostgreSQL service setup
- `requirements.txt` — Python dependencies

---

## Database Schema
- `transactions`
  - `transaction_id`
  - `amount`
  - `timestamp`
  - `user_id`
- `anomalies`
  - `transaction_id`
  - `amount`
  - `timestamp`
  - `user_id`
  - `anomaly`

The `anomaly` column marks detected outliers.

---

## Endpoints
- Dashboard: `http://localhost:8501`
- FastAPI API (if enabled): `GET /anomalies`

---

## Troubleshooting
- If the database is already initialized or has stale data, remove the Docker volume and restart:

```bash
docker compose down
docker volume rm data-blackhole-detector_postgres_data
docker compose up --build
```

- If Streamlit fails to start, ensure port `8501` is not already in use.
- If the app cannot connect to PostgreSQL, confirm the credentials in `db.py` match `docker-compose.yml`.

---

## Future Improvements
- Add real-time transaction ingestion
- Add API authentication
- Add more dashboard visualizations
- Add unit tests and CI pipeline
- Add additional anomaly detection models
