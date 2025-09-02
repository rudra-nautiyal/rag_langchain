from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

db = Chroma(persist_directory="G:/Python/rag_langchain/rag_langchain/chroma_db", embedding_function=embedding_model)

def query_rag(question: str, k: int = 3):
    results = db.similarity_search(question, k=k)
    return [doc.page_content for doc in results]
