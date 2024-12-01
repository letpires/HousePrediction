# House Prediction
Projeto em andamento para a fase 3 da POSTECH 
https://www.kaggle.com/datasets/harlfoxem/housesalesprediction

# criando Ambiente
python -m venv venv
source venv/bin/activate  # No Linux/MacOS
venv\Scripts\activate # No Windows

# Instalação de Dependências
pip install -r requirements.txt

# Executando a API
uvicorn main:app --reload

# estrutura do Projeto
project/
├── downloads/              # Diretório onde os datasets são armazenados e extraídos
├── main.py                 # Código principal da API
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
└── .gitignore              # Arquivos/diretórios ignorados no Git

# Baixar e Descompactar o Dataset
Endpoint: /download-and-extract/
Método: POST
Descrição: Baixa o dataset do Kaggle, descompacta o arquivo .zip e retorna uma lista de arquivos extraídos.
Exemplo de Resposta:
{
    "message": "Dataset baixado e extraído com sucesso.",
    "extracted_files": [
        "/path/to/project/downloads/file1.csv",
        "/path/to/project/downloads/file2.csv"
    ]
}
# Listar Arquivos .csv
Endpoint: /list-csvs/
Método: GET
Descrição: Lista todos os arquivos .csv na pasta downloads.
Exemplo de Resposta:
{
    "csv_files": [
        "/path/to/project/downloads/file1.csv",
        "/path/to/project/downloads/file2.csv"
    ]
}
