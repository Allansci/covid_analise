# -*- coding: utf-8 -*-
"""
Este código foi criado em:
Data: Quarta-feira, 15 de Outubro de 2024
Autor: Allan Cardoso Araujo
"""

# Importando as bibliotecas necessárias
import pandas as pd           # Usada para manipulação e análise de dados
import plotly.express as px    # Usada para criar gráficos interativos
import streamlit as st         # Usada para criar uma interface web interativa

# LENDO O DATASET
# O dataset contendo dados da COVID-19 no Brasil é carregado diretamente de um arquivo CSV disponível publicamente no GitHub.
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# MELHORANDO O NOME DAS COLUNAS DA TABELA
# As colunas são renomeadas para termos mais descritivos e intuitivos em português, tornando os dados mais fáceis de interpretar.
df = df.rename(columns={
    'newDeaths': 'Novos óbitos',  # Renomeia a coluna de novos óbitos
    'newCases': 'Novos casos',    # Renomeia a coluna de novos casos
    'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes',  # Óbitos ajustados para cada 100 mil habitantes
    'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'  # Casos ajustados para cada 100 mil habitantes
})

# SELEÇÃO DO ESTADO
# O usuário pode escolher o estado do Brasil para visualizar os dados. A lista de estados é extraída da coluna 'state' do dataset.
estados = list(df['state'].unique())  # Gera uma lista de todos os estados disponíveis no dataset
state = st.sidebar.selectbox('Qual estado?', estados)  # Cria um menu suspenso na barra lateral para o usuário selecionar o estado

# SELEÇÃO DA COLUNA
# O usuário pode escolher qual métrica deseja visualizar, como novos casos, novos óbitos, etc.
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']  # Define as opções de dados disponíveis
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)  # Cria um menu suspenso para o usuário escolher qual dado visualizar

# SELEÇÃO DAS LINHAS QUE PERTENCEM AO ESTADO
# Após a seleção do estado, o dataset é filtrado para incluir apenas as informações do estado escolhido pelo usuário.
df = df[df['state'] == state]  # Filtra os dados do dataset para o estado selecionado

# CRIAÇÃO DO GRÁFICO
# Um gráfico de linha é criado usando Plotly, onde o eixo X representa as datas e o eixo Y representa o dado selecionado.
# O título do gráfico é dinâmico, combinando o tipo de dado e o estado selecionado.
fig = px.line(df, x="date", y=column, title=column + ' - ' + state)

# CONFIGURAÇÃO DO LAYOUT DO GRÁFICO
# O layout do gráfico é ajustado, definindo o rótulo dos eixos e centralizando o título.
fig.update_layout(xaxis_title='Data',  # Define o título do eixo X como "Data"
                  yaxis_title=column.upper(),  # Define o título do eixo Y com o nome da coluna selecionada em letras maiúsculas
                  title={'x': 0.5})  # Centraliza o título do gráfico

# EXIBIÇÃO DO TÍTULO DA APLICAÇÃO
# Define o título da aplicação na interface.
st.title('DADOS COVID - BRASIL')

# TEXTO EXPLICATIVO PARA O USUÁRIO
# Um texto explicativo é exibido, instruindo o usuário sobre como interagir com a aplicação.
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')

# EXIBIÇÃO DO GRÁFICO
# O gráfico gerado é exibido na interface, ajustando sua largura automaticamente ao container.
st.plotly_chart(fig, use_container_width=True)

# EXIBIÇÃO DA FONTE DOS DADOS
# Um rodapé com a origem dos dados é exibido, promovendo a transparência sobre a fonte.
st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
