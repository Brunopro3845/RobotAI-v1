import json
import os

ARQUIVO = "data/memoria.json"

def carregar_memoria():

    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}

    return {}

def salvar_memoria(memoria):

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=4)