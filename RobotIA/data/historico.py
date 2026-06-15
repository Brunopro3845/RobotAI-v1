import json
import os

ARQUIVO = "data/historico.json"

def carregar_historico():

    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    return []

def salvar_historico(historico):

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=4)