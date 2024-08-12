# Temperature API

Esta é uma API que consulta a temperatura atual de cidades ao redor do mundo. A API utiliza o site [Time and Date](https://www.timeanddate.com) para obter informações sobre o clima.

## Tecnologias Utilizadas

- **FastAPI**: Framework web para criar a API.
- **Selenium**: Para automação de navegação e coleta de dados das páginas do Time and Date.
- **BeautifulSoup**: Para análise e extração de dados das páginas HTML.
- **requests**: Para fazer requisições HTTP.
- **webdriver_manager**: Para gerenciar o WebDriver do Chrome.

## Funcionalidades

- **/all/countries**: Retorna a lista de todos os países disponíveis para consulta.
- **/all/cities**: Retorna a lista de todas as cidades disponíveis para consulta.
- **/{country}/{city}**: Retorna a temperatura atual da cidade especificada no país especificado.

## Instalação

Clone este repositório e instale as dependências:

```bash
git clone https://github.com/seuusuario/timeAPI.git
cd timeAPI
pip install -r requirements.txt
```

## Uso

1. **Atualizar Cidades**:
   Para atualizar a lista de cidades disponíveis, execute o script `handler.py`. Isso fará com que o Selenium colete os dados das cidades do Time and Date.

   ```bash
   python handler.py
   ```

2. **Executar o Servidor FastAPI**:
   Para iniciar o servidor da API, execute o seguinte comando:

   ```bash
   uvicorn main:app --reload
   ```

   O servidor estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Arquitetura do Projeto

- **handler.py**: Contém funções para coleta e processamento de dados das cidades e temperaturas.
- **main.py**: Define os endpoints da API usando FastAPI.
- **utils.py**: Funções auxiliares para sanitização de texto e salvamento de dados.

## Dependências

Certifique-se de ter o `requirements.txt` atualizado com todas as bibliotecas necessárias. O arquivo `requirements.txt` pode ser gerado com:

```bash
pip freeze > requirements.txt
```

## Contribuição

Se você quiser contribuir para o projeto, sinta-se à vontade para enviar pull requests. Para problemas ou dúvidas, abra uma issue no GitHub.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
```

Você pode ajustar qualquer detalhe conforme necessário. Se precisar de mais informações ou ajustes, é só me falar!