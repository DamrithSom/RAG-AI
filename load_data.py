from langchain_community.document_loaders import TextLoader


def load_documents():
    loader = TextLoader("data/policy.txt")
    return loader.load()
