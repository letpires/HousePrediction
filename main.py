from fastapi import FastAPI, HTTPException
import kagglehub
import os
import subprocess
import zipfile

app = FastAPI()

# Configurações do projeto
MAIN_DIR = 'house_sales_king_county_data'
CSV_DIR = os.path.join(MAIN_DIR, 'csv_files')
DATASET_NAME = 'house-sales-in-king-county'
KAGGLE_JSON_PATH = os.path.join('config', 'kaggle.json')  # Caminho do arquivo kaggle.json
KAGGLE_USERNAME = "osmanlira"  # Substitua pelo seu username no Kaggle
KAGGLE_KEY = "fe2ecffc83eeb878766e24704be67745"        # Substitua pela sua API key do Kaggle
DATASET_URL = "https://www.kaggle.com/api/v1/datasets/download/harlfoxem/housesalesprediction"
DOWNLOAD_PATH = os.path.expanduser("~/Downloads/housesalesprediction.zip")
EXTRACTION_DIR = os.path.join(os.getcwd(), "downloads")


def download_dataset():
    """Baixa o dataset usando curl"""
    # Cria a pasta de downloads se não existir
    os.makedirs(os.path.dirname(DOWNLOAD_PATH), exist_ok=True)

    # Define as variáveis de ambiente para a API do Kaggle
    os.environ["KAGGLE_USERNAME"] = KAGGLE_USERNAME
    os.environ["KAGGLE_KEY"] = KAGGLE_KEY

    # Comando curl para baixar o dataset
    curl_command = [
        "curl",
        "-L",  # Seguir redirecionamentos
        "-o", DOWNLOAD_PATH,  # Caminho do arquivo de destino
        DATASET_URL,  # URL do dataset
        "--user", f"{KAGGLE_USERNAME}:{KAGGLE_KEY}"  # Autenticação da API
    ]

    try:
        print("Baixando o dataset...")
        subprocess.run(curl_command, check=True)
        print(f"Download concluído! Arquivo salvo em: {DOWNLOAD_PATH}")
        return DOWNLOAD_PATH
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Erro ao baixar o dataset: {str(e)}")


def extract_dataset(zip_path, extract_to):
    """Extrai o conteúdo do arquivo ZIP para a pasta especificada"""
    try:
        print(f"Extraindo o conteúdo do arquivo ZIP para {extract_to}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("Extração concluída.")
    except zipfile.BadZipFile:
        raise HTTPException(status_code=500, detail="Erro ao extrair o arquivo ZIP. O arquivo pode estar corrompido.")


@app.post("/download-and-extract/")
def download_and_extract_endpoint():
    """Endpoint para baixar e descompactar o dataset"""
    # Baixa o arquivo
    zip_path = download_dataset()
    
    # Extrai o conteúdo para a pasta 'downloads'
    extract_dataset(zip_path, EXTRACTION_DIR)
    
    # Lista os arquivos extraídos
    extracted_files = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(EXTRACTION_DIR)
        for file in files
    ]
    
    return {
        "message": "Dataset baixado e extraído com sucesso.",
        "extracted_files": extracted_files
    }   

# Função para extrair arquivos CSV
def extract_csv(zip_path, dest_dir):
    """Extrai arquivos CSV do ZIP"""
    os.makedirs(dest_dir, exist_ok=True)
    if os.path.exists(zip_path):
        try:
            print("Descompactando os arquivos...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                for file in zip_ref.namelist():
                    if file.endswith('.csv'):
                        zip_ref.extract(file, dest_dir)
            os.remove(zip_path)  # Remove o arquivo ZIP após extração
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao extrair os arquivos: {str(e)}")
    else:
        raise HTTPException(status_code=404, detail="Arquivo ZIP não encontrado para extração.")


# Função para listar os arquivos CSV
def list_csv_files(dest_dir):
    """Lista os arquivos CSV disponíveis"""
    if not os.path.exists(dest_dir):
        raise HTTPException(status_code=404, detail="Diretório de arquivos CSV não encontrado.")
    csv_files = []
    for root, dirs, files in os.walk(dest_dir):
        for file in files:
            csv_files.append(os.path.join(root, file))
    return csv_files


@app.get("/list-csvs/")
def list_csvs_endpoint():
    """Endpoint para listar os arquivos .csv na pasta downloads"""
    csv_files = list_csv_files(EXTRACTION_DIR)
    return {"csv_files": csv_files}
