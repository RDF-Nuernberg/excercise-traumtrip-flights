const API_BASE_URL = 'http://127.0.0.1:5000/api';

function showError(message) {
    const errorEl = document.getElementById('error')
    errorEl.textContent = message
    errorEl.style.display = 'block'
}

function fetchFlights() {
    console.log("Starting fetching flights.")

    const loadingEl = document.getElementById('loading')
    const tableEl = document.getElementById('flights-table')
    const tableBodyEl = document.getElementById('flights-body')

    fetch(`${API_BASE_URL}/flights`)
    .then(response => {
        // Fehlerbehandlung:
        if (!response.ok) {
            // Wenn die Antwort nicht ok ist, versuche die Fehlermeldung aus der Antwort zu extrahieren
            return response.json().then(errorData => {
                throw new Error(`HTTP error! status: ${response.status}, message: ${errorData.message}`)
            })
        }
        // Wenn die Antwort ok ist, parse sie als JSON
        return response.json()
    })
    .then(json => {
        loadingEl.style.display = 'none'
        tableEl.style.display = 'table';

        console.log(json)

        tableBodyEl.innerHTML = ''
        json.forEach(element => {
            const row = document.createElement('tr');
            // console.log(element)
            row.innerHTML = `
            <td>${element.IDflug}</td>
            <td>${element.Startflughafen}</td>
            <td>${element.Zielflughafen}</td>
            <td>${element.Abflugdatum}</td>
            <td>${element.Preis}</td>
            <td>${element.Dauer_in_Stunden}</td>
            <td>${element.fluggesellschaft}</td>
            <td>${element.Flugzeugtyp}</td>
            `
            tableBodyEl.appendChild(row);
        });
    }).catch(error => {
        loadingEl.style.display = 'none'
        showError(`Konnte Flüge nicht laden: ${error.message}`)
        console.log("error")
    })
}

// fetchFlights()
document.addEventListener('DOMContentLoaded', fetchFlights)