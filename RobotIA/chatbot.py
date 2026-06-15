import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen2.5:0.5b"


def perguntar_ia(prompt):

    try:
        resposta = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        resposta.raise_for_status()

        data = resposta.json()

        return data.get("response", "Sem resposta do modelo.")

    except requests.exceptions.ConnectionError:
        return "❌ Erro: não consegui conectar ao Ollama. Ele está aberto?"

    except requests.exceptions.Timeout:
        return "❌ Erro: a IA demorou demais para responder."

    except Exception as erro:
        return f"❌ Erro inesperado: {erro}"