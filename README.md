# ai-code-explainer
📌 PROJECT COMMANDS + REQUIREMENTS + WORKING SUMMARY
🖥️ Commands to Run Project
1️⃣ Activate virtual environment
cd backend
venv\Scripts\activate

2️⃣ Start backend server
python -m uvicorn main:app


Server runs at:

http://127.0.0.1:8000

3️⃣ Open frontend

Open file:

frontend/index.html


(Double click or open in browser)

4️⃣ Run AI model (if not running automatically)
ollama run deepseek-coder:6.7b

📦 Requirements / Installations Needed
🟢 Software Required

Install these once:

✔ Python

Download:
https://python.org

✔ Ollama

Download:
https://ollama.com

✔ Model Download

Run once:

ollama pull deepseek-coder:6.7b

🟢 Python Libraries Required

Install inside backend folder:

pip install fastapi uvicorn pydantic

📂 Project Folder Structure
ai-code-explainer
│
├── backend
│     └── main.py
│
├── frontend
│     └── index.html
│
└── venv

⚙️ How Project Works (Overall Flow)
Step-by-Step Execution

User enters code in frontend UI.

Frontend sends POST request to backend.

Backend receives code input.

Backend sends prompt to AI model (DeepSeek-Coder via Ollama).

Model analyzes code logic.

Model generates explanation.

Backend returns explanation.

Frontend displays explanation to user.

Architecture Diagram (Text)
User
 ↓
Frontend (HTML UI)
 ↓
FastAPI Backend
 ↓
Ollama Engine
 ↓
DeepSeek-Coder Model
 ↓
Explanation Response
 ↓
Frontend Display

🧠 Technology Stack Used
Component	Technology
Frontend	HTML, CSS, JavaScript
Backend	FastAPI (Python)
AI Model	DeepSeek-Coder
AI Runtime	Ollama
API Communication	REST API
🎯 Project Objective

To build an AI system that automatically explains programming code in simple language using a locally hosted large language model.

⭐ Key Features

Explains code logic

Works offline

Supports multiple languages

No API cost

Fast response

User-friendly interface

Runs locally

🔐 Advantages

No internet dependency

Secure local execution

Free to use

Customizable

Lightweight frontend

Real AI reasoning