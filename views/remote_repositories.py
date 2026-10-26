import streamlit as st

def init():
    st.header("🌐 Repositórios Remotos")
    st.code("git remote add <name> <url> # Vincula repositório remoto\ngit remote -v               # Lista remotos ativos\ngit remote remove <nome>    # Desvincula remoto", language="bash")
    
    st.subheader("Enviar e Baixar Alterações")
    st.code("git push origin <branch>   # Envia commits locais\ngit fetch                   # Busca atualizações sem mesclar\ngit pull                    # Busca atualizações e faz merge\ngit pull --rebase           # Busca atualizações com histórico linear", language="bash")
