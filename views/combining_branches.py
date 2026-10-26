import streamlit as st

def init():
    st.header("🔀 Combinando Branches Divergentes")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Rebase")
        st.write('Transfere todas as alterações de uma branch para outra e remove a anterior')
        st.code("git switch banana\ngit rebase main", language="bash")

        st.write("**Antes:**")
        st.image("assets/rebase_before.png", caption="Estrutura de branches antes do rebase", use_container_width=True)
        
        st.write("**Depois:**")
        st.image("assets/rebase_after.png", caption="Histórico linear após o rebase", use_container_width=True)
    with col2:
        st.subheader("Merge")
        st.write('Transfere as alterações de uma branch para outra e mantém a anterior')
        st.code("git switch main\ngit merge banana", language="bash")

        st.write("**Antes:**")
        st.image("assets/merge_before.png", caption="Estrutura de branches antes do merge", use_container_width=True)
        
        st.write("**Depois:**")
        st.image("assets/merge_after.png", caption="Histórico linear após o merge", use_container_width=True)
        
    st.subheader("Merge Squash")
    st.write('Transfere as alterações de uma branch para outra e mantém a anterior. As alterações dessa branch são compiladas em um commit só')
    st.code("git switch main\ngit merge --squash banana\ngit commit", language="bash")

    st.write("**Antes:**")
    st.image("assets/squash_before.png", caption="Estrutura de branches antes do Squash Merge", width=344)
    
    st.write("**Depois:**")
    st.image("assets/squash_after.png", caption="Histórico linear após o Squash Merge", width=344)

    st.subheader("Cherry-Pick")
    st.write('Pega um commit de uma branch e atualiza')
    st.code("git cherry-pick <commit>", language="bash")

    st.write("**Antes:**")
    st.image("assets/cherry_before.png", caption="Estrutura de branches antes do Cherry-Pick", width=344)
    
    st.write("**Depois:**")
    st.image("assets/cherry_after.png", caption="Histórico linear após o Cherry-Pick", width=344)

    st.subheader("Atualizar uma branch usando outra branch")
    st.write('Trás uma branch no mesmo ponto que outra está (também conhecido como merge fast-forward)')
    st.code("git swith main \ngit merge banana", language="bash")

    st.write("**Antes:**")
    st.image("assets/update_branch_before.png", caption="Estrutura de branches antes do Update", width=344)
    
    st.write("**Depois:**")
    st.image("assets/update_branch_after.png", caption="Histórico linear após o Update", width=344)
