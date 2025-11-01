from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

def create_qa_chain():
    # 1. Load dokumen dari folder docs
    loader = TextLoader("docs/sample.txt")
    docs = loader.load()

    # 2. Pisahkan teks biar bisa diembeding
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(docs)

    # 3. Buat embeddings dari Ollama
    embedding = OllamaEmbeddings(model="mxbai-embed-large")

    # 4. Simpan vectorstore di lokal
    vectorstore = Chroma.from_documents(texts, embedding, persist_directory="./chroma_db")

    # 5. Load model LLM (llama3)
    llm = Ollama(model="llama3")

    # 6. Gabungkan retrieval + LLM jadi chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return qa_chain


if __name__ == "__main__":
    qa = create_qa_chain()
    query = "Siapa yang membuat chatbot ini?"
    result = qa.run(query)
    print("🔹 Pertanyaan:", query)
    print("🔹 Jawaban:", result)
