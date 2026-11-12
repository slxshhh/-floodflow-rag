# FoodFlow RAG 🍔🤖

Um motor de busca semântica e assistente conversacional (RAG - Retrieval-Augmented Generation) construído para o ecossistema de delivery de alimentos. 

Este projeto foi desenvolvido como demonstração de arquitetura para a trilha de **AI Engineer**, focando em Groundedness (prevenção de alucinação de IA) e resiliência de microsserviços.

## 🚀 Arquitetura e Stack Tecnológico

O sistema processa catálogos e regras de negócio em um banco de dados vetorial e utiliza Large Language Models (LLMs) para responder aos clientes com contexto estrito.

* **API & Roteamento:** [FastAPI](https://fastapi.tiangolo.com/) com validação estrita via Pydantic.
* **Vector Database:** [ChromaDB](https://www.trychroma.com/) (Persistência local) para busca semântica veloz.
* **LLM / GenAI:** [Google Gemini 3.8 Flash](https://aistudio.google.com/) via SDK `google-genai`.
* **Resiliência:** Tratamento avançado de exceções HTTP 503 (Unavailable) e 500 (Internal Error) com fallbacks amigáveis.
* **Ambiente:** Python 3.10+, configurado com `venv` e variáveis protegidas (`.env`).

## ⚙️ Como Executar Localmente

### 1. Clonar e Preparar o Ambiente
```bash
git clone [https://github.com/SEU-USUARIO/floodflow-rag.git](https://github.com/SEU-USUARIO/floodflow-rag.git)
cd floodflow-rag
python -m venv venv

# Ative o ambiente (Windows)
.\venv\Scripts\activate
# Ative o ambiente (Linux/Mac)
source venv/bin/activate
