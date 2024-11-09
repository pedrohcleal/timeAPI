// Configuração da URL base da API
const API_BASE_URL = 'http://127.0.0.1:8000';

// Função para buscar dados do backend
async function fetchDataFromBackend() {
    try {
        const response = await fetch(`${API_BASE_URL}/all/countries`);
        if (!response.ok) {
            throw new Error('Erro ao buscar dados');
        }
        const data = await response.json();
        displayData(data);
    } catch (error) {
        console.error('Erro:', error);
        displayError(error.message);
    }
}

// Função para exibir os dados na página
function displayData(data) {
    const container = document.getElementById('data-container');
    container.innerHTML = ''; // Limpa o conteúdo anterior
    console.log(data.countries)
    
    if (Array.isArray(data.countries)) {
        const ul = document.createElement('ul');
        data.countries.forEach(item => {
            const li = document.createElement('li');
            li.textContent = JSON.stringify(item);
            ul.appendChild(li);
        });
        container.appendChild(ul);
    } else {
        container.textContent = JSON.stringify(data, null, 2);
    }
}

// Função para exibir mensagens de erro
function displayError(message) {
    const container = document.getElementById('data-container');
    container.innerHTML = `<p style="color: red;">Erro: ${message}</p>`;
}

// Adiciona evento de clique ao botão
document.getElementById('fetchData').addEventListener('click', fetchDataFromBackend);

// Inicialização quando a página carrega
document.addEventListener('DOMContentLoaded', () => {
    console.log('Aplicação inicializada');
});