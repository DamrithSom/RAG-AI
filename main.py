from load_data import load_documents
from split_text import split_documents
from embed_store import create_vector_db
from retrieve import retrieve_docs
from llm_client import call_llm
import time

def main():
    # 1. Load once
    docs = load_documents()

    # 2. Split once
    chunks = split_documents(docs)

    # 3. Build vector DB once
    db = create_vector_db(chunks)

    print("\n🚀 RAG system ready! Type 'exit' to quit.\n")

    while True:
        # 4. User input loop
        query = input("Ask: ")

        if query.lower() in ["exit", "quit"]:
            print("👋 Bye!")
            break

        start_time = time.time()

        # 5. Retrieve
        retrieved_docs = retrieve_docs(db, query)

        context = "\n".join([doc.page_content for doc in retrieved_docs])

        # 6. Prompt
        prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{query}
"""

        # 7. LLM call
        answer = call_llm(prompt)

        end_time = time.time()
        duration = end_time - start_time

        # 8. Output
        print("\n=== ANSWER ===")
        print(answer)
        print(f"\n⏱️ Time: {duration:.2f} seconds\n")


if __name__ == "__main__":
    main()