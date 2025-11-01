import streamlit as st
from rag_pipeline import create_qa_chain

# Judul aplikasi
st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("🤖 RAG Chatbot dengan Ollama + LangChain")

# Inisialisasi QA chain (sekali saja, caching)
@st.cache_resource
def load_chain():
    return create_qa_chain()

qa_chain = load_chain()

# Input dari pengguna
query = st.text_input("Masukkan pertanyaanmu berdasarkan dokumen:", "")

if st.button("Tanya"):
    if query.strip() == "":
        st.warning("Masukkan pertanyaan dulu.")
    else:
        with st.spinner("Sedang memproses..."):
            result = qa_chain.invoke(query)
            st.success("Jawaban:")
            st.write(result["result"])
