import streamlit as st

def init():
    st.header("🗑️ Descartando Alterações")
    st.code("git restore <file>        # Descartar mudanças unstaged (Novo)\ngit checkout <file>       # Descartar mudanças unstaged (Antigo)\ngit reset --hard          # Descartar ABSOLUTAMENTE tudo", language="bash")
    
    st.subheader("📦 Salvar para depois (Stash)")
    st.write("Guarda um rascunho temporário do progresso para limpar o diretório de trabalho.")
    st.code("git stash", language="bash")

    st.subheader("🧹 Excluir arquivos nunca rastreados")
    st.code("git clean", language="bash")
    st.error("🚨 Extremamente perigoso! Não pode ser desfeito.")
