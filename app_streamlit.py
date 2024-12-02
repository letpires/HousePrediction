import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Carregar o pipeline (modelo e scaler)
pipeline = joblib.load('model_pipeline.joblib')
model = pipeline['model']
scaler = pipeline['scaler']
y_transform = pipeline['y_transform']  # Informação sobre a transformação da variável alvo

# Título do app
st.title('Previsão de Preços de Imóveis')

# Formulário para entrada de dados do imóvel
st.sidebar.header('Insira os dados do imóvel')

st.sidebar.markdown("""
### Descrição das variáveis:
- **bedrooms**: Quantidade de quartos disponíveis em cada casa.  
- **bathrooms**: Número de banheiros disponíveis em cada casa.  
- **sqft_living**: Tamanho da área útil da casa em pés quadrados.  
- **sqft_lot**: Área total do terreno em pés quadrados, incluindo a área ocupada pela casa e espaços externos, como jardim ou quintal.  
- **floors**: Número de andares disponíveis na casa.  
- **waterfront**: Indicador se a casa está localizada à beira de um lago ou praia (0: não possui vista para água, 1: possui).  
- **view**: Avaliação visual do imóvel com base na vista disponível (escala de 0 a 4).  
- **grade**: Classificação da qualidade do design e construção do imóvel, em uma escala de 1 a 12.  
- **renovated**: 1 se foi renovado, 0 se não foi.  
- **basement**: 1 se tem basement, 0 se não tem.  
- **condition_encoded**: Condição geral da casa: 'Ruim', 'Média', 'Regular', 'Boa', 'Excelente' (escala de 1 a 5).  
""")

bedrooms = st.sidebar.number_input('Número de quartos (bedrooms)', min_value=1, max_value=10, value=3, help="Quantidade de quartos disponíveis em cada casa.")
bathrooms = st.sidebar.number_input('Número de banheiros (bathrooms)', min_value=1, max_value=5, value=2, help="Número de banheiros disponíveis em cada casa.")
sqft_living = st.sidebar.number_input('Área útil (em pés²) (sqft_living)', min_value=500, max_value=10000, value=1500, help="Tamanho da área útil da casa em pés quadrados.")
sqft_lot = st.sidebar.number_input('Tamanho do lote (em pés²) (sqft_lot)', min_value=500, max_value=50000, value=5000, help="Área total do terreno em pés quadrados, incluindo a área ocupada pela casa e espaços externos.")
floors = st.sidebar.number_input('Número de andares (floors)', min_value=1, max_value=3, value=1, help="Número de andares disponíveis na casa.")
waterfront = st.sidebar.selectbox('Possui vista para a água? (waterfront)', [0, 1], help="Indicador se a casa está localizada à beira de um lago ou praia (0: não possui vista para água, 1: possui).")
view = st.sidebar.slider('Vista (escala de 0 a 4) (view)', min_value=0, max_value=4, value=0, help="Avaliação visual do imóvel com base na vista disponível (cidade, lago ou praia).")
grade = st.sidebar.slider('Classificação do imóvel (1 a 12) (grade)', min_value=1, max_value=12, value=7, help="Classificação da qualidade do design e construção do imóvel, em uma escala de 1 a 12.")
renovated = st.sidebar.selectbox('Foi renovado? (renovated)', [0, 1], help="1 se foi renovado, 0 se não foi.")
basement = st.sidebar.number_input('Tamanho do porão (em pés²) (basement)', min_value=0, max_value=5000, value=0, help="Tamanho do porão da casa, em pés quadrados (0 se não tiver porão).")
condition_encoded = st.sidebar.slider('Condição do imóvel (1 a 5) (condition_encoded)', min_value=1, max_value=5, value=3, help="Condição geral da casa: 'Ruim', 'Média', 'Regular', 'Boa', 'Excelente' (escala de 1 a 5).")

# Organizar os dados de entrada
nova_casa = pd.DataFrame({
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'sqft_living': [sqft_living],
    'sqft_lot': [sqft_lot],
    'floors': [floors],
    'waterfront': [waterfront],
    'view': [view],
    'grade': [grade],
    'renovated': [renovated],
    'basement': [basement],
    'condition_encoded': [condition_encoded]
})

# Botão para realizar a previsão
if st.sidebar.button('Prever Preço'):
    # Normalizar os dados de entrada
    nova_casa_scaled = scaler.transform(nova_casa)

    # Fazer a previsão
    y_pred_log = model.predict(nova_casa_scaled)

    # Reverter o log para a escala original, se necessário
    if y_transform == 'log':
        y_pred = np.exp(y_pred_log)
    else:
        y_pred = y_pred_log

    # Exibir o resultado
    st.subheader('Resultado da Previsão')
    st.write(f'O preço estimado do imóvel é: **R${y_pred[0]:,.2f}**')
