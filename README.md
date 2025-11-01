# 🤖 RAG Chatbot dengan Ollama + LangChain

Proyek ini membangun **chatbot lokal berbasis Retrieval-Augmented Generation (RAG)** menggunakan **Ollama**, **LangChain**, dan **ChromaDB**.  
Chatbot ini dapat menjawab pertanyaan berdasarkan isi dokumen teks lokal.

---

## 🚀 Fitur Utama

- 🔍 **Retrieval-Augmented Generation (RAG)** untuk jawaban berbasis konteks dokumen.  
- 🧠 **Ollama LLM (Llama3)** berjalan lokal tanpa koneksi API eksternal.  
- 📚 **ChromaDB** sebagai penyimpanan *vector embeddings* dokumen.  
- 🧩 **LangChain** sebagai kerangka kerja pipeline RAG.  
- 💬 **Streamlit UI** yang interaktif untuk tanya jawab langsung.

---

## 🧰 Teknologi yang Digunakan

| Komponen | Deskripsi |
|-----------|------------|
| 🦙 Ollama | Local LLM engine (model: `llama3` dan `mxbai-embed-large`) |
| 🧠 LangChain | Framework RAG pipeline |
| 🧩 LangChain-Chroma | Vector store integration |
| 💾 ChromaDB | Penyimpanan embeddings dokumen |
| 🪄 Streamlit | Antarmuka pengguna interaktif |
| 🐍 Python 3.10+ | Bahasa utama |

---


---

## ⚙️ Cara Menjalankan

### 1️⃣ Persiapan
Pastikan kamu sudah menginstall [Ollama](https://ollama.com/download) dan menjalankan server-nya:

```bash
ollama serve

Lalu download model yang dibutuhkan:
ollama pull llama3
ollama pull mxbai-embed-large

2️⃣ Install Dependensi
Aktifkan environment kamu lalu jalankan:
pip install -r requirements.txt

3️⃣ Jalankan Aplikasi
streamlit run app.py

