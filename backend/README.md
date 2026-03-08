# Flights Backend

Hier befindet sich das Backend für die Platform von Traumtripp Flugreisen.

## Setup

Das Projekt nutzt den python manager `uv` für die Verwaltung von Abhängigkeiten.
Es werden die Pakete  `flask` und `flask-cors` wie in der `project.toml` angegeben benötigt.

Um die Virtuelle Umgebung zu initialisieren müssen sie im Backend Ordner den Befehl `uv sync` ausführen.

```sh
cd backend
uv sync
```

Die `main.py` enthält schon den minimalen Boilerplate Code um das Flask-Backend zu starten. 
Führen Sie dazu die `main.py` aus. Anschließend startet der Server unter dem Port `5000` wie auf der Console angegeben.

```sh
uv run main.py
```

## Aufgabe 

Implementieren Sie die API-Endpunkte wie in der Aufgabenstellung angegeben.

In der Datei `sql_statements.py` befinden Sie alle SQL Statements welche für den Zugriff auf die Datenbank notwendig ist. Diese wurde bereits in der `main.py` importiert.



### Lösungshinweise

**Wichtig:** Diese sind in der Klausur nicht enthalten!

2. GET /api/airports - List all airports
   Endpoint: "/api/airports"
   Use: SQL_SELECT_AIRPORTS
   Returns: JSON array of airport objects

3. GET /api/aircraft-types - List all aircraft types
   Endpoint: "/api/aircraft-types"
   Use: SQL_SELECT_AIRCRAFT_TYPES
   Returns: JSON array of aircraft type objects

4. GET /api/airlines - List all airlines
   Endpoint: "/api/airlines"
   Use: SQL_SELECT_AIRLINES
   Returns: JSON array of airline objects

5. GET /api/flights - List all flights
   Endpoint: "/api/flights"
   Use: SQL_SELECT_ALL_FLIGHTS
   Returns: JSON array of flight objects

6. POST /api/flights - Create a new flight
   Endpoint: "/api/flights"
   Use: SQL_INSERT_FLIGHT and SQL_SELECT_FLIGHT_BY_ID
   Required fields in request body:
     - Startflughafen (int)
     - Zielflughafen (int)
     - Abflugdatum (string)
     - Preis (float)
     - Dauer_in_Stunden (float)
     - Flugzeugtyp (int)
   Optional field:
     - fluggesellschaft (int or null)
   Returns: JSON of the newly created flight with status code 201
