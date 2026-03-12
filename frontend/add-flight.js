const API_BASE_URL = 'http://127.0.0.1:5000/api';

function loadAirports() {
    const startSelect = document.getElementById('startflughafen');
    const destSelect = document.getElementById('zielflughafen');

    fetch(`${API_BASE_URL}/airports`)
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Failed to load airports');
            }
            return response.json();
        })
        .then(function (airports) {
            startSelect.innerHTML = '<option value="">Select start airport...</option>';
            destSelect.innerHTML = '<option value="">Select destination airport...</option>';

            airports.forEach(function (airport) {
                const option1 = document.createElement('option');
                option1.value = airport.ID_Flughafen;
                option1.textContent = airport.Bezeichnung_Flughafen;
                startSelect.appendChild(option1);

                const option2 = document.createElement('option');
                option2.value = airport.ID_Flughafen;
                option2.textContent = airport.Bezeichnung_Flughafen;
                destSelect.appendChild(option2);
            });
        })
        .catch(function (error) {
            console.error('Error loading airports:', error);
            startSelect.innerHTML = '<option value="">Error loading airports</option>';
            destSelect.innerHTML = '<option value="">Error loading airports</option>';
        });
}

function loadAirlines() {
    const select = document.getElementById('fluggesellschaft');

    fetch(`${API_BASE_URL}/airlines`)
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Failed to load airlines');
            }
            return response.json();
        })
        .then(function (airlines) {
            select.innerHTML = '<option value="">Select airline...</option>';

            airlines.forEach(function (airline) {
                const option = document.createElement('option');
                option.value = airline.IDFluggesellschaft;
                option.textContent = airline.Name_Fluggesellschaft;
                select.appendChild(option);
            });
        })
        .catch(function (error) {
            console.error('Error loading airlines:', error);
            select.innerHTML = '<option value="">Error loading airlines</option>';
        });
}

function loadAircraftTypes() {
    const select = document.getElementById('flugzeugtyp');

    fetch(`${API_BASE_URL}/aircraft-types`)
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Failed to load aircraft types');
            }
            return response.json();
        })
        .then(function (types) {
            select.innerHTML = '<option value="">Select aircraft type...</option>';

            types.forEach(function (type) {
                const option = document.createElement('option');
                option.value = type.IDFlugzeugtyp;
                option.textContent = type.Typenbezeichnung;
                select.appendChild(option);
            });
        })
        .catch(function (error) {
            console.error('Error loading aircraft types:', error);
            select.innerHTML = '<option value="">Error loading aircraft types</option>';
        });
}

function handleFormSubmit(event) {
    event.preventDefault();

    const errorEl = document.getElementById('error');
    const successEl = document.getElementById('success');

    errorEl.style.display = 'none';
    successEl.style.display = 'none';

    const formData = new FormData(event.target);
    const data = {
        Startflughafen: parseInt(formData.get('Startflughafen')),
        Zielflughafen: parseInt(formData.get('Zielflughafen')),
        Abflugdatum: formData.get('Abflugdatum'),
        Preis: parseFloat(formData.get('Preis')),
        Dauer_in_Stunden: parseFloat(formData.get('Dauer_in_Stunden')),
        Flugzeugtyp: parseInt(formData.get('Flugzeugtyp')),
        fluggesellschaft: parseInt(formData.get('fluggesellschaft'))
    };

    fetch(`${API_BASE_URL}/flights`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
        .then(response => {
            // Fehlerbehandlung:
            if (!response.ok) {
                return response.json().then(errorData => {
                    throw new Error(`${errorData.error}`)
                })
            }
            // Falls kein Fehler
            return response.json()
        })
        .then(flight => {
            console.log('Flight added:', flight);
            successEl.textContent = `Flight added successfully! ID: ${flight.IDflug}`;
            successEl.style.display = 'block';
            event.target.reset();  // Reset form after successful submission
        })
        .catch(error => {
            errorEl.textContent = `Error: ${error.message}`;
            errorEl.style.display = 'block';
            console.error('Error adding flight:', error);
        });
}

// Initialize page
document.addEventListener('DOMContentLoaded', function () {
    loadAirports();
    loadAirlines();
    loadAircraftTypes();

    const form = document.getElementById('add-flight-form');
    form.addEventListener('submit', handleFormSubmit);
});
