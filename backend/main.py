from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Enable CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str
    language: str

@app.post("/explain")
def explain_code(request: CodeRequest):

    prompt = f"""
Explain the following {request.language} code clearly and simply:

{request.code}
"""

    result = subprocess.run(
        ["ollama", "run", "deepseek-coder:6.7b"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return {"explanation": result.stdout.strip()}
