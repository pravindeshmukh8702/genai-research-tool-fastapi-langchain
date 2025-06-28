# SaraBotAI – Generative AI Research Tool 🤖

A Generative AI-powered research tool that allows users to upload URLs or documents and ask intelligent questions based on the content. Built using Python, Streamlit, HuggingFace embeddings, ChromaDB, LangChain, and Gemini API.

---

## 🔧 Features

- 📄 Upload URLs or text files (TXT)
- 🔍 Ask questions based on the uploaded content
- 🧠 Generates embeddings with HuggingFace Transformers
- 🗄️ Stores vectors in ChromaDB for semantic search
- 💬 Uses Gemini API to generate detailed answers with citations
- 📊 Visualizes frequent terms and generates summary reports

---

## 🛠 Tech Stack

- Python
- Streamlit (interactive frontend and backend)
- HuggingFace Transformers
- ChromaDB
- LangChain
- Gemini API
- Pandas & Plotly

---

## 🚀 How It Works

1. User uploads URLs or text files.
2. Content is split into chunks and embedded using HuggingFace models.
3. ChromaDB stores the vector embeddings.
4. Relevant context is retrieved via similarity search.
5. The Gemini model generates an answer based on the question and context.
6. Results are displayed in Streamlit, including sources and visualizations.

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/genai-research-tool.git
cd genai-research-tool
pip install -r requirements.txt


genai-research-tool/
├── app.py
├── modules/
│   ├── data_processing.py
│   ├── gemini_integration.py
├── assets/
│   └── style.css
├── requirements.txt
├── README.md


🧪 Example Prompts
"Summarize the uploaded research article in 5 bullet points."

"What are the main arguments presented in this document?"

"List all key takeaways from the content."

🙋‍♂️ About the Author
I’m Pravin Deshmukh, a Python backend developer and GenAI enthusiast.
I enjoy building intelligent products using Streamlit, LangChain, HuggingFace, and Gemini/OpenAI APIs.

📩 Connect with me on LinkedIn   https://www.linkedin.com/in/pravindeshmukh8702
💻 Explore more of my projects   https://github.com/pravindeshmukh8702
