# Blackhole Anomaly Detector

An end-to-end anomaly detection project for identifying unusual financial transactions. It includes:
- transaction ingestion and anomaly detection
- PostgreSQL storage
- interactive Streamlit dashboard
- optional FastAPI endpoint for anomaly data

---

## Features
- Detects anomalies using Isolation Forest
- Stores detected anomalies in PostgreSQL
- Streamlit dashboard for interactive exploration
- Dockerized deployment for app + database

---

## Tech Stack
- Python
- Pandas
- Scikit-learn
- SQLAlchemy
- PostgreSQL
- Streamlit
- Docker / Docker Compose

---

## Docker Usage
Use Docker Compose to launch the app and PostgreSQL together.

```bash
docker compose up --build
```

Then open the dashboard at:

```text
http://localhost:8501
```

Stop the stack with:

```bash
docker compose down
```

---

## Local Development
If you want to run components locally without Docker, use these commands from the project root.

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Initialize PostgreSQL and load `sql/dump.sql` using your local database tools.

3. Start the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

4. (Optional) Start the API:

```bash
uvicorn main:app --reload
```

---

## Project Structure
- `anomaly_detection.py` — anomaly detection pipeline
- `dashboard.py` — Streamlit dashboard
- `main.py` — FastAPI endpoint for anomalies
- `db.py` — database connection setup
- `sql/dump.sql` — sample database schema + seeded data
- `docker-compose.yml` — Docker service definitions
- `requirements.txt` — Python dependencies

---

## Notes
- The Docker setup uses `postgres:15` and mounts `sql/dump.sql` to initialize the database.
- The app currently uses `postgres` / `postgres` credentials for database access.
- If the dashboard fails to connect after startup, ensure the database service is healthy and the volume is fresh.
