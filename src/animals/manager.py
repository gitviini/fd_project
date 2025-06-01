""" 
* MANAGER ANIMALS DATA
"""
import json
import os

ARQUIVO_JSON = os.path.join(os.path.dirname(__file__), "../../jsons/animals.json")

def carregar_dados():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return {}

def salvar_dados(banco_dados):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(banco_dados, arquivo, ensure_ascii=False, indent=4)
