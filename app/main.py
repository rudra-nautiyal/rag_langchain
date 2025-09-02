from fastapi import FastAPI, Query
from app.rag_logic import query_rag

app = FastAPI(
    title="RAG API",
)

@app.get("/query")
def query_endpoint(question: str = Query(..., description="Enter your question")):
    results = query_rag(question)
    return {"question": question, "results": results}
