# 📸 Project Screenshot

<p align="center">
  <img src="Screenshot 2026-02-17 230002.png" width="900"/>
</p>

# 🚀 AI Code Explainer

AI Code Explainer is a web-based application that explains programming code in simple and beginner-friendly terms using a Local Large Language Model (LLM).

The system runs fully offline using Ollama and does not require OpenAI or any external API.

---

# 📌 Project Overview

This project allows users to:

- Paste source code (Python, Java, C++)
- Select programming language
- Get short AI-generated explanations
- Run completely locally using a local LLM

Tech Stack:

Frontend  → React.js  
Backend   → FastAPI  
AI Model  → Ollama (TinyLlama / Phi3 Mini)  

---

# 🏗️ Architecture

User (React UI)
        ↓
FastAPI Backend
        ↓
Ollama Local Model
        ↓
Generated Explanation
        ↓
Displayed on Frontend

---

# 🛠️ Technologies Used

Frontend:
- React.js
- Axios
- CSS

Backend:
- Python 3.10+
- FastAPI
- Uvicorn
- Requests

AI:
- Ollama
- TinyLlama / Phi3 Mini

Version Control:
- Git
- GitHub

---

## 📂 Project Structure

```
ai_code_explainer/
│
├── backend/
│   ├── main.py
│   ├── venv/
│   └── requirements.txt
│
├── frontend/
│   └── frontend/
│       ├── src/
│       ├── public/
│       └── package.json
│
├── .gitignore
└── README.md
```


# ⚙️ Installation Guide

Follow these steps to run the project locally.

---

## 1️⃣ Install Python

Download:
https://www.python.org/downloads/

Check installation:
python --version

---

## 2️⃣ Install Node.js

Download:
https://nodejs.org/

Check installation:
node -v  
npm -v

---

## 3️⃣ Install Ollama

Download:
https://ollama.com

Verify:
ollama --version

---

## 4️⃣ Download AI Model

Recommended for 8GB RAM:

ollama pull tinyllama

OR

ollama pull phi3:mini

Check installed models:
ollama list

---

# 🔧 Backend Setup

Navigate to backend folder:

cd backend

Create virtual environment:

python -m venv venv

Activate (Windows):

venv\Scripts\activate

Install dependencies:

pip install fastapi uvicorn requests

(Optional) Generate requirements file:

pip freeze > requirements.txt

Run backend:

python -m uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

API Docs:

http://127.0.0.1:8000/docs

---

# 🎨 Frontend Setup

Navigate to frontend folder:

cd frontend/frontend

Install dependencies:

npm install

Start React server:

npm start

Frontend runs at:

http://localhost:3000

---

# 🚀 Run Full Project

Open two terminals:

Terminal 1 (Backend):

cd backend  
venv\Scripts\activate  
python -m uvicorn main:app --reload  

Terminal 2 (Frontend):

cd frontend/frontend  
npm start  

Make sure Ollama is installed and model is downloaded.

---

# 📌 How It Works

1. User enters code in React UI.
2. React sends POST request to FastAPI.
3. FastAPI creates prompt and sends it to Ollama.
4. Ollama generates explanation.
5. FastAPI returns explanation.
6. React displays output.

---

# 🧠 Prompt Design

Backend creates prompt like:

"Explain this code briefly in 3-4 lines..."

This ensures short and simple output.

---

# 📊 Features

- Short code explanations
- Clean dark UI
- Offline AI
- No API key required
- Beginner-friendly design
- Modern full-stack architecture

---

# ⚠️ System Requirements

Minimum:
- 8GB RAM
- Python 3.10+
- Node.js
- Ollama installed

Note:
First response may be slow due to model loading.

---