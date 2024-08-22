import streamlit as st
from conex import view_data





import pandas as pd



# Criando um DataFrame de exemplo
data = {'Coluna 1': [1, 2, 3, 4, 5] * 10,
        'Coluna 2': [10, 20, 30, 40, 50] * 10}
df = pd.DataFrame(data)

# Opção 1: Estilo CSS inline
st.write(df.style.set_properties(**{'width': '80%'}))

# Opção 2: Utilizando st.container()
with st.container():
    st.write("Alunos")
    st.dataframe(df, width=800)

# Opção 3: Utilizando o parâmetro width de st.dataframe()
st.dataframe(df, width=1000)