import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path(__file__).resolve().parent / "predictions.db"


def init_db():

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
                model_version TEXT,
                predicted_price REAL,
                response_time_ms REAL,
                status TEXT,
                error_message TEXT
            )
        """)

def log_prediction(model_version, predicted_price, response_time_ms,
                   status, error_message=None):

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO predictions
            (model_version, predicted_price, response_time_ms, status, error_message)
            VALUES (?, ?, ?, ?, ?)
        """, (model_version, predicted_price, response_time_ms,
              status, error_message))



def get_predictions():

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query("SELECT * FROM predictions", conn)
        

        return df