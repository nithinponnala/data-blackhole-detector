#  Blackhole Anomaly Detector

An end-to-end anomaly detection system for identifying unusual financial transactions using machine learning, FastAPI, and Streamlit.

---

##  Features
- Detect anomalies using Isolation Forest
- Store anomalies in PostgreSQL
- REST API with filtering support
- Interactive dashboard with Streamlit

---

##  Tech Stack
- Python, Pandas, Scikit-learn
- FastAPI
- PostgreSQL
- Streamlit

---

##  How to Run

### 1. Run anomaly detection
python anomaly_detection.py

### 2. Start API
uvicorn main:app --reload

### 3. Launch dashboard
streamlit run dashboard.py

---

##  What This Project Shows
- End-to-end ML pipeline
- Backend API design
- Data engineering + visualization
