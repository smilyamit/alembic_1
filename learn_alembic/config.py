import os

POSTGRES_USER = os.getenv("POSTGRES_USER", "tester")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "tester")
POSTGRES_DB = os.getenv("POSTGRES_DB", "alembic_demo_dev")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
