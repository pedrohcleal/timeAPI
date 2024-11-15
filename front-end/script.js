// Configuração da API
const API_BASE_URL = 'http://127.0.0.1:8000';

// Elementos do DOM
const countrySelect = document.getElementById('country');
const citySelect = document.getElementById('city');
const currentSelection = document.getElementById('current-selection');
const timeBttn = document.getElementById('timeBttn');
const currTemp = document.getElementById('timeTemp');
const updateParsBttn = document.getElementById('UpdatePairsBttn');
const paresRetorno = document.getElementById('paresRetorno');

// Armazena os dados completos
let pairsData = {};
let temp = '';

// Função para carregar os dados
async function loadPairsData() {
    try {
        const response = await fetch(`${API_BASE_URL}/get_pairs`);
        if (!response.ok) throw new Error('Erro ao carregar dados');

        pairsData = await response.json();

        // Preenche o select de países
        populateCountries();
    } catch (error) {
        console.error('Erro ao carregar dados:', error);
        showError('Não foi possível carregar os dados');
    }
}

async function get_temperature() {
    try {
        const response = await fetch(`${API_BASE_URL}/${countrySelect.value}/${citySelect.value}`);
        if (!response.ok) throw new Error('Erro ao carregar dados');

        temp = await response.json();
        console.log(temp.temperature)
        currTemp.textContent = temp.temperature
    } catch (error) {
        console.error('Erro ao carregar dados:', error);
        showError('Não foi possível carregar os dados');
    }

}

async function fetch_update_pairs() {
    paresRetorno.textContent = 'Atualizando pares Cidade/País aguarde'
    try {
        const response = await fetch(`${API_BASE_URL}/update_pairs_city_country`)
        if (!response.ok) throw new Error('Erro ao carregar dados');
        let final_pairs = await response.json();
        console.log(final_pairs)
        paresRetorno.textContent = `${final_pairs.message} - Falhas = ${final_pairs.falhas}`
    } catch (error) {
        console.error('Erro ao carregar dados:', error);
        showError('Não foi possível carregar os dados');
    }
}


// Função para preencher o select de países
function populateCountries() {
    timeBttn.disabled = true;

    countrySelect.innerHTML = '<option value="">Selecione um país</option>';

    // Obtém a lista de países e ordena
    const countries = Object.keys(pairsData).sort();

    // Adiciona cada país como uma opção
    countries.forEach(country => {
        const option = document.createElement('option');
        option.value = country;
        option.textContent = country;
        countrySelect.appendChild(option);
    });
}

// Função para preencher o select de cidades
function populateCities(country) {
    // Limpa e desabilita o select de cidades
    citySelect.innerHTML = '<option value="">Selecione uma cidade</option>';
    citySelect.disabled = true;

    if (!country) {
        citySelect.innerHTML = '<option value="">Primeiro selecione um país</option>';
        return;
    }

    // Obtém e ordena a lista de cidades do país selecionado
    const cities = pairsData[country].sort();

    // Adiciona cada cidade como uma opção
    cities.forEach(city => {
        const option = document.createElement('option');
        option.value = city;
        option.textContent = city;
        citySelect.appendChild(option);
    });

    // Habilita o select de cidades
    citySelect.disabled = false;
}

// Função para mostrar erro
function showError(message) {
    currentSelection.textContent = `Erro: ${message}`;
    currentSelection.style.color = 'red';
}

// Função para atualizar a exibição da seleção atual
function updateSelectionDisplay() {
    const country = countrySelect.value;
    const city = citySelect.value;

    if (country && city) {
        timeBttn.disabled = false;
        currentSelection.textContent = `${city}, ${country}`;
        currentSelection.style.color = '#333';
    } else {
        currentSelection.textContent = 'Seleção incompleta';
        currentSelection.style.color = '#666';
    }
}

// Event Listeners
countrySelect.addEventListener('change', (e) => {
    const selectedCountry = e.target.value;
    populateCities(selectedCountry);
    updateSelectionDisplay();
});

citySelect.addEventListener('change', updateSelectionDisplay);

timeBttn.addEventListener('click', get_temperature)

updateParsBttn.addEventListener('click', fetch_update_pairs)

document.addEventListener('DOMContentLoaded', loadPairsData);
