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


@app.get("/api/airports")
def list_airports():
    with get_connection() as connection:
        rows = connection.execute(sql_statements.SQL_SELECT_AIRPORTS).fetchall()

    return jsonify([dict(row) for row in rows])


@app.get("/api/aircraft-types")
def list_aircraft_types():
    with get_connection() as connection:
        rows = connection.execute(sql_statements.SQL_SELECT_AIRCRAFT_TYPES).fetchall()

    return jsonify([dict(row) for row in rows])


@app.get("/api/airlines")
def list_airlines():
    with get_connection() as connection:
        rows = connection.execute(sql_statements.SQL_SELECT_AIRLINES).fetchall()

    return jsonify([dict(row) for row in rows])


@app.get("/api/flights")
def list_flights():
    with get_connection() as connection:
        rows = connection.execute(sql_statements.SQL_SELECT_ALL_FLIGHTS_WITH_NAMES).fetchall()

        print(type(rows[0]))
    return jsonify([dict(row) for row in rows])


@app.post("/api/flights")
def create_flight():
    payload = request.get_json(silent=True) or {}

    print(payload)

    required_fields = [
        "Startflughafen",
        "Zielflughafen",
        "Abflugdatum",
        "Preis",
        "Dauer_in_Stunden",
        "Flugzeugtyp",
        "fluggesellschaft",
    ]

    missing = []
    for field in required_fields:
        if field not in payload:
            missing.append(field)
    
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    try:
        # Hier kann auch eine Validierung mittels regex erfolgen, 
        # um sicherzustellen, dass die Daten korrekt formatiert sind.
        startflughafen = int(payload["Startflughafen"])
        zielflughafen = int(payload["Zielflughafen"])
        abflugdatum = str(payload["Abflugdatum"])
        preis = float(payload["Preis"])
        dauer = float(payload["Dauer_in_Stunden"])
        flugzeugtyp = int(payload["Flugzeugtyp"])
        fluggesellschaft = int(payload["fluggesellschaft"])

    except (TypeError, ValueError):
        # Als Verbesserung sollte hier auch eine genauere Fehlermeldung zurückgegeben werden, 
        # die angibt, welches Feld ungültig war.
        return jsonify({"error": "Invalid value in request body."}), 400

    with get_connection() as connection:
        cursor = connection.execute(
            sql_statements.SQL_INSERT_FLIGHT,
            (
                startflughafen,
                zielflughafen,
                abflugdatum,
                preis,
                dauer,
                fluggesellschaft,
                flugzeugtyp,
            ),
        )
        connection.commit()
        new_id = cursor.lastrowid

        row = connection.execute(
            sql_statements.SQL_SELECT_FLIGHT_BY_ID,
            (new_id,),
        ).fetchone()

    return jsonify(dict(row)), 201


if __name__ == "__main__":
    app.run(debug=True)


