from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Vectorization setup
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma(embedding_function=embeddings, persist_directory="chroma_db")

def add_articles_to_vectorstore(articles):
    docs = [article for article in articles if isinstance(article, str)]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    split_docs = text_splitter.split_text(docs)
    vectorstore.add_texts(split_docs)