# Analisador de Logs em Python

## Sobre o projeto

Este projeto foi desenvolvido em Python com o objetivo de analisar registros de login (logs) e identificar possíveis atividades suspeitas.

O programa realiza a leitura de arquivos CSV, contabiliza tentativas de login e identifica usuários com três ou mais falhas.

## Funcionalidades

- Leitura de arquivos CSV.
- Contagem de eventos registrados.
- Identificação de falhas de login.
- Contagem de falhas por usuário.
- Geração de alertas para três ou mais falhas.
- Criação de relatórios em formato TXT.

## Tecnologias utilizadas

- Python
- Biblioteca CSV
- Biblioteca Counter
- Biblioteca Path

## Como executar

1. Tenha o Python instalado.
2. Baixe ou clone este repositório.
3. Execute o arquivo:

```bash
python analisar.py
```

## Estrutura do projeto

```text
CyberLab/
├── Dados/
│   └── logs.csv
├── analisar.py
└── README.md
```

## Objetivo de aprendizagem

Este projeto faz parte dos meus estudos em Python e Segurança da Informação, com foco em análise de logs e identificação de comportamentos suspeitos.

**Observação:** os registros utilizados devem ser fictícios ou devidamente autorizados e anonimizados.
