import streamlit as st
import pandas as pd
import numpy as np
import joblib  # Para carregar o modelo treinado

# Carregar o modelo
model = joblib.load('modelo_previsao.pkl')

# Dados históricos para exemplo
dados_historicos = pd.DataFrame({
    'num_quartos': [2, 3, 4],
    'num_banheiros': [1, 2, 3],
    'tamanho_m2': [80, 120, 200],
    'localizacao': ['Centro', 'Subúrbio', 'Rural'],
    'original_price': [200000, 300000, 500000],
    'preco_previsto': [210000, 290000, 480000]
})

# Título do app
st.title('Previsão de Preços de Imóveis')

# Exibição dos dados históricos
st.header('Dados Históricos')
st.dataframe(dados_historicos)

# Formulário para nova previsão
st.sidebar.header('Insira os dados do imóvel')
num_quartos = st.sidebar.number_input('Número de quartos', min_value=1, max_value=10, value=3)
num_banheiros = st.sidebar.number_input('Número de banheiros', min_value=1, max_value=5, value=2)
tamanho_m2 = st.sidebar.number_input('Tamanho (m²)', min_value=10, max_value=500, value=120)
localizacao = st.sidebar.selectbox('Localização', ['Centro', 'Subúrbio', 'Rural'])

# Organizar dados de entrada
nova_casa = pd.DataFrame({
    'num_quartos': [num_quartos],
    'num_banheiros': [num_banheiros],
    'tamanho_m2': [tamanho_m2],
    'localizacao': [localizacao]
})

# Botão para prever o preço
if st.sidebar.button('Prever Preço'):
    preco_previsto = model.predict(nova_casa)[0]
    st.subheader('Resultado da Previsão')
    st.write(f'Preço estimado: **R${preco_previsto:,.2f}**')

# Gráfico de comparação (preços originais vs. previstos)
st.header('Comparação de Preços')
st.bar_chart(dados_historicos[['original_price', 'preco_previsto']])
