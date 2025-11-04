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

## Screenshot DEMO
<img width="1919" height="1096" alt="Screenshot 2025-11-01 000905" src="https://github.com/user-attachments/assets/cc5c6182-45a9-4bb9-9f0a-5bac554dee4d" />

---

## ⚙️ Cara Menjalankan
### 1️⃣ Persiapan

```bash
Pastikan kamu sudah menginstall Ollama dan menjalankan server-nya:

ollama serve

Kemudian download model yang dibutuhkan:

ollama pull llama3
ollama pull mxbai-embed-large
```

### 2️⃣ Install Dependensi

```bash
Aktifkan virtual environment dan install semua library yang dibutuhkan:

pip install -r requirements.txt
```

### 3️⃣ Jalankan Aplikasi

```bash
Jalankan proyek dengan perintah berikut:

streamlit run app.py

Lalu copy ip address localhost ke browser
```
