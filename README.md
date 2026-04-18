# 📚 RAG AI (Retrieval Augmented Generation)

A simple **local RAG (Retrieval-Augmented Generation) system** built with Python, FAISS, FastAPI, and Ollama.  
It allows you to ask questions from your own documents using a local LLM.

---

# 🚀 Features

- 📄 Load local documents (TXT support, extensible to PDF/DOCX)
- ✂️ Text chunking for better retrieval
- 🧠 Embeddings using HuggingFace Sentence Transformers
- 📦 Vector storage using FAISS
- 🔍 Semantic search for relevant context
- 🤖 Local LLM inference using Ollama (Mistral / Llama3)
- ⚡ FastAPI backend for model serving
- 💬 Interactive CLI chatbot with response time tracking

---

# 🏗️ Project Structure
rag-ai/
│
├── main.py # CLI RAG chatbot
├── load_data.py # Load documents
├── split_text.py # Chunking logic
├── embed_store.py # Embedding + FAISS DB
├── retrieve.py # Vector search
├── llm_client.py # Call FastAPI LLM
│
├── api.py # FastAPI server (Ollama)
│
└── data/
└── policy.txt

---

# ⚙️ Installation

```bash
pip install fastapi uvicorn ollama langchain faiss-cpu sentence-transformers requests```
---
## ▶️ Run FastAPI Server

```bash
uvicorn api:app --reload --host 127.0.0.1 --port 8000
---
## ▶️ 🧪 Run RAG Chatbot

```bash
uv run python main.py
---
# ⭐ Author

Built by **DamrithSom** 🚀  

A simple but powerful local RAG system for learning and production experimentation.
