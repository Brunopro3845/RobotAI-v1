#  RobotIA

Uma assistente virtual em Python com interface gráfica, memória permanente e integração com IA local via Ollama.

---

##  Sobre o projeto

O **RobotIA** é uma IA pessoal desenvolvida em Python que combina:

-  Chat inteligente com IA local (Ollama)
-  Interface gráfica moderna (CustomTkinter)
-  Memória permanente do usuário
-  Histórico de conversas
-  Sistema de voz (opcional)
-  Exportação de conversas
-  Tema escuro/claro

---

##  Tecnologias utilizadas

- Python 3.10+
- CustomTkinter
- Requests
- JSON (memória e histórico)
- Threading
- Ollama (modelo local de IA)

---

##  Instalação

### 1. Clone o repositório

git clone https://github.com/seu-usuario/RobotIA.git
cd RobotIA

---

### 2. Instale as dependências

pip install customtkinter requests

---

### 3. Instale e rode o Ollama

Baixe em:
https://ollama.com

Depois rode:

ollama run qwen2.5:0.5b

---

##  Como executar

python main.py

---

##  Funcionalidades

###  Chat com IA
Conversa inteligente com modelo local via Ollama.

###  Memória permanente
A IA pode lembrar informações do usuário:

meu nome é Bruno

---

###  Histórico
Todas as conversas são salvas automaticamente.

---

###  Exportar conversa
Permite salvar o chat em .txt.

---

###  Interface moderna
Interface gráfica estilo aplicativo usando CustomTkinter.

---

###  (Opcional) Voz
A IA pode falar respostas usando sistema de TTS.

---

##  Estrutura do projeto

RobotIA/
│
├── main.py
├── interface.py
├── chatbot.py
├── historico.py
├── memoria.py
│
├── data/
├── logs/
├── memory/
└── assets/

---

##  Requisitos

- Python 3.10 ou superior
- Ollama rodando localmente
- Conexão local ativa (localhost:11434)

---

##  Exemplo de uso

Você: meu nome é Bruno  
RobotIA: Vou lembrar disso!

Você: quem sou eu?  
RobotIA: Seu nome é Bruno.

---

##  Próximas melhorias

-  Reconhecimento de voz (fala → texto)
-  Memória inteligente avançada
-  Múltiplas conversas
-  Versão online
-  App mobile

---

##  Autor

Projeto desenvolvido por Bruno Miguel
