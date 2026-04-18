
from langchain_text_splitters import CharacterTextSplitter

def split_documents(documents):
    splitter = CharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)
