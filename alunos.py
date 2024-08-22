import streamlit as st
import pandas as pd
import sys
sys.path.append('C://Users//paulo//Desktop//curriculo')
from conex import view_data
import matplotlib.pyplot as plt
import matplotlib.figure as mfigure
import numpy as np


def banco_de_dados(x):
    if x == 'alunos':
        query = """
    SELECT 
    ID,
    Matricula,
    Nome,
    Sexo
    FROM alunos
"""
    elif x == 'nota':
        query = """
    SELECT 
    ID,
    Matricula,
    Nota,
    data
    FROM notas
"""
    else:
        print('escolha um banco corretamente')
    dados = view_data(query) 

    return pd.DataFrame(dados)

DF_Alunos = banco_de_dados('alunos')
DF_Alunos.columns = ['ID', 'Matricula', 'Nome', 'Sexo']
DF_Notas = banco_de_dados('nota')
DF_Notas.columns = ['ID', 'Matricula', 'Nota', 'data']


with st.container():
    st.write("Alunos")
    st.dataframe(DF_Alunos, width=1000, height=1000)