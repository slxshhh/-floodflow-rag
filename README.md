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
```
git clone [https://github.com/SEU-USUARIO/floodflow-rag.git](https://github.com/SEU-USUARIO/floodflow-rag.git)
cd floodflow-rag
python -m venv venv
````
# Ative o ambiente (Windows)
````
.\venv\Scripts\activate
````
# Ative o ambiente (Linux/Mac)
````
source venv/bin/activate
````
### 2. Instalar Dependências

````
pip install -r requirements.txt
````
### 3. Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto contendo sua chave da API do Google AI Studio:

Snippet de código
GEMINI_API_KEY=sua_chave_api_aqui

### 4. Popular o Banco de Dados (Ingestão)
Abasteça o ChromaDB com os dados de exemplo do restaurante:

````
python run_ingestion.py
5. Iniciar o Servidor
Bash
uvicorn app.main:app --reload
````
Acesse a documentação interativa (Swagger UI) em: http://127.0.0.1:8000/docs

### 🧠 Exemplo de Requisição (Grounded RAG)
````
POST /api/v1/chat/query

JSON
{
  "query": "Tem alguma opção sem glúten? Qual o valor?",
  "filter_dict": null
}
````
O sistema buscará a informação no ChromaDB, montará um prompt protegido contra alucinações, processará via Gemini e retornará a resposta baseada exclusivamente no catálogo do banco, acompanhada das fontes rastreáveis.

