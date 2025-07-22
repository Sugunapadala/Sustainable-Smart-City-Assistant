from fastapi import APIRouter, Request
from app.api.services.watsonx_service import ask_watsonx
from app.api.services.pinecone_client import semantic_search

router = APIRouter()

@router.get("/test")
async def test_route():
    return {"message": "Smart City Assistant backend is working ✅"}

@router.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    query = data.get("question")

    # 🔹 WatsonX Answer
    answer = ask_watsonx(query)

    # 🔹 Semantic Policies (optional)
    policies = semantic_search(query)

    return {
        "question": query,
        "watsonx_answer": answer,
        "matching_policies": policies
    }
