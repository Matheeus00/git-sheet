import streamlit as st

def init():
    st.header("🏷️ Tags")
    st.code("git tag <name>              # Cria tag simples\ngit tag -a <name> -m <msg>  # Cria tag anotada (Recomendado)\ngit tag                     # Lista tags\ngit push origin <tag>       # Envia tag específica\ngit push origin --tags      # Envia todas as tags locais", language="bash")
