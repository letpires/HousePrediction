# 🏠 Previsão de Preços de Imóveis

Projeto que utiliza Machine Learning para prever o preço de imóveis com base em características fornecidas pelo usuário. O projeto possui uma API FastAPI para download e preparação do dataset e uma interface Streamlit que permite interação com o modelo preditivo treinado.

<h2>📁 Estrutura do Projeto</h2>

<pre>
project/
├── downloads/               # Diretório onde os datasets são armazenados e extraídos
├── config/                  # Configurações adicionais do projeto
├── venv/                    # Ambiente virtual do Python
├── predicao_casas.ipynb     # Notebook usado para análise de dados, processamento e criação do modelo
├── app_streamlit.py         # Aplicação Streamlit para interface com o usuário
├── main.py                  # Código principal da API (FastAPI)
├── model_pipeline.joblib    # Modelo preditivo serializado
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
</pre>

<hr>

<h2>🚀 Instalação e Configuração</h2>

<h3>1. Criar Ambiente Virtual</h3>
<pre>
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
</pre>

<h3>2. Instalar Dependências</h3>
<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>🌐 API - Gerenciamento do Dataset</h2>

<p>A <strong>API FastAPI</strong> é responsável pelo download, extração e listagem do dataset.</p>

<h3>Executar a API</h3>
<pre>
uvicorn main:app --reload
</pre>

Isso iniciará o servidor na porta 8000 por padrão. Você pode acessar a documentação interativa da API em http://127.0.0.1:8000/docs.

<h3>Endpoints</h3>

<h4>📥 <strong>Download e Extração do Dataset</strong></h4>
<ul>
  <li><strong>URL:</strong> <code>/download-and-extract/</code></li>
  <li><strong>Método:</strong> <code>POST</code></li>
  <li><strong>Descrição:</strong> Baixa o dataset do Kaggle, descompacta o arquivo .zip e retorna uma lista de arquivos extraídos.</li>
</ul>
<p><strong>Exemplo de Resposta:</strong></p>
<pre>
{
  "message": "Dataset baixado e extraído com sucesso.",
  "extracted_files": [
    "/path/to/project/downloads/file1.csv",
    "/path/to/project/downloads/file2.csv"
  ]
}
</pre>

<h4>📄 <strong>Listar Arquivos <code>.csv</code></strong></h4>
<ul>
  <li><strong>URL:</strong> <code>/list-csvs/</code></li>
  <li><strong>Método:</strong> <code>GET</code></li>
  <li><strong>Descrição:</strong> Lista todos os arquivos <code>.csv</code> armazenados em <code>/downloads</code>.</li>
</ul>
<p><strong>Exemplo de Resposta:</strong></p>
<pre>
{
  "csv_files": [
    "/path/to/project/downloads/file1.csv",
    "/path/to/project/downloads/file2.csv"
  ]
}
</pre>

<hr>

<h2>🤖 Modelo Preditivo</h2>

<p>O modelo é treinado utilizando o arquivo <strong>predicao_casas.ipynb</strong>, que realiza:</p>
<ol>
  <li><strong>Pré-processamento dos Dados</strong>.</li>
  <li><strong>Treinamento do Modelo</strong>.</li>
  <li><strong>Exportação do Modelo</strong> serializado com <code>joblib</code> em <code>model_pipeline.joblib</code>.</li>
</ol>

<hr>

<h2>📊 Interface do Usuário - Streamlit</h2>

<p>O arquivo <code>app_streamlit.py</code> fornece uma interface interativa para inserir as características do imóvel e prever o preço.</p>

<h3>Executar o Streamlit</h3>
<pre>
streamlit run app_streamlit.py
</pre>

<h3>🎯 Funcionalidades da Interface</h3>
<ul>
  <li><strong>Inserir Características do Imóvel:</strong> Quartos, banheiros, área útil, etc.</li>
  <li><strong>Prever o Preço:</strong> Clique no botão <strong>"Prever Preço"</strong>.</li>
  <li><strong>Receber a Previsão:</strong> O preço é calculado com base no modelo treinado.</li>
</ul>

<h3>📝 Variáveis de Entrada</h3>

<table>
  <thead>
    <tr>
      <th>Variável</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>bedrooms</code></td>
      <td>Quantidade de quartos.</td>
    </tr>
    <tr>
      <td><code>bathrooms</code></td>
      <td>Número de banheiros.</td>
    </tr>
    <tr>
      <td><code>sqft_living</code></td>
      <td>Área útil da casa em pés quadrados.</td>
    </tr>
    <tr>
      <td><code>sqft_lot</code></td>
      <td>Tamanho do terreno.</td>
    </tr>
    <tr>
      <td><code>floors</code></td>
      <td>Número de andares.</td>
    </tr>
    <tr>
      <td><code>waterfront</code></td>
      <td>Vista para a água (<code>Sim</code>/<code>Não</code>).</td>
    </tr>
    <tr>
      <td><code>view</code></td>
      <td>Avaliação da vista (0-4).</td>
    </tr>
    <tr>
      <td><code>grade</code></td>
      <td>Qualidade da construção (1-12).</td>
    </tr>
    <tr>
      <td><code>yr_renovated</code></td>
      <td>Ano de renovação (ou 0).</td>
    </tr>
    <tr>
      <td><code>basement</code></td>
      <td>Tamanho do porão em pés².</td>
    </tr>
    <tr>
      <td><code>condition_encoded</code></td>
      <td>Condição da casa (<code>Ruim</code>, <code>Média</code>, etc.).</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>🛠 Tecnologias Utilizadas</h2>
<ul>
  <li><strong>Python:</strong> Linguagem principal.</li>
  <li><strong>FastAPI:</strong> Framework para API.</li>
  <li><strong>Streamlit:</strong> Interface gráfica.</li>
  <li><strong>Joblib:</strong> Serialização do modelo.</li>
  <li><strong>Pandas/Numpy:</strong> Processamento de dados.</li>
  <li><strong>Uvicorn:</strong> Servidor para API.</li>
</ul>

<hr>

<h2>🏁 Próximos Passos</h2>
<ul>
  <li>Melhorar o desempenho do modelo.</li>
  <li>Adicionar testes automatizados.</li>
  <li>Melhorar a interface da aplicação Streamlit.</li>
</ul>

<hr>

<h2>✨ Demonstração</h2>

![Demonstração da Aplicação](https://github.com/letpires/PredicaoCasas/blob/main/demonstracao.gif)
