from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import ollama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="Prompt to send to the model")
    model: str = Field(default="mistral", description="Ollama model name")


@app.post("/generate")
async def generate_response(payload: GenerateRequest):
    prompt = payload.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    try:
        response = ollama.chat(
            model=payload.model,
            messages=[{"role": "user", "content": prompt}],
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Ollama request failed: {exc}") from exc

    message = response.get("message", {})
    return {"response": message.get("content", "")}