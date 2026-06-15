import json
import os

ARQUIVO = "historico.json"


def carregar_historico():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_historico(historico):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=4, ensure_ascii=False)