# A Generative AI-powered research tool…
A Generative AI-powered research tool that allows users to upload URLs or documents and ask questions based on the content. Built using Python, FastAPI, HuggingFace embeddings,  and Streamlit.


# Generative AI Research Tool

A smart research tool that allows users to input URLs or documents (PDF, TXT) and ask intelligent questions based on the content. It uses large language models, HuggingFace embeddings, and vector search to provide accurate answers with sources.

## 🔧 Features

- 📄 Upload PDFs or URLs
- 🔍 Ask questions based on document or page content
- 🧠 Uses HuggingFace Transformers & FAISS
- ⚡ FastAPI backend, Streamlit frontend
- 💬 Displays answers with sources for reference

## 🛠 Tech Stack

- Python
- FastAPI
- HuggingFace Transformers
- Chroma
- Streamlit
- LangChain (optional)
- GEMINII API (for responses)

## 🚀 How It Works

1. User uploads a file or URL
2. Content is broken into chunks and embedded
3. chroma is used to store vector database
4. Relevant context + user question is sent to the OpenAI model
5. The response is displayed in the UI

## 📦 Installation

```bash
git clone https://github.com/your-username/genai-research-tool.git
cd genai-research-tool
pip install -r requirements.txt


## 🚀 Run the App

```bash
streamlit run app.py


genai-research-tool/
├── app.py
├── backend/
│   ├── api.py
│   ├── utils.py
├── static/
├── embeddings/
├── requirements.txt
├── README.md

🧪 Example Prompts
"Summarize the uploaded research paper in 5 points."

"What are the key takeaways from the document?"

"List all the advantages mentioned in the PDF."

🙋‍♂️ About the Author
I’m Pravin Deshmukh, a Python backend developer and GenAI enthusiast.
I love building with FastAPI, LangChain, Redis, and OpenAI/Gemini APIs — and I’m actively seeking opportunities in backend or AI-powered product development.

📩 Connect on LinkedIn
📁 Explore More Projects
