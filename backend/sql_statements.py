# SQL Query Constants
# Students: Use these SQL statements in your route implementations

SQL_SELECT_AIRPORTS = """
    SELECT ID_Flughafen, Bezeichnung_Flughafen
    FROM flughafen
    ORDER BY Bezeichnung_Flughafen
"""

SQL_SELECT_AIRCRAFT_TYPES = """
    SELECT IDFlugzeugtyp, Typenbezeichnung
    FROM flugzeugtyp
    ORDER BY Typenbezeichnung
"""

SQL_SELECT_AIRLINES = """
    SELECT IDFluggesellschaft, Name_Fluggesellschaft
    FROM fluggesellschaft
    ORDER BY Name_Fluggesellschaft
"""

SQL_SELECT_ALL_FLIGHTS = """
    SELECT
        IDflug,
        Startflughafen,
        Zielflughafen,
        Abflugdatum,
        Preis,
        Dauer_in_Stunden,
        fluggesellschaft,
        Flugzeugtyp
    FROM flug
    ORDER BY IDflug
"""

SQL_INSERT_FLIGHT = """
    INSERT INTO flug (
        Startflughafen,
        Zielflughafen,
        Abflugdatum,
        Preis,
        Dauer_in_Stunden,
        fluggesellschaft,
        Flugzeugtyp
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""

SQL_SELECT_FLIGHT_BY_ID = """
    SELECT
        IDflug,
        Startflughafen,
        Zielflughafen,
        Abflugdatum,
        Preis,
        Dauer_in_Stunden,
        fluggesellschaft,
        Flugzeugtyp
    FROM flug
    WHERE IDflug = ?
"""
