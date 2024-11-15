# Webscraping Fundamentos IBOVX

<p align="center">
<img src="https://img.shields.io/badge/status-em%20construção-orange" alt="Status do projeto">
</p>

## Sobre o projeto

Este projeto realiza a extração de dados relacionados a:

- **Indicadores financeiros** de Fundos de Investimentos Imobiliários (FIIs) disponíveis no site **Fundamentos**.
- **Histórico de negociações na B3**, extraído do site **IBOVX**.

### Objetivo

O objetivo é consolidar essas informações e apresentá-las de forma organizada e acessível para análises.

## Funcionalidades

- Web scraping para capturar indicadores financeiros de FIIs.
- Obtenção de dados históricos da bolsa de valores.
- Agregação e exibição dos dados coletados.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

- **Python** 3.8 ou superior.
- Bibliotecas necessárias (instale com `pip install -r requirements.txt`).

## Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/adaircommodo/webscraping_fundamentus_ibovex.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script principal:
   ```bash
   python ws_fundamentus_ibovx.py
   ```

## Estrutura do repositório

```
webscraping_fundamentus_ibovex/
├── servicos/                # Código modular para serviços de scraping
├── ws_fundamentus_ibovx.py  # Script principal
├── README.md                # Documentação
└── novo_arquivo.csv         # Exemplo de saída gerada
```

## Próximos passos

- [ ] Implementar novos indicadores financeiros.
- [ ] Melhorar a exibição dos dados agregados.
- [ ] Automatizar o processo de coleta e atualização dos dados.

---

<p align="center">
Feito com ❤️ por [Adair Commodo](https://github.com/adaircommodo)
</p>
