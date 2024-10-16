# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 11:24:46 2024

@author: Allan Cardoso Araujo
"""

# Importando as bibliotecas necessárias
import pandas as pd           # Para manipulação e análise de dados
import plotly.express as px    # Para criar gráficos interativos
import streamlit as st         # Para criar a interface web interativa

# LENDO O DATASET
# O dataset é carregado diretamente de um arquivo CSV hospedado no GitHub.
# O arquivo contém dados da COVID-19 por estado no Brasil.
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# MELHORANDO O NOME DAS COLUNAS DA TABELA
# As colunas que contêm dados importantes são renomeadas para termos mais intuitivos em português,
# facilitando a compreensão por parte dos usuários.
df = df.rename(columns={
    'newDeaths': 'Novos óbitos',  # Novos óbitos confirmados
    'newCases': 'Novos casos',    # Novos casos confirmados
    'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes',  # Óbitos ajustados para cada 100 mil habitantes
    'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'  # Casos ajustados para cada 100 mil habitantes
})

# SELEÇÃO DO ESTADO
# Uma lista contendo todos os estados disponíveis no dataset é criada.
# O usuário escolhe um estado específico a partir de um menu suspenso (selectbox) na barra lateral da aplicação.
estados = list(df['state'].unique())  # Lista dos estados disponíveis
state = st.sidebar.selectbox('Qual estado?', estados)  # Caixa de seleção para escolher o estado

# SELEÇÃO DA COLUNA
# O usuário pode escolher qual tipo de dado quer visualizar (novos óbitos, novos casos, etc.),
# também através de um menu suspenso (selectbox) na barra lateral.
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']  # Tipos de dados disponíveis
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)  # Caixa de seleção para escolher o tipo de dado

# FILTRANDO OS DADOS POR ESTADO
# Após o estado ser selecionado, o dataset é filtrado para incluir apenas as informações
# do estado escolhido pelo usuário.
df = df[df['state'] == state]  # Filtra as linhas que pertencem ao estado selecionado

# CRIAÇÃO DO GRÁFICO
# Um gráfico de linha é gerado usando o Plotly, onde o eixo X representa as datas e o eixo Y
# representa o tipo de dado escolhido (novos óbitos, novos casos, etc.).
# O título do gráfico é dinâmico, combinando o dado selecionado e o estado escolhido.
fig = px.line(df, x="date", y=column, title=column + ' - ' + state)

# CONFIGURAÇÃO DO LAYOUT DO GRÁFICO
# O título do eixo X é configurado como 'Data' e o título do eixo Y é configurado com o nome da coluna (em letras maiúsculas).
# O título do gráfico é centralizado.
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title={'x': 0.5})

# EXIBIÇÃO DA APLICAÇÃO NO STREAMLIT
# O título da aplicação é exibido no topo da página.
st.title('DADOS COVID - BRASIL')

# Texto explicativo é exibido, informando ao usuário que ele pode selecionar o estado e o tipo de informação desejada.
st.write('Nesta aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')

# O gráfico gerado é exibido na interface Streamlit, ajustando automaticamente para ocupar a largura da tela disponível.
st.plotly_chart(fig, use_container_width=True)

# FONTE DOS DADOS
# Um pequeno texto de rodapé é exibido, informando que os dados foram obtidos a partir do repositório no GitHub.
st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
