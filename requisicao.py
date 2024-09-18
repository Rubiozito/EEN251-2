import requests
from dotenv import load_dotenv
import os

def send_data(score):
    load_dotenv()
    # Seu token de autenticação do Ubidots STEM (substitua pelo seu)
    TOKEN = os.getenv("TOKEN")
    # Label do dispositivo para onde você quer enviar os dados
    DEVICE_LABEL = os.getenv("DEVICE_LABEL")
    # URL da API Ubidots para o STEM
    API_URL = f"http://things.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}/"

    # Cabeçalhos da requisição
    headers = {
        "X-Auth-Token": TOKEN,
        "Content-Type": "application/json"
    }

    # Dados que você deseja enviar
    payload = {
        "score": score
    }

    # Fazendo o envio dos dados
    response = requests.post(API_URL, json=payload, headers=headers)

    # Verifica se o envio foi bem-sucedido
    if response.status_code == 200:
        print("Dados enviados com sucesso!")
    else:
        print(f"Erro ao enviar dados: {response.status_code}")
        print(response.json())
