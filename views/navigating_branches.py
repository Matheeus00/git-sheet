import streamlit as st

def init():
    st.header("🌿 Navegando através das Branches")
    st.subheader("Trocando de branches")
    st.code("git switch <branch>        # Troca de branch (Moderno)\ngit checkout <branch>      # Somente troca branch (Antigo)", language="bash")

    st.subheader("Criando novas branches")
    st.code("git switch -c <branch>       # Cria e troca (Novo)\ngit checkout -b <branch>     # Cria e troca (Antigo)", language="bash")

    st.subheader("Listando branches")
    st.code("git branch                         # Ordem alfabética\ngit branch --sort=-committerdate   # Por commit mais novo", language="bash")

    st.subheader("Excluindo branches")
    st.code("git branch -d <branch>      # Apenas se tiver feito merge (Seguro)\ngit branch -D <branch>      # Força exclusão (CUIDADO!)", language="bash")
