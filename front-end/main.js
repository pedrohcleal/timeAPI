// Configuração da API
const API_BASE_URL = 'http://127.0.0.1:8000/';

// Elementos do DOM
const countrySelect = document.getElementById('country');
const citySelect = document.getElementById('city');
const currentSelection = document.getElementById('current-selection');

// Cache para os dados das cidades
const citiesCache = {};

// Função para carregar os países
async function loadCountries() {
    try {
        const response = await fetch(`${API_BASE_URL}/all/countries`);
        if (!response.ok) throw new Error('Erro ao carregar países');
        
        const countries = await response.json();
        
        // Ordena os países por nome
        countries.sort((a, b) => a.name.localeCompare(b.name));
        
        // Adiciona as opções ao select de países
        countries.forEach(country => {
            const option = document.createElement('option');
            option.value = country.id;
            option.textContent = country.name;
            countrySelect.appendChild(option);
        });
    } catch (error) {
        console.error('Erro ao carregar países:', error);
        showError('Não foi possível carregar a lista de países');
    }
}

// Função para carregar as cidades de um país
async function loadCities(countryId) {
    if (citiesCache[countryId]) {
        populateCitySelect(citiesCache[countryId]);
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/cities/${countryId}`);
        if (!response.ok) throw new Error('Erro ao carregar cidades');
        
        const cities = await response.json();
        
        // Armazena no cache
        citiesCache[countryId] = cities;
        
        populateCitySelect(cities);
    } catch (error) {
        console.error('Erro ao carregar cidades:', error);
        showError('Não foi possível carregar a lista de cidades');
    }
}

// Função para preencher o select de cidades
function populateCitySelect(cities) {
    citySelect.innerHTML = '<option value="">Selecione uma cidade</option>';
    
    // Ordena as cidades por nome
    cities.sort((a, b) => a.name.localeCompare(b.name));
    
    cities.forEach(city => {
        const option = document.createElement('option');
        option.value = city.id;
        option.textContent = city.name;
        citySelect.appendChild(option);
    });
    
    citySelect.disabled = false;
}

// Função para mostrar erro
function showError(message) {
    currentSelection.textContent = `Erro: ${message}`;
    currentSelection.style.color = 'red';
}

// Função para atualizar a exibição da seleção atual
function updateSelectionDisplay() {
    const countryName = countrySelect.options[countrySelect.selectedIndex].text;
    const cityName = citySelect.options[citySelect.selectedIndex].text;
    
    if (countrySelect.value && citySelect.value) {
        currentSelection.textContent = `${cityName}, ${countryName}`;
    } else {
        currentSelection.textContent = 'Seleção incompleta';
    }
}

// Event Listeners
countrySelect.addEventListener('change', (e) => {
    const countryId = e.target.value;
    citySelect.innerHTML = '<option value="">Carregando cidades...</option>';
    citySelect.disabled = true;
    
    if (countryId) {
        loadCities(countryId);
    } else {
        citySelect.innerHTML = '<option value="">Primeiro selecione um país</option>';
        citySelect.disabled = true;
    }
    
    updateSelectionDisplay();
});

citySelect.addEventListener('change', updateSelectionDisplay);

// Inicialização
document.addEventListener('DOMContentLoaded', loadCountries);