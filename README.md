# Git Sheet

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Git-Flow-000000?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
</p>

Uma ferramenta prática e visual para estudar e revisar o uso do Git, desenvolvida em Python com Streamlit.

Este projeto foi criado como um exercício pessoal de aprendizado e como uma forma de consolidar conceitos do Git em uma interface simples e interativa. Ele serve como um guia de referência rápida para comandos, fluxos e boas práticas de versionamento.

## Visão geral

O Git Sheet é um mini guia de consulta para comandos e situações comuns no Git, como:

- inicialização e configuração do repositório
- criação e uso de commits
- navegação entre branches
- comparação de alterações
- descarte de mudanças
- resolução de conflitos
- uso de tags e repositórios remotos
- revisão de histórico e arquivos estruturais

A aplicação foi pensada para facilitar o aprendizado por meio de uma interface intuitiva, com navegação por tópicos em sidebar e conteúdo organizado por área.

## Tecnologias utilizadas

- Python
- Streamlit
- Git

## Funcionalidades

- interface interativa em navegador
- menu lateral com tópicos organizados
- conteúdo de apoio sobre comandos Git
- estrutura didática para estudo contínuo
- foco em uso prático e revisão rápida de conceitos

## Como executar

### Pré-requisitos

- Python 3.10 ou superior
- pip

### Instalação

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No macOS/Linux:

```bash
source .venv/bin/activate
```

Em seguida, instale as dependências:

```bash
pip install -r requirements.txt
```

### Execução

```bash
streamlit run app.py
```

A aplicação será aberta localmente em:

```text
http://localhost:8501
```

## Estrutura do projeto

```text
git-sheet/
├── app.py                  # aplicação principal em Streamlit
├── requirements.txt        # dependências do projeto
├── .streamlit/             # configurações da aplicação Streamlit
├── assets/                 # arquivos visuais e estáticos
├── views/                  # módulos de conteúdo por tópico do Git
├── README.md               # documentação do projeto
└── .gitignore              # arquivos ignorados pelo Git
```

## Objetivo do projeto

Este repositório representa uma etapa de estudo e prática em Python, com foco em:

- aprendizado de desenvolvimento em Python
- uso de frameworks e bibliotecas de interface
- criação de aplicações simples e úteis
- aprofundamento em Git e versionamento de código

## Status

Projeto em desenvolvimento pessoal, com foco em prática, aprendizado contínuo e documentação de estudos.

## Autor

Matheus Lucas

## Licença

Este projeto é destinado a fins educacionais e de estudo pessoal.
