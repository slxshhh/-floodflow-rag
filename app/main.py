from fastapi import FastAPI
from app.schemas.query import QueryRequest
from app.services.rag_engine import search_catalog, build_prompt

app = FastAPI()



@app.post("/api/v1/chat/query")

async def ask_assistant(request: QueryRequest):
    search_results = search_catalog(query=request.query, filter_dict=request.filter_dict)
    prompt = build_prompt(user_query=request.query, search_results=search_results)
    return {"generated_prompt": prompt, "raw_results": search_results}