from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:admin@localhost:5432/blackhole_db"

engine = create_engine(DB_URL)

print("DB connection created successfully")