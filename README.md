SaraBotAI – Generative AI Research Tool 🤖
A Generative AI–powered research assistant that processes URLs or documents and answers intelligent questions based on the content. Designed for fast, accurate research with semantic search, embeddings, and LLM integration.

🔧 Features
📄 Upload URLs or plain-text files (TXT)
🔍 Ask natural-language questions about uploaded content
🧠 Generate embeddings with HuggingFace Transformers
🗄️ Store and search vectors in ChromaDB
💬 Generate detailed, cited answers via Gemini API
📊 Visualize key terms and generate summary reports

🛠 Tech Stack
Language: Python
Frontend + Backend: Streamlit
Embeddings: HuggingFace Transformers
Vector DB: ChromaDB
Orchestration: LangChain
LLM: Gemini API
Visualization: Pandas, Plotly
Cloud: AWS (EC2, S3, IAM, Security Groups)

🚀 How It Works
Upload URLs or text files.
Content is split into chunks → embedded via HuggingFace model.
Embeddings are stored in ChromaDB.
A similarity search fetches the most relevant chunks.
Gemini API generates answers based on retrieved context.
Results (answer, citations, visualizations) are displayed in Streamlit.

📦 Installation (Local)
# 1. Clone repo
git clone https://github.com/pravindeshmukh8702/genai-research-tool.git
cd genai-research-tool

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables
export GEMINI_API_KEY="your_api_key_here"     # Mac/Linux
set GEMINI_API_KEY="your_api_key_here"        # Windows

# 5. Run the app locally
streamlit run app.py
☁️ AWS Deployment (EC2)
Launch EC2 Instance

OS: Ubuntu 22.04 LTS
Instance type: t2.medium (or higher)
Allow inbound rules: HTTP (80), HTTPS (443), Custom TCP 8501 (Streamlit default), SSH (22)

SSH into EC2
ssh -i your-key.pem ubuntu@your-ec2-public-ip

Install system packages
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y

Clone your repo
git clone https://github.com/pravindeshmukh8702/genai-research-tool.git
cd genai-research-tool

Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Set environment variables
echo "export GEMINI_API_KEY='your_api_key_here'" >> ~/.bashrc
source ~/.bashrc

Run Streamlit on public IP
streamlit run app.py --server.address 0.0.0.0 --server.port 8501

(Optional) Keep app running with screen
sudo apt install screen -y
screen -S sarabot
streamlit run app.py --server.address 0.0.0.0 --server.port 8501

# Detach: Ctrl+A then D
Access app
Open in browser:
http://<your-ec2-public-ip>:8501

📂 Project Structure
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

📊 Architecture Diagram
User → Streamlit App → LangChain Orchestrator
→ HuggingFace Embeddings → ChromaDB → Gemini API
→ Answer + Citations → Streamlit Visualization

🙋‍♂️ About the Author
I’m Pravin Deshmukh, a Python backend developer and AWS + AI integration enthusiast.
I build intelligent, deployable products using AWS, Streamlit, LangChain, HuggingFace, and LLM APIs.
📩 LinkedIn – linkedin.com/in/pravindeshmukh8702
💻 GitHub – github.com/pravindeshmukh8702
