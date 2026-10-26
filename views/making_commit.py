import streamlit as st

def init():
    st.header("💾 Fazendo Commit")
    st.write("O commit grava as modificações em uma revisão local na sua máquina física.")
    st.markdown("**Abre o editor de texto para a mensagem:**")
    st.code("git commit", language="bash")
    st.markdown("**Faz o commit passando a mensagem direto:**")
    st.code('git commit -m "<msg>"', language="bash")
    st.markdown("**Faz o commit incluindo arquivos modificados não adicionados via git add:**")
    st.code('git commit -am "<msg>"', language="bash")
