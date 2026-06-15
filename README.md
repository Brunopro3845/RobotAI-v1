# Assistente de IA Local em Python

## Visão geral

Este projeto é um assistente de inteligência artificial local desenvolvido em Python, com interface gráfica e integração com modelos de linguagem (LLMs), como Ollama.

O sistema foi projetado para funcionar como um chatbot extensível, capaz de manter histórico de conversas, memória básica e interação em tempo real por meio de interface gráfica.

O foco do projeto é aprendizado prático de inteligência artificial aplicada, arquitetura de software e desenvolvimento de aplicações desktop.

---

## Funcionalidades

- Chat com inteligência artificial local ou via API  
- Interface gráfica desenvolvida com CustomTkinter  
- Sistema de histórico de conversas persistente  
- Memória básica para contexto de interação  
- Processamento assíncrono para evitar travamentos na interface  
- Arquitetura modular para fácil manutenção e expansão  

---

## Arquitetura

.
main.py       -       # Ponto de entrada e interface principal
chatbot.py    -      # Comunicação com modelo de IA
memoria.py     -     # Gerenciamento de memória contextual
historico.py   -     # Persistência de conversas
assets/        -     # Recursos da interface
README.md

A separação em módulos permite evolução independente de cada componente, como substituição do modelo de IA ou melhoria da interface sem impacto no restante do sistema.

---

## Tecnologias utilizadas

- Python 3.x  
- CustomTkinter  
- Requests  
- Threading  
- Ollama API (ou outro modelo LLM local)  
- Tkinter  

---

## Como executar o projeto

1. Clonar o repositório:

git clone https://github.com/Brunopro3845/RobotAI.git
cd RobotAI

2. Instalar dependências:

pip install -r requirements.txt

3. Executar aplicação:

python main.py

---

## Requisitos

- Python 3.10 ou superior  
- Sistema operacional com suporte a interface gráfica  
- (Opcional) Ollama instalado para execução local de modelos  

---

## Objetivo do projeto

Este projeto foi desenvolvido com foco em:

- Aplicação prática de inteligência artificial em Python  
- Desenvolvimento de interfaces gráficas desktop  
- Integração com modelos de linguagem locais (LLMs)  
- Organização de código em arquitetura modular  
- Construção de portfólio técnico para demonstração profissional  

---

## Possíveis melhorias

- Implementação de memória avançada com banco de dados (SQLite ou similar)  
- Sistema de contexto mais robusto para conversas longas  
- Suporte a múltiplos modelos de IA  
- Adição de entrada e saída por voz (Speech-to-Text e Text-to-Speech)  
- Empacotamento como executável para distribuição  
- Interface gráfica mais avançada e responsiva  

---

## Estrutura de evolução do projeto

Este projeto foi pensado para evolução contínua em três níveis:

1. Base funcional: chatbot local com interface  
2. Expansão de inteligência: memória, contexto e múltiplos modelos  
3. Produto final: assistente completo com voz, persistência e interface refinada  

---

## Autor

Bruno Miguel  
Desenvolvedor Python com foco em inteligência artificial, automação e sistemas interativos.

---

## Observação

Este projeto tem finalidade educacional e serve como base para evolução em aplicações mais complexas de inteligência artificial local.
