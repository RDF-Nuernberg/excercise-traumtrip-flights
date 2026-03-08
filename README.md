# Aufgabe Traumtrip Flugverwaltung

Das Reisebüro Traumtripp ist auf den Verkauf von Flugreisen spezialisiert. Dafür wurde ein EDV-System entwickelt, welches aber noch nicht ganz fertig ist. Das System besteht aus einem Frontend und einem Backend.

- Das Backend basiert auf dem `Flask` Framework und soll eine `JSON`-API Schnittstelle bieten und kümmert sich um den sicheren Zugriff auf die Datenbank.
- Das Frontend ist eine Weboberfläche mit HTML, CSS und JS, welche über die `JSON`- API mit dem Backend kommuniziert.


Das Frontend soll zwei Seiten bereitstellen. Die erste Seite `index.html` soll alle Flüge in einer Tabelle anzeigen. Die zweite Seite `add.html` stellt ein Formular zur Verfügung um neue Flüge anzulegen. Die Menüpunkte im Frontend sollen dynamisch aus der Datenbank geladen werden, das heißt wenn sich die zu Grunde liegende Tabelle in der Datenbank ändert, sollen sich das Menü automatisch mit ändern. 
Wurden Daten erfolgreich geladen, soll diese in der Seite entsprechend angezeigt und der Hinweis: "Loading" entfernt werden. Kann keine Verbindung zum Backend aufgebaut werden oder liefert dies einen Fehler zurück, soll dies entsprechend auf der Seite angezeigt werden.

Das Backend kümmert sich den Zugriff auf die Datenbank, dazu sind alle nötigen SQL Statements in der Datei `sql_statements.py` bereits vorgegeben. Außerdem soll das Backend alle nötigen Endpunkt, welche für die korrekte Funktionsweise des Frontends nötig sind implementieren.
Dabei sollen alle Eingaben sollen mit Hilfe von RegEx auf Plausibilität überprüft werden. Wird ein Fehler erkannt soll dieser mit einer aussagekräftigen Nachricht an das Frontend zurück gegeben werden.

## Logisches Modell der Datenbank

![Logisches Modell](./db-modell.png)