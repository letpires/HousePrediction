import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Carregar o pipeline (modelo e scaler)
pipeline = load('/Users/leticiapires/Desktop/HousePrediction/model_pipeline.joblib')
model = pipeline['model']
scaler = pipeline['scaler']
y_transform = pipeline['y_transform']  # Informação sobre a transformação da variável alvo

# # Título do app
# st.title('Previsão de Preços de Imóveis')

# Título estilizado do app
st.markdown(
    """
    <h1 style='color: #4A90E2; font-size: 42px;'>🏠 Previsão de Preços de Imóveis</h1>
    """,
    unsafe_allow_html=True
)

# Formulário centralizado
st.markdown("### Insira os dados do imóvel")

# st.markdown("""
# ### Descrição das variáveis:
# - **bedrooms**: Quantidade de quartos disponíveis em cada casa.  
# - **bathrooms**: Número de banheiros disponíveis em cada casa.  
# - **sqft_living**: Tamanho da área útil da casa em pés quadrados.  
# - **sqft_lot**: Área total do terreno em pés quadrados, incluindo a área ocupada pela casa e espaços externos, como jardim ou quintal.  
# - **floors**: Número de andares disponíveis na casa.  
# - **waterfront**: Indicador se a casa está localizada à beira de um lago ou praia (0: não possui vista para água, 1: possui).  
# - **view**: Avaliação visual do imóvel com base na vista disponível (escala de 0 a 4).  
# - **grade**: Classificação da qualidade do design e construção do imóvel, em uma escala de 1 a 12.  
# - **renovated**: 1 se foi renovado, 0 se não foi.  
# - **basement**: 1 se tem basement, 0 se não tem.  
# - **condition_encoded**: Condição geral da casa: 'Ruim', 'Média', 'Regular', 'Boa', 'Excelente' (escala de 1 a 5).  
# """)

# Descrição escondida usando st.expander
with st.expander("🔍 **Descrição das Variáveis**"):
    st.markdown("""
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


# Criando o formulário com as entradas
with st.form(key='form_dados'):
    bedrooms = st.number_input('Número de quartos', min_value=1, max_value=10, value=3)
    bathrooms = st.number_input('Número de banheiros', min_value=1, max_value=5, value=2)
    sqft_living = st.number_input('Área útil (em pés²)', min_value=500, max_value=10000, value=1500)
    sqft_lot = st.number_input('Tamanho do lote (em pés²)', min_value=500, max_value=50000, value=5000)
    floors = st.number_input('Número de andares', min_value=1, max_value=3, value=1)
    waterfront = st.selectbox('Possui vista para a água?', [0, 1], format_func=lambda x: 'Sim' if x == 1 else 'Não')
    view = st.slider('Vista (escala de 0 a 4)', min_value=0, max_value=4, value=0)
    grade = st.slider('Classificação do imóvel (1 a 12)', min_value=1, max_value=12, value=7)
    renovated = st.selectbox('Foi renovado?', [0, 1], format_func=lambda x: 'Sim' if x == 1 else 'Não')
    basement = st.number_input('Tamanho do porão (em pés²)', min_value=0, max_value=5000, value=0)
    condition_encoded = st.slider('Condição do imóvel (1 a 5)', min_value=1, max_value=5, value=3)

    # Botão de submissão
    submit_button = st.form_submit_button(label='Prever Preço')

# Processando a previsão
if submit_button:
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

    # Normalizar os dados de entrada
    nova_casa_scaled = scaler.transform(nova_casa)

    # Fazer a previsão
    y_pred_log = model.predict(nova_casa_scaled)

    # Reverter o log para a escala original, se necessário
    if y_transform == 'log':
        y_pred = np.exp(y_pred_log)
    else:
        y_pred = y_pred_log

    # # Mostrar o resultado
    # st.markdown("### Resultado da Previsão")
    # st.write(f'O preço estimado do imóvel é: **R${y_pred[0]:,.2f}**')

    # Mostrar o resultado com estilo
    st.markdown(
        f"""
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='color: #2E8B57;'>🏡 O preço estimado do imóvel é:</h2>
            <h1 style='color: #FF5733;'>R${y_pred[0]:,.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )




# bedrooms = st.sidebar.number_input('Número de quartos (bedrooms)', min_value=1, max_value=10, value=3, help="Quantidade de quartos disponíveis em cada casa.")
# bathrooms = st.sidebar.number_input('Número de banheiros (bathrooms)', min_value=1, max_value=5, value=2, help="Número de banheiros disponíveis em cada casa.")
# sqft_living = st.sidebar.number_input('Área útil (em pés²) (sqft_living)', min_value=500, max_value=10000, value=1500, help="Tamanho da área útil da casa em pés quadrados.")
# sqft_lot = st.sidebar.number_input('Tamanho do lote (em pés²) (sqft_lot)', min_value=500, max_value=50000, value=5000, help="Área total do terreno em pés quadrados, incluindo a área ocupada pela casa e espaços externos.")
# floors = st.sidebar.number_input('Número de andares (floors)', min_value=1, max_value=3, value=1, help="Número de andares disponíveis na casa.")
# waterfront = st.sidebar.selectbox('Possui vista para a água? (waterfront)', [0, 1], help="Indicador se a casa está localizada à beira de um lago ou praia (0: não possui vista para água, 1: possui).")
# view = st.sidebar.slider('Vista (escala de 0 a 4) (view)', min_value=0, max_value=4, value=0, help="Avaliação visual do imóvel com base na vista disponível (cidade, lago ou praia).")
# grade = st.sidebar.slider('Classificação do imóvel (1 a 12) (grade)', min_value=1, max_value=12, value=7, help="Classificação da qualidade do design e construção do imóvel, em uma escala de 1 a 12.")
# renovated = st.sidebar.selectbox('Foi renovado? (renovated)', [0, 1], help="1 se foi renovado, 0 se não foi.")
# basement = st.sidebar.number_input('Tamanho do porão (em pés²) (basement)', min_value=0, max_value=5000, value=0, help="Tamanho do porão da casa, em pés quadrados (0 se não tiver porão).")
# condition_encoded = st.sidebar.slider('Condição do imóvel (1 a 5) (condition_encoded)', min_value=1, max_value=5, value=3, help="Condição geral da casa: 'Ruim', 'Média', 'Regular', 'Boa', 'Excelente' (escala de 1 a 5).")

# # Organizar os dados de entrada
# nova_casa = pd.DataFrame({
#     'bedrooms': [bedrooms],
#     'bathrooms': [bathrooms],
#     'sqft_living': [sqft_living],
#     'sqft_lot': [sqft_lot],
#     'floors': [floors],
#     'waterfront': [waterfront],
#     'view': [view],
#     'grade': [grade],
#     'renovated': [renovated],
#     'basement': [basement],
#     'condition_encoded': [condition_encoded]
# })

# # Botão para realizar a previsão
# if st.sidebar.button('Prever Preço'):
#     # Normalizar os dados de entrada
#     nova_casa_scaled = scaler.transform(nova_casa)

#     # Fazer a previsão
#     y_pred_log = model.predict(nova_casa_scaled)

#     # Reverter o log para a escala original, se necessário
#     if y_transform == 'log':
#         y_pred = np.exp(y_pred_log)
#     else:
#         y_pred = y_pred_log

#     # Exibir o resultado
#     st.subheader('Resultado da Previsão')
#     st.write(f'O preço estimado do imóvel é: **R${y_pred[0]:,.2f}**')
