import os
import sys
import time
import traceback
import importlib
from datetime import datetime


# =========================
# CONFIGURAÇÕES DO PROJETO
# =========================

APP_NAME = "RobotIA"
VERSION = "1.0.0"

REQUIRED_FILES = [
    "interface.py",
    "chatbot.py",
    "historico.py",
    "memoria.py"
]


# =========================
# LOG SYSTEM
# =========================

LOG_FILE = "logs.txt"


def log(msg):
    """Registra logs do sistema"""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] {msg}\n")
    except:
        pass


# =========================
# VERIFICAÇÕES DO SISTEMA
# =========================

def verificar_arquivos():
    """Verifica se arquivos essenciais existem"""

    faltando = []

    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            faltando.append(file)

    if faltando:
        print("❌ Arquivos faltando:")
        for f in faltando:
            print(" -", f)

        log(f"Arquivos faltando: {faltando}")
        return False

    return True


def verificar_python():
    """Verifica versão do Python"""

    version = sys.version_info

    print(f"🐍 Python {version.major}.{version.minor}.{version.micro}")

    if version.major < 3:
        print("❌ Python muito antigo!")
        return False

    return True


def verificar_imports():
    """Testa imports principais"""

    try:
        import chatbot
        import historico
        import memoria
        return True

    except Exception as e:
        print("❌ Erro nos imports:", e)
        log(f"Erro imports: {e}")
        return False


# =========================
# DIAGNÓSTICO DO SISTEMA
# =========================

def diagnostico():
    """Executa diagnóstico completo"""

    print("\n🔍 DIAGNÓSTICO DO SISTEMA")
    print("=" * 40)

    ok = True

    if not verificar_python():
        ok = False

    if not verificar_arquivos():
        ok = False

    if not verificar_imports():
        ok = False

    if ok:
        print("✅ Sistema OK")
        log("Sistema OK")
    else:
        print("❌ Problemas detectados")
        log("Problemas no sistema")

    return ok


# =========================
# INICIALIZAÇÃO SEGURA
# =========================

def inicializar_interface():
    """Importa e inicia interface de forma segura"""

    try:
        print("\n🚀 Iniciando interface...")

        from interface import iniciar_interface

        iniciar_interface()

    except ImportError as e:
        print("❌ Erro de import:")
        print(e)
        log(f"Import error: {e}")

    except Exception as e:
        print("❌ Erro inesperado:")
        print(e)
        log(traceback.format_exc())


# =========================
# MODO TERMINAL (FALLBACK)
# =========================

def modo_terminal():
    """Modo fallback caso GUI falhe"""

    print("\n⚠️ MODO TERMINAL ATIVADO")
    print("Digite 'sair' para encerrar\n")

    try:
        from chatbot import perguntar_ia

        while True:
            msg = input("Você: ")

            if msg.lower() == "sair":
                break

            resposta = perguntar_ia(msg)
            print("RobotIA:", resposta)

    except Exception as e:
        print("❌ Erro no modo terminal:", e)
        log(traceback.format_exc())


# =========================
# MENU PRINCIPAL
# =========================

def menu():
    """Menu principal do sistema"""

    print("\n" + "=" * 50)
    print(f"🤖 {APP_NAME} v{VERSION}")
    print("=" * 50)
    print("1 - Iniciar Interface (GUI)")
    print("2 - Modo Terminal")
    print("3 - Diagnóstico")
    print("4 - Sair")
    print("=" * 50)


# =========================
# LOOP PRINCIPAL
# =========================

def main():

    log("Sistema iniciado")

    while True:

        menu()

        opcao = input("\nEscolha: ").strip()

        if opcao == "1":
            log("Modo GUI escolhido")

            if diagnostico():
                inicializar_interface()
            else:
                print("⚠️ Problemas detectados, usando terminal")
                modo_terminal()

        elif opcao == "2":
            log("Modo terminal escolhido")
            modo_terminal()

        elif opcao == "3":
            diagnostico()
            input("\nEnter para continuar...")

        elif opcao == "4":
            print("👋 Encerrando RobotIA...")
            log("Sistema encerrado")
            break

        else:
            print("❌ Opção inválida")
            time.sleep(1)


# =========================
# PROTEÇÃO DE EXECUÇÃO
# =========================

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\n⚠️ Interrompido pelo usuário")
        log("Interrompido via teclado")

    except Exception as e:
        print("❌ Erro fatal:")
        print(e)

        log(traceback.format_exc())

        print("\n🔁 Tentando modo seguro...")
        modo_terminal()