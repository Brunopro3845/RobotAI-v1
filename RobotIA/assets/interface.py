import customtkinter as ctk
import threading
from tkinter import filedialog

from chatbot import perguntar_ia
from data.historico import carregar_historico, salvar_historico
from data.memoria import carregar_memoria, salvar_memoria

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

historico = carregar_historico()
memoria = carregar_memoria()


def adicionar_chat(texto):
    chat.insert("end", texto + "\n")
    chat.see("end")


def exportar_chat():

    arquivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Texto", "*.txt")]
    )

    if arquivo:
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(chat.get("1.0", "end"))


def limpar_chat():

    chat.delete("1.0", "end")
    historico.clear()

    salvar_historico(historico)

    adicionar_chat("🤖 Conversa limpa.")


def responder(mensagem):

    contexto = ""

    for item in historico[-10:]:

        contexto += (
            f"{item['autor']}: "
            f"{item['mensagem']}\n"
        )

    prompt = f"""
Você é a RobotIA.

Responda sempre em português brasileiro.

MEMÓRIA:
{memoria}

CONVERSA:
{contexto}

Usuário: {mensagem}
RobotIA:
"""

    resposta = perguntar_ia(prompt)

    historico.append({
        "autor": "RobotIA",
        "mensagem": resposta
    })

    salvar_historico(historico)

    chat.after(
        0,
        lambda: adicionar_chat(
            f"\n🤖 RobotIA:\n{resposta}"
        )
    )


def enviar(event=None):

    mensagem = entrada.get().strip()

    if not mensagem:
        return

    entrada.delete(0, "end")

    if mensagem.lower().startswith("meu nome é"):

        nome = mensagem[11:].strip()

        memoria["nome"] = nome

        salvar_memoria(memoria)

        adicionar_chat(
            f"\n🤖 Vou lembrar que seu nome é {nome}."
        )

        return

    if mensagem == "/memoria":

        adicionar_chat(
            f"\n🧠 Memória:\n{memoria}"
        )

        return

    historico.append({
        "autor": "Usuário",
        "mensagem": mensagem
    })

    salvar_historico(historico)

    adicionar_chat(
        f"\n👤 Você:\n{mensagem}"
    )

    adicionar_chat(
        "\n🤖 RobotIA:\nPensando..."
    )

    threading.Thread(
        target=responder,
        args=(mensagem,),
        daemon=True
    ).start()


def alternar_tema():

    atual = ctk.get_appearance_mode()

    if atual == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")


def iniciar_interface():

    global janela
    global chat
    global entrada

    janela = ctk.CTk()

    janela.title("🤖 RobotIA")
    janela.geometry("1000x700")

    ctk.CTkLabel(
        janela,
        text="🤖 RobotIA",
        font=("Arial", 30, "bold")
    ).pack(pady=10)

    chat = ctk.CTkTextbox(
        janela,
        font=("Consolas", 14)
    )

    chat.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    adicionar_chat(
        "🤖 RobotIA iniciada."
    )

    frame = ctk.CTkFrame(janela)

    frame.pack(
        fill="x",
        padx=20,
        pady=10
    )

    entrada = ctk.CTkEntry(
        frame,
        placeholder_text="Digite sua mensagem..."
    )

    entrada.pack(
        side="left",
        fill="x",
        expand=True,
        padx=10,
        pady=10
    )

    entrada.bind("<Return>", enviar)

    ctk.CTkButton(
        frame,
        text="Enviar",
        command=enviar
    ).pack(side="left", padx=5)

    ctk.CTkButton(
        frame,
        text="Limpar",
        command=limpar_chat
    ).pack(side="left", padx=5)

    ctk.CTkButton(
        frame,
        text="Exportar",
        command=exportar_chat
    ).pack(side="left", padx=5)

    ctk.CTkButton(
        frame,
        text="Tema",
        command=alternar_tema
    ).pack(side="left", padx=5)

    janela.mainloop()

  

    
    
     