<div align="center">

# Git Sheet

### Guia interativo de Git feito com Python e Streamlit

Aprenda e consulte conceitos e comandos do Git em uma aplicação simples, organizada por tópicos e criada como parte dos meus estudos de Python.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)

</div>

## Sobre o projeto

O **Git Sheet** é um guia de consulta interativo para quem está aprendendo ou quer revisar os principais recursos do Git. A aplicação apresenta os conteúdos em tópicos acessíveis por um menu lateral.

O projeto também é um exercício prático de desenvolvimento com Python e Streamlit, reunindo estudos de programação e controle de versão em uma aplicação web.

## Conteúdo

A aplicação organiza os tópicos em áreas como:

- primeiros passos e preparação de commits
- criação de commits e navegação entre branches
- comparação e descarte de alterações
- edição e exploração do histórico
- combinação de branches e resolução de conflitos
- repositórios remotos e tags
- configurações e arquivos estruturais do Git

## Tecnologias

- **Python** — linguagem utilizada no projeto
- **Streamlit** — criação da interface web interativa
- **Git** — controle de versão

## Como executar localmente

### Requisitos

- Python instalado
- `pip`

### 1. Clone o repositório

```bash
git clone https://github.com/Matheeus00/git-sheet.git
cd git-sheet
```

### 2. (Opcional) Crie e ative um ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie a aplicação

```bash
streamlit run app.py
```

O Streamlit exibirá no terminal o endereço local da aplicação, normalmente `http://localhost:8501`.

## Estrutura do repositório

```text
git-sheet/
├── app.py              # ponto de entrada e navegação da aplicação
├── views/              # conteúdo separado por tópico
├── assets/             # recursos visuais
├── .streamlit/         # configurações do Streamlit
├── requirements.txt    # dependências Python
└── README.md           # documentação do projeto
```

## Objetivos de aprendizado

- praticar Python em um projeto aplicado
- conhecer o Streamlit e criar uma interface interativa
- estudar e organizar conceitos importantes do Git
- desenvolver e documentar um projeto pessoal

## Próximos passos

O projeto pode crescer junto com os estudos, com novos tópicos, exemplos práticos e melhorias na experiência de navegação.

## Autor

**Matheus Lucas**

- GitHub: [@Matheeus00](https://github.com/Matheeus00)

---

Feito como parte dos meus estudos contínuos de Python e Git.
