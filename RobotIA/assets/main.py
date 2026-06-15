import requests
import json
import os
from datetime import datetime

ARQUIVO_HISTORICO = "historico.json"

historico = []


def carregar_historico():
    global historico

    if os.path.exists(ARQUIVO_HISTORICO):
        try:
            with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
                historico = json.load(f)
        except:
            historico = []


def salvar_historico():
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=4)


def mostrar_ajuda():
    print("\n=== COMANDOS DISPONÍVEIS ===")
    print("/ajuda      - Mostrar ajuda")
    print("/limpar     - Limpar memória da conversa")
    print("/historico  - Ver histórico atual")
    print("/exportar   - Exportar conversa para TXT")
    print("/hora       - Mostrar horário")
    print("/sair       - Encerrar RobotIA")


def exportar_conversa():
    nome = f"conversa_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(nome, "w", encoding="utf-8") as f:
        for item in historico:
            f.write(f"{item['autor']}: {item['mensagem']}\n")

    print(f"\n✅ Conversa exportada para {nome}")


def montar_contexto():
    contexto = ""

    for item in historico[-20:]:
        contexto += f"{item['autor']}: {item['mensagem']}\n"

    return contexto


def perguntar_ia(pergunta):
    contexto = montar_contexto()

    prompt = f"""
Você é a RobotIA.
Responda sempre em português brasileiro.
Seja educada, útil e objetiva.

{contexto}

Usuário: {pergunta}
RobotIA:
"""

    try:
        resposta = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:0.5b",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        resposta.raise_for_status()

        return resposta.json()["response"]

    except requests.exceptions.ConnectionError:
        return "Não consegui conectar ao Ollama. Verifique se ele está aberto."

    except requests.exceptions.Timeout:
        return "A resposta demorou muito para chegar."

    except Exception as erro:
        return f"Erro: {erro}"


def main():
    carregar_historico()

    print("=" * 40)
    print("🤖 RobotIA v2")
    print("=" * 40)
    print("Digite /ajuda para ver os comandos.")
    print()

    while True:
        pergunta = input("Você: ").strip()

        if not pergunta:
            continue

        if pergunta == "/sair":
            salvar_historico()
            print("Até logo!")
            break

        elif pergunta == "/ajuda":
            mostrar_ajuda()
            continue

        elif pergunta == "/limpar":
            historico.clear()
            salvar_historico()
            print("✅ Memória limpa.")
            continue

        elif pergunta == "/historico":
            print("\n=== HISTÓRICO ===")

            if not historico:
                print("Nenhuma conversa registrada.")
            else:
                for item in historico:
                    print(f"{item['autor']}: {item['mensagem']}")

            continue

        elif pergunta == "/exportar":
            exportar_conversa()
            continue

        elif pergunta == "/hora":
            agora = datetime.now().strftime("%H:%M:%S")
            print(f"\n🕒 Horário atual: {agora}")
            continue

        historico.append({
            "autor": "Usuário",
            "mensagem": pergunta
        })

        resposta = perguntar_ia(pergunta)

        historico.append({
            "autor": "RobotIA",
            "mensagem": resposta
        })

        salvar_historico()

        print(f"\n RobotIA: {resposta}\n")


if __name__ == "__main__":
    main()

    from interface import iniciar_interface

if __name__ == "__main__":
    iniciar_interface()