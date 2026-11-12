from fastapi import FastAPI, HTTPException
from typer import prompt
from app.schemas.query import QueryRequest
from app.services.rag_engine import search_catalog, build_prompt
from app.core.llm import ask_gemini
from google.genai.errors import ServerError, ClientError

app = FastAPI()

@app.post("/api/v1/chat/query")

async def ask_assistant(request: QueryRequest):
    search_results = search_catalog(query=request.query, filter_dict=request.filter_dict)
    prompt = build_prompt(user_query=request.query, search_results=search_results)
    try:
        answer = ask_gemini(prompt)
        return {"answer": answer, "sources": search_results}
        
    except (ServerError, ClientError) as e:
        # Se a Google cair, devolvemos um erro 503 limpo para o usuário, não um 500 feio
        raise HTTPException(
            status_code=503, 
            detail="Nosso assistente de inteligência artificial está temporariamente indisponível devido à alta demanda. Por favor, tente novamente em alguns instantes."
        )