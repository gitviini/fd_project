import json
import os

ARQUIVO_JSON = os.path.join(os.path.dirname(__file__), "../../jsons/animals.json")

def load_json():
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("Erro: o arquivo JSON está vazio ou corrompido. Retornando dicionário vazio.")
            return{}
    return{}

def save_json(banco_dados):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(banco_dados, arquivo, ensure_ascii=False, indent=4)