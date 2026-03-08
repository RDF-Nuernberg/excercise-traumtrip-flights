from pathlib import Path
import sqlite3

from flask import Flask, jsonify, request
from flask_cors import CORS

import sql_statements

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "traumtrip.db"

app = Flask(__name__)
CORS(app)


def get_connection() -> sqlite3.Connection:
    """
    Creates and returns a database connection.
    Connection uses Row factory for dictionary-like access to columns.
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


# TODO: Implement the missing routes:



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


