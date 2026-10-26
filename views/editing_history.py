import streamlit as st

def init():
    st.header("⏳ Edição de Histórico")
    st.code("git rebase -i HEAD~<n>      # Edita commits interativamente\ngit commit --amend          # Modifica o último commit feito\ngit revert <commit>         # Cria novo commit desfazendo o anterior\ngit reset --hard <commit>   # Retorna apagando o histórico adiante", language="bash")
