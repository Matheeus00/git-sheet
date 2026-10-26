import streamlit as st

def init():
    st.header("🔍 Diferenças entre Alterações")
    st.code("git diff HEAD              # Diferença do último commit\ngit diff                   # Apenas arquivos unstaged\ngit diff --staged          # Apenas arquivos staged", language="bash")
    st.info("**Terminologia:**\n- **unstaged:** Sem git add\n- **staged:** Com git add")

    st.subheader("Diferenças entre commits")
    st.code("git show <commit>          # Diferença do commit e seu anterior\ngit show <commit> <commit> # Diferença entre dois commits distintos\ngit diff <commit> <file>   # Diferença de um arquivo até o commit", language="bash")
