# SaraBot – Generative AI Research Assistant

SaraBot is a Generative AI-powered research tool designed to extract, process, and retrieve relevant information from provided URLs using a **Retrieval-Augmented Generation (RAG)** pipeline. It leverages **LangChain**, **ChromaDB**, and **OpenAI API** for semantic search and contextual answering, deployed entirely on **AWS** for scalability and reliability.

---

## 🚀 Features
- **RAG Pipeline** for accurate, source-cited answers.
- **LangChain + ChromaDB** for semantic search and document retrieval.
- **FastAPI Backend** for handling queries and API calls.
- **OpenAI API Integration** for natural language responses.
- **AWS-Powered Deployment** for reliability and scalability.

---

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI
- **LLM Orchestration:** LangChain
- **Vector Database:** ChromaDB
- **LLM Provider:** OpenAI API
- **Deployment:** AWS EC2, AWS S3, AWS CloudFront, AWS Route 53, AWS IAM
- **Networking:** AWS VPC, Security Groups
- **Monitoring:** AWS CloudWatch

---

## 📦 Project Structure
```
SaraBot/
│── app/
│   ├── main.py           # FastAPI app entry point
│   ├── rag_pipeline.py   # RAG logic
│   ├── vector_store.py   # ChromaDB integration
│   ├── utils.py          # Helper functions
│── requirements.txt      # Python dependencies
│── Dockerfile            # Docker configuration for deployment
│── README.md             # Project documentation
```
---

## ⚙️ AWS Deployment Steps

### 1️⃣ Prepare Environment
- Create an **AWS EC2** instance (Ubuntu 22.04 recommended).
- Assign an **Elastic IP** to ensure a static address.
- Open required ports in **Security Groups** (80, 443, 8000).

### 2️⃣ Install Dependencies
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

### 3️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/SaraBot.git
cd SaraBot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables
```bash
export OPENAI_API_KEY="your_openai_api_key"
```

### 5️⃣ Run Locally (For Testing)
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 6️⃣ (Optional) Docker Deployment
```bash
docker build -t sarabot .
docker run -d -p 8000:8000 sarabot
```

### 7️⃣ Reverse Proxy & SSL (AWS CloudFront + Route 53 + S3)
- Use **AWS CloudFront** for HTTPS distribution.
- Route domain via **AWS Route 53**.
- Store static assets in **AWS S3** for faster delivery.

### 8️⃣ Monitor
- Enable **AWS CloudWatch** for logs and metrics.
- Set up alarms for high CPU/Memory usage.

---

## 📌 Usage
1. Go to the deployed URL.
2. Enter up to 3 URLs.
3. Ask any question related to the content.
4. SaraBot retrieves relevant information and provides citations.

---

## 📜 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author
Developed by **PRAVIN DESHMUKH**
