import streamlit as st
from views import (
    getting_started,
    preparing_commit,
    making_commit,
    navigating_branches,
    diffing_changes,
    discarding_changes,
    editing_history,
    git_archaeology,
    combining_branches,
    remote_repositories,
    tags,
    resolving_conflicts,
    useful_settings,
    structural_files
)

st.set_page_config(
    page_title="Cheat Git - Seu Guia Prático",
    page_icon="⚡",
    layout="centered"
)

st.title("Cheat Git - Seu guia de Git")

page_names_to_funcs = {
    "Iniciando": getting_started.init,
    "Preparando para o Commit": preparing_commit.init,
    "Fazendo Commit": making_commit.init,
    "Navegando pelas Branches": navigating_branches.init,
    "Diferenças entre Alterações": diffing_changes.init,
    "Descartando Alterações": discarding_changes.init,
    "Edição de Histórico": editing_history.init,
    "Arqueologia do Git": git_archaeology.init,
    "Combinando Branches": combining_branches.init,
    "Repositórios Remotos": remote_repositories.init,
    "Tags": tags.init,
    "Resolução de Conflitos": resolving_conflicts.init,
    "Configurações Úteis": useful_settings.init,
    "Arquivos Estruturais": structural_files.init,
}

demo_name = st.sidebar.selectbox("Escolha o tópico:", list(page_names_to_funcs.keys()))
page_names_to_funcs[demo_name]()

st.sidebar.info("Selecione um tópico acima.")
