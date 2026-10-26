import streamlit as st

def init():
    st.header("⚙️ Configurações Úteis")
    st.code('git config --global user.name "<Nome>" \ngit config --global user.email "<email>" \ngit config --global core.editor "vim" \ngit config --list', language="bash")
    
    st.subheader("Atalhos personalizados (Aliases)")
    st.code('git config --global alias.st status \ngit config --global alias.co checkout \ngit config --global alias.cm "commit -m" \ngit config --global alias.acp "!git add . && git commit -m \'Atualiza\' && git push"', language="bash")
