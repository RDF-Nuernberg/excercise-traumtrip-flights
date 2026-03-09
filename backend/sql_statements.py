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
# Bookings (Buchungen)
SQL_SELECT_ALL_BOOKINGS = """
    SELECT
        IDbuchungen,
        IDKunde,
        Buchungsdatum,
        MitarbeiterDerDenFlugVerkauftHat
    FROM buchungen
    ORDER BY IDbuchungen DESC
"""

SQL_INSERT_BOOKING = """
    INSERT INTO buchungen (
        IDKunde,
        Buchungsdatum,
        MitarbeiterDerDenFlugVerkauftHat
    )
    VALUES (?, ?, ?)
"""

SQL_SELECT_BOOKING_BY_ID = """
    SELECT
        IDbuchungen,
        IDKunde,
        Buchungsdatum,
        MitarbeiterDerDenFlugVerkauftHat
    FROM buchungen
    WHERE IDbuchungen = ?
"""

# Customers (Kunden)
SQL_SELECT_ALL_CUSTOMERS = """
    SELECT
        IDKunden,
        IDAnrede,
        Name,
        Vorname,
        Straße,
        Hausnummer,
        PLZ,
        Telefon,
        Geburtsdatum,
        Email,
        Titel
    FROM kunden
    ORDER BY Name, Vorname
"""

SQL_INSERT_CUSTOMER = """
    INSERT INTO kunden (
        IDAnrede,
        Name,
        Vorname,
        Straße,
        Hausnummer,
        PLZ,
        Telefon,
        Geburtsdatum,
        Email,
        Titel
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

SQL_SELECT_CUSTOMER_BY_ID = """
    SELECT
        IDKunden,
        IDAnrede,
        Name,
        Vorname,
        Straße,
        Hausnummer,
        PLZ,
        Telefon,
        Geburtsdatum,
        Email,
        Titel
    FROM kunden
    WHERE IDKunden = ?
"""

# Employees (Mitarbeiter)
SQL_SELECT_ALL_EMPLOYEES = """
    SELECT
        IDMitarbeiter,
        Vorname,
        Nachname,
        Anrede,
        Straße,
        Hausnummer,
        PLZ,
        Filiale
    FROM mitarbeiter
    ORDER BY Nachname, Vorname
"""

SQL_INSERT_EMPLOYEE = """
    INSERT INTO mitarbeiter (
        Vorname,
        Nachname,
        Anrede,
        Straße,
        Hausnummer,
        PLZ,
        Filiale
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""

SQL_SELECT_EMPLOYEE_BY_ID = """
    SELECT
        IDMitarbeiter,
        Vorname,
        Nachname,
        Anrede,
        Straße,
        Hausnummer,
        PLZ,
        Filiale
    FROM mitarbeiter
    WHERE IDMitarbeiter = ?
"""

# Airports (Flughafen)
SQL_SELECT_ALL_AIRPORTS_FULL = """
    SELECT
        ID_Flughafen,
        Bezeichnung_Flughafen,
        Land
    FROM flughafen
    ORDER BY Bezeichnung_Flughafen
"""

SQL_INSERT_AIRPORT = """
    INSERT INTO flughafen (
        Bezeichnung_Flughafen,
        Land
    )
    VALUES (?, ?)
"""

SQL_SELECT_AIRPORT_BY_ID = """
    SELECT
        ID_Flughafen,
        Bezeichnung_Flughafen,
        Land
    FROM flughafen
    WHERE ID_Flughafen = ?
"""

# Airlines (Fluggesellschaft)
SQL_SELECT_ALL_AIRLINES_FULL = """
    SELECT
        IDFluggesellschaft,
        Name_Fluggesellschaft,
        Telefon,
        Straße,
        Hausnummer,
        PLZ
    FROM fluggesellschaft
    ORDER BY Name_Fluggesellschaft
"""

SQL_INSERT_AIRLINE = """
    INSERT INTO fluggesellschaft (
        Name_Fluggesellschaft,
        Telefon,
        Straße,
        Hausnummer,
        PLZ
    )
    VALUES (?, ?, ?, ?, ?)
"""

SQL_SELECT_AIRLINE_BY_ID = """
    SELECT
        IDFluggesellschaft,
        Name_Fluggesellschaft,
        Telefon,
        Straße,
        Hausnummer,
        PLZ
    FROM fluggesellschaft
    WHERE IDFluggesellschaft = ?
"""

# Supporting Data (for dropdowns)
SQL_SELECT_SALUTATIONS = """
    SELECT IDAnrede, Anrede
    FROM anrede
    ORDER BY IDAnrede
"""

SQL_SELECT_BRANCHES = """
    SELECT IDFiliale
    FROM filiale
    ORDER BY IDFiliale
"""

SQL_SELECT_COUNTRIES = """
    SELECT ID_Land, Bezeichnung_Land
    FROM laender
    ORDER BY Bezeichnung_Land
"""