import customtkinter as ctk
import threading
from tkinter import filedialog

from chatbot import perguntar_ia
from historico import carregar_historico, salvar_historico
from memoria import carregar_memoria, salvar_memoria


# =========================
# CONFIGURAÇÃO VISUAL
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# =========================
# DADOS GLOBAIS
# =========================

historico = carregar_historico()
memoria = carregar_memoria()

chat = None
entrada = None
janela = None


# =========================
# FUNÇÕES DE CHAT
# =========================

def adicionar_chat(texto):
    chat.insert("end", texto + "\n")
    chat.see("end")


def limpar_chat():
    historico.clear()
    salvar_historico(historico)

    chat.delete("1.0", "end")
    adicionar_chat("🤖 Chat limpo com sucesso!")


def exportar_chat():
    arquivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de Texto", "*.txt")]
    )

    if arquivo:
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(chat.get("1.0", "end"))

        adicionar_chat("📁 Chat exportado com sucesso!")


# =========================
# MEMÓRIA
# =========================

def atualizar_memoria(mensagem):

    global memoria

    if mensagem.lower().startswith("meu nome é"):
        nome = mensagem[11:].strip()
        memoria["nome"] = nome
        salvar_memoria(memoria)

        adicionar_chat(f"🧠 Memória salva: nome = {nome}")
        return True

    return False


# =========================
# IA
# =========================

def construir_prompt(mensagem):

    contexto = ""

    for item in historico[-10:]:
        contexto += f"{item['autor']}: {item['mensagem']}\n"

    prompt = f"""
Você é a RobotIA, uma assistente virtual inteligente.

Responda sempre em português brasileiro.

MEMÓRIA DO USUÁRIO:
{memoria}

CONVERSA RECENTE:
{contexto}

Usuário: {mensagem}
RobotIA:
"""

    return prompt


def responder_ia(mensagem):

    prompt = construir_prompt(mensagem)

    resposta = perguntar_ia(prompt)

    historico.append({
        "autor": "RobotIA",
        "mensagem": resposta
    })

    salvar_historico(historico)

    chat.after(
        0,
        lambda: adicionar_chat(f"🤖 RobotIA:\n{resposta}")
    )


# =========================
# ENVIO DE MENSAGEM
# =========================

def enviar(event=None):

    mensagem = entrada.get().strip()

    if not mensagem:
        return

    entrada.delete(0, "end")

    # memória
    if atualizar_memoria(mensagem):
        return

    historico.append({
        "autor": "Usuário",
        "mensagem": mensagem
    })

    salvar_historico(historico)

    adicionar_chat(f"👤 Você: {mensagem}")
    adicionar_chat("🤖 RobotIA: pensando...")

    threading.Thread(
        target=responder_ia,
        args=(mensagem,),
        daemon=True
    ).start()


# =========================
# TEMA
# =========================

def alternar_tema():

    atual = ctk.get_appearance_mode()

    if atual == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")


# =========================
# INTERFACE
# =========================

def iniciar_interface():

    global chat, entrada, janela

    janela = ctk.CTk()
    janela.title("🤖 RobotIA")
    janela.geometry("1000x700")

    ctk.CTkLabel(
        janela,
        text="🤖 RobotIA",
        font=("Arial", 28, "bold")
    ).pack(pady=10)

    chat = ctk.CTkTextbox(janela, font=("Consolas", 14))
    chat.pack(fill="both", expand=True, padx=20, pady=10)

    adicionar_chat("🤖 RobotIA iniciada!")

    frame = ctk.CTkFrame(janela)
    frame.pack(fill="x", padx=20, pady=10)

    entrada = ctk.CTkEntry(frame, placeholder_text="Digite sua mensagem...")
    entrada.pack(side="left", fill="x", expand=True, padx=10, pady=10)

    entrada.bind("<Return>", enviar)

    ctk.CTkButton(frame, text="Enviar", command=enviar).pack(side="left", padx=5)
    ctk.CTkButton(frame, text="Limpar", command=limpar_chat).pack(side="left", padx=5)
    ctk.CTkButton(frame, text="Exportar", command=exportar_chat).pack(side="left", padx=5)
    ctk.CTkButton(frame, text="Tema", command=alternar_tema).pack(side="left", padx=5)

    janela.mainloop()


if __name__ == "__main__":
    iniciar_interface()