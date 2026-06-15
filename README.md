Assistente de IA Local em Python






Visão geral

Este projeto é um assistente de inteligência artificial local desenvolvido em Python, com interface gráfica e integração com modelos de linguagem (LLMs), como Ollama.

O objetivo é criar um chatbot funcional, leve e extensível, capaz de rodar localmente, armazenar histórico e manter memória básica de conversação.

Funcionalidades
Chat inteligente com IA local
Integração com modelos LLM (Ollama ou similares)
Interface gráfica com CustomTkinter
Histórico de conversas persistente
Sistema de memória local simples
Execução em tempo real com threads
Arquitetura do projeto

O projeto foi organizado de forma modular para facilitar manutenção e escalabilidade.

.
├── main.py              # Interface principal
├── chatbot.py          # Comunicação com IA
├── memoria.py          # Sistema de memória local
├── historico.py        # Controle de histórico
├── assets/             # Recursos visuais
└── README.md
Interface


Tecnologias utilizadas
Python 3.x
CustomTkinter
Requests
Threading
Ollama API ou outro LLM local
Tkinter
Como executar
Clonar o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPO.git
cd SEU_REPO
Instalar dependências
pip install -r requirements.txt
Executar o projeto
python main.py
Objetivo do projeto

Este projeto foi desenvolvido com foco em:

-Aprendizado de inteligência artificial aplicada
-Desenvolvimento de interfaces gráficas em Python
-Integração com modelos de linguagem (LLMs)
-Estruturação de projetos reais para portfólio
-Melhorias futuras
-Adição de sistema de voz (TTS e STT)
-Integração com APIs externas (OpenAI, HuggingFace)
-Memória avançada com banco de dados SQLite
-Interface mais moderna e responsiva
-Empacotamento como executável (.exe)

Autor:

Bruno Miguel
Desenvolvedor Python focado em inteligência artificial, automação e sistemas inteligentes.

Observação:

Este projeto tem finalidade educacional e pode ser expandido para aplicações mais avançadas de IA local e assistentes inteligentes.
