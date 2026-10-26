import streamlit as st

def init():
    st.header("🏁 Iniciando")
    st.subheader("Iniciar um repositório (LOCAL)")
    st.write("Cria os arquivos internos ocultos que identificam e dão início ao repositório Git na pasta atual.")
    st.code("git init", language="bash")
    
    st.subheader("Clonar um repositório já existente (REMOTO)")
    st.write("Baixa os arquivos que constam em um local remoto para a sua máquina local.")
    st.code("git clone <url>", language="bash")
