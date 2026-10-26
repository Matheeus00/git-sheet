import streamlit as st

def init():
    st.header("📂 Arquivos Estruturais Importantes")
    st.markdown("📄 **Configuração Local:** Validade restrita ao repositório atual.")
    st.code(".git/config", language="text")
    st.markdown("🌍 **Configuração Global:** Válido para o perfil de usuário do sistema operacional.")
    st.code("~/.gitconfig", language="text")
    st.markdown("🙈 **Filtro de Exclusões (.gitignore):** Arquivos que nunca serão indexados ou enviados.")
    st.code(".gitignore", language="text")
