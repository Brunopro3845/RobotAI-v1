#  RobotIA

Um assistente virtual inteligente desenvolvido em Python com integração ao Ollama, interface gráfica moderna, memória persistente e histórico de conversas.

---

##  Sobre o Projeto

RobotIA é um assistente virtual criado para executar conversas utilizando modelos de inteligência artificial locais através do Ollama.

O projeto foi desenvolvido com foco em aprendizado de Python, inteligência artificial, interfaces gráficas e organização de código, utilizando uma arquitetura modular e preparada para futuras expansões.

---

##  Funcionalidades

*  Chat com IA local usando Ollama
*  Interface gráfica moderna com CustomTkinter
*  Memória permanente do usuário
*  Histórico de conversas
*  Exportação de chats para arquivos TXT
*  Alternância entre tema claro e escuro
*  Interface responsiva com Threads
*  Estrutura modular para facilitar manutenção e expansão

---

##  Tecnologias Utilizadas

* Python 3
* CustomTkinter
* Requests
* JSON
* Ollama
* Threading

---

##  Estrutura do Projeto

```text
RobotIA/
│
├── main.py
├── chatbot.py
├── memoria.py
├── historico.py
├── interface.py
│
└── data/
    ├── memoria.json
    └── historico.json
```

---

##  Instalação

Clone o repositório:

```bash
git clone https://github.com/Brunopro3845/RobotIA.git
```

Acesse a pasta:

```bash
cd RobotIA
```

Instale as dependências:

```bash
pip install customtkinter requests
```

---

##  Configurando o Ollama

Instale o Ollama:

https://ollama.com

Baixe um modelo:

```bash
ollama pull qwen2.5:0.5b
```

Inicie o Ollama normalmente e mantenha-o em execução.

---

##  Executando o Projeto

```bash
python main.py
```

ou

```bash
py main.py
```

---

##  Memória Permanente

A RobotIA é capaz de armazenar informações importantes em arquivos JSON, permitindo que determinados dados sejam preservados entre diferentes sessões.

Exemplo:

```text
Meu nome é Bruno
```

A informação será armazenada automaticamente e poderá ser utilizada posteriormente.

---

##  Histórico de Conversas

Todas as conversas podem ser armazenadas localmente através do sistema de histórico.

Os dados são salvos automaticamente em:

```text
data/historico.json
```

---

##  Objetivos do Projeto

* Aprender Inteligência Artificial Local
* Praticar Programação em Python
* Desenvolver Interfaces Gráficas
* Trabalhar com Persistência de Dados
* Criar um Assistente Virtual Personalizado

---

##  Futuras Atualizações

*  Reconhecimento de voz
*  Respostas por voz
*  Banco de dados SQLite
*  Leitura de PDFs
*  Pesquisa na internet
*  Sistema de plugins
*  Múltiplas conversas
*  Memória avançada

---

##  Autor

Bruno Miguel

GitHub:
https://github.com/Brunopro3845

---

## ⭐ Contribuição

Sugestões, melhorias e contribuições são sempre bem-vindas.

Se gostou do projeto, considere deixar uma estrela no repositório.
