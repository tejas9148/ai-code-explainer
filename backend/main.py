from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class CodeRequest(BaseModel):
    code: str
    language: str

@app.post("/explain")
def explain_code(request: CodeRequest):

    prompt = f"""
Explain the following {request.language} code in simple terms:

{request.code}
"""

    result = subprocess.run(
        ["ollama", "run", "deepseek-coder:6.7b"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return {
        "explanation": result.stdout.strip()
    }
