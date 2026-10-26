import streamlit as st

def init():
    st.header("🧰 Arqueologia do Git")
    st.subheader("Histórico de Logs")
    st.code("git log <branch>           # Histórico completo\ngit log --graph <branch>   # Gráfico estrutural com nós\ngit log --oneline <branch> # Resumido (um commit por linha)", language="bash")
    
    st.subheader("Rastreamento por Arquivo/Texto")
    st.code("git log <file>             # Commits que alteraram o arquivo\ngit log --follow <file>    # Histórico incluindo renomeações\ngit blame <file>           # Autor de cada linha individual\ngit log -G<text>           # Commits que mexeram nesse texto", language="bash")
