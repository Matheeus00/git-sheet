import streamlit as st

def init():
    st.header("🤝 Resolução de Conflitos")
    st.subheader("Durante o Merge")
    st.code("git status                  # Identifica arquivos conflitados\ngit diff                    # Examina conflitos nas linhas\ngit add <file>              # Marca conflito como resolvido\ngit commit                  # Finaliza a mesclagem", language="bash")
    
    st.subheader("Durante o Rebase")
    st.code("git rebase --continue       # Continua rebase após corrigir e dar git add\ngit rebase --abort          # Cancela operação e retorna ao início", language="bash")
