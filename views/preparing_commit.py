import streamlit as st

def init():
    st.header("🧪 Preparando para o Commit")
    st.subheader("Verificar os arquivos")
    st.write("Verifica o estado atual dos seus arquivos (modificados, staged ou não rastreados).")
    st.code("git status", language="bash")
    
    st.subheader("Adicionar arquivos (Staging)")
    st.markdown("**Adiciona apenas os arquivos especificados:**")
    st.code("git add <files>", language="bash")
    st.markdown("**Adiciona todos os arquivos modificados e novos:**")
    st.code("git add .", language="bash")
    
    st.subheader("Excluir arquivos")
    st.code("git rm <files>            # Remove do disco e do Git\ngit rm --cached <files>   # Remove do Git, mas mantém físico", language="bash")
    
    st.subheader("Reverter alterações preparados (Reset)")
    st.code("git reset <files>         # Reverte arquivos selecionados\ngit reset                 # Reverte todos do staging area", language="bash")
