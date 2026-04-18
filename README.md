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

▶️ Run FastAPI Server
uvicorn api:app --reload --host 127.0.0.1 --port 8000
API Endpoint
POST http://127.0.0.1:8000/generate
🧪 Run RAG Chatbot
python main.py
💬 Example Usage
Ask: What is IT security policy?
Output
=== ANSWER ===
Employees must follow password policy and security guidelines.

⏱️ Time: 1.25 seconds
🔁 RAG Pipeline Workflow
Document
   ↓
Chunking
   ↓
Embedding (MiniLM)
   ↓
FAISS Vector DB
   ↓
User Query
   ↓
Top-K Retrieval
   ↓
Context Injection
   ↓
Prompt to LLM
   ↓
Ollama (Mistral / Llama3)
   ↓
Final Answer
🤖 API Example
Request
POST /generate
{
  "prompt": "What is leave policy?",
  "model": "mistral"
}
Response
{
  "response": "Employees are entitled to 14 days annual leave."
}
🧠 Code Flow (main.py)
docs = load_documents()
chunks = split_documents(docs)
db = create_vector_db(chunks)

while True:
    query = input("Ask: ")

    retrieved_docs = retrieve_docs(db, query)
    context = "\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{query}
"""

    answer = call_llm(prompt)
    print(answer)
🧠 Tech Stack
Python 🐍
FastAPI ⚡
FAISS 📦
Ollama 🤖
HuggingFace Transformers 🧠
LangChain (utilities only)
📌 Future Improvements
🌐 Web UI (Streamlit / React Chat UI)
📄 PDF / DOCX support
💾 Save & load FAISS index
💬 Chat memory (multi-turn conversation)
⚡ Streaming token response
🧩 Multi-document knowledge base
📷 Architecture
User Query
   ↓
Vector Search (FAISS)
   ↓
Relevant Context
   ↓
Prompt Engineering
   ↓
Local LLM (Ollama via FastAPI)
   ↓
Final Answer
⭐ Author

Built by DamrithSom 🚀
A simple but powerful local RAG system for learning and production experimentation.
