# 🐍 Marvellous Python Tutor
```markdown

An AI-powered Python programming tutor built using **Python, Streamlit, Ollama, and Llama 3.2:1b**.

Marvellous Python Tutor provides an interactive chat interface where users can ask questions related to Python programming and receive AI-generated explanations, examples, and programming assistance.

The application uses **Ollama to run the Llama 3.2:1b model locally**, while **Streamlit** provides the web-based and mobile-friendly user interface.

---

## 🚀 Features

- 🐍 AI-powered Python programming tutor
- 💬 Interactive chat-based interface
- 🤖 Powered by **Llama 3.2:1b**
- 🦙 Uses **Ollama** for local LLM execution
- 🌐 Built using **Streamlit**
- 📱 Mobile-friendly web interface
- 🧠 Maintains conversation history during the session
- 💻 Runs locally without requiring a paid LLM API
- 🌍 Can be temporarily exposed to the internet using **Cloudflare Quick Tunnel**
- 🔒 Uses the local Ollama API for communication with the language model

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Application development |
| **Streamlit** | Web-based GUI |
| **Ollama** | Local LLM runtime |
| **Llama 3.2:1b** | Language model |
| **Python Ollama Library** | Communication between Python and Ollama |
| **Cloudflare Tunnel** | Temporary public access for demonstration |

---

## 📁 Project Structure

```text
marvellous-python-tutor/
│
├── marvellous_python_tutor.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File | Description |
|---|---|
| `marvellous_python_tutor.py` | Main Streamlit chatbot application |
| `requirements.txt` | Python project dependencies |
| `README.md` | Project documentation |
| `.gitignore` | Files and folders excluded from Git |

---

# ⚙️ Prerequisites

Before running the project, make sure the following software is installed:

- Python 3.x
- Ollama
- Git
- A supported web browser

For optional public access:

- `cloudflared.exe`

---
## 📦 Installation

Follow the steps below to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/SurajGardi/marvellous-python-tutor.git
```

Move into the project directory:

```bash
cd marvellous-python-tutor
```

### 2. Create the Python Virtual Environment

It is recommended to use a Python virtual environment for this project.

## 1. Create a Virtual Environment

From the project directory:

```bash
python -m venv MarvellousLLM
```

## 2. Activate the Virtual Environment

### Windows

```powershell
MarvellousLLM\Scripts\activate
```

### Linux / macOS

```bash
source MarvellousLLM/bin/activate
```

After activation, the terminal should show something similar to:

```text
(MarvellousLLM)
```

---

# 📦 Python Dependencies

The project uses the following Python packages:

```text
streamlit
ollama
```

Install them using:

```bash
python -m pip install -r requirements.txt
```

You can also install them individually:

```bash
python -m pip install streamlit
python -m pip install ollama
```

Verify Streamlit:

```bash
streamlit --version
```

Verify the Ollama Python library:

```bash
python -c "import ollama; print('Ollama Python library installed successfully')"
```

---

# 🦙 Ollama Setup

Marvellous Python Tutor uses **Ollama** to run the language model locally.

Ollama provides a local environment for running large language models without requiring a paid cloud LLM API.

The Python application communicates with Ollama through its local API.

By default, Ollama runs its API at:

```text
http://localhost:11434
```

---

## 1. Install Ollama

### Windows

Download Ollama from the official website:

https://ollama.com/download/windows

Install Ollama normally.

After installation, verify it:

```powershell
ollama --version
```

Example:

```text
ollama version is 0.x.x
```

---

## 2. Download Llama 3.2:1b

This project uses:

```text
llama3.2:1b
```

Download the model using:

```powershell
ollama pull llama3.2:1b
```

Ollama will download the model and store it locally.

> **Note:** The model itself is not stored inside this GitHub repository. It is managed separately by Ollama on the local machine.

---

## 3. Verify the Model

Check the installed models:

```powershell
ollama list
```

You should see something similar to:

```text
NAME            ID              SIZE
llama3.2:1b     ...             ...
```

---

## 4. Test Llama 3.2:1b

Run:

```powershell
ollama run llama3.2:1b
```

Then try:

```text
Hello! Explain what a chatbot is.
```

If the model responds successfully, the Ollama and Llama setup is working.

To exit the interactive session:

```text
/bye
```

---

# 🔌 Verify Ollama API

Ollama normally runs its local API at:

```text
http://localhost:11434
```

You can verify that Ollama is running by opening this address in your browser:

```text
http://localhost:11434
```

You can also test the API from PowerShell:

```powershell
Invoke-WebRequest `
  -Method POST `
  -Body '{"model":"llama3.2:1b","prompt":"Hello","stream":false}' `
  -Uri http://localhost:11434/api/generate
```

If Ollama is running correctly, the command should return a JSON response containing the generated output.

---

# 🧪 Test Ollama from Python

The Python application communicates with Ollama using the Python `ollama` library.

Create a temporary file:

```text
test_ollama.py
```

Add:

```python
import ollama

response = ollama.chat(
    model="llama3.2:1b",
    messages=[
        {
            "role": "user",
            "content": "Hello! Explain what an LLM is in simple words."
        }
    ]
)

print(response["message"]["content"])
```

Run:

```powershell
python test_ollama.py
```

If you receive an AI-generated response, the following integration is working:

```text
Python
   ↓
Ollama Python Library
   ↓
Ollama
   ↓
Llama 3.2:1b
```

---

# ▶️ Run the Application

Make sure:

1. Ollama is installed
2. Ollama is running
3. `llama3.2:1b` is available
4. The Python virtual environment is activated
5. Project dependencies are installed

Activate the environment:

```powershell
MarvellousLLM\Scripts\activate
```

Then start the Streamlit application:

```powershell
streamlit run marvellous_python_tutor.py
```

Streamlit will provide a local address similar to:

```text
Local URL: http://localhost:8501
```

Open:

```text
http://localhost:8501
```

in your browser.

---

# 💡 Example Questions

You can ask questions such as:

```text
What is inheritance in Python?
```

```text
Explain decorators in Python.
```

```text
What is the difference between a list and a tuple?
```

```text
Explain Python exception handling.
```

```text
How does a Python dictionary work?
```

```text
Write a Python program to check whether a number is prime.
```

```text
Explain polymorphism with an example.
```

---

# 🧠 How It Works

The application uses Streamlit to provide the web-based chat interface.

The user's question is added to the conversation history and sent to the Ollama-powered Llama 3.2:1b model.

The generated response is then displayed in the Streamlit interface.

```text
┌─────────────────────┐
│        User         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Streamlit Chat UI   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Conversation History│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Python Application  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Ollama Python Client│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Ollama         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Llama 3.2:1b     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    AI Response      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Streamlit Interface │
└─────────────────────┘
```

---

# 🌐 Free Public Demonstration

The application can be temporarily exposed to the internet using **Cloudflare Quick Tunnel**.

This allows the Streamlit application running on the local laptop to be accessed from another device, such as a mobile phone.

## Architecture

```text
                 INTERNET
                    │
                    ▼
        https://xxxxx.trycloudflare.com
                    │
                    ▼
          Cloudflare Quick Tunnel
                    │
                    ▼
              Your Laptop
                    │
              Port 8501
                    │
                    ▼
              Streamlit
                    │
                    ▼
        marvellous_python_tutor.py
                    │
                    ▼
                 Ollama
                    │
                    ▼
              Llama 3.2:1b
```

> **Important:** Cloudflare is only providing the tunnel. The LLM continues to run locally through Ollama on the laptop.

---

# ☁️ Cloudflare Quick Tunnel Setup

Cloudflare Quick Tunnel provides a temporary public URL without requiring a Cloudflare account or domain.

The URL normally looks like:

```text
https://random-name.trycloudflare.com
```

This setup is intended for demonstration and development purposes.

---

## Step 1 — Download cloudflared

Download the Windows version of `cloudflared` from the official Cloudflare documentation:

https://developers.cloudflare.com/tunnel/downloads/

For a 64-bit Windows system, download the Windows AMD64 executable.

The downloaded file may have a name similar to:

```text
cloudflared-windows-amd64.exe
```

---

## Step 2 — Store cloudflared

Create a folder such as:

```text
D:\Software
```

Rename the downloaded executable to:

```text
cloudflared.exe
```

The final location should be:

```text
D:\Software\cloudflared.exe
```

Project files and `cloudflared.exe` are kept separate.

```text
D:\
│
├── Software
│   └── cloudflared.exe
│
└── Marvellous
    └── ...
        └── marvellous-python-tutor
            ├── marvellous_python_tutor.py
            ├── requirements.txt
            └── README.md
```

---

## Step 3 — Verify cloudflared

Open PowerShell:

```powershell
cd D:\Software
```

Run:

```powershell
.\cloudflared.exe --version
```

Example:

```text
cloudflared version 2026.x.x
```

> `cloudflared` does not need to be installed inside the Python virtual environment. It is a separate Windows executable.

---

# Step 4 — Start Ollama

Make sure Ollama is running.

Verify the model:

```powershell
ollama list
```

Make sure:

```text
llama3.2:1b
```

is available.

If required:

```powershell
ollama run llama3.2:1b
```

---

# Step 5 — Start Streamlit

Open a PowerShell terminal and navigate to the project:

```powershell
cd "D:\path\to\marvellous-python-tutor"
```

Activate the virtual environment:

```powershell
MarvellousLLM\Scripts\activate
```

Start Streamlit:

```powershell
streamlit run marvellous_python_tutor.py
```

You should see:

```text
Local URL: http://localhost:8501
```

Keep this terminal running.

---

# Step 6 — Start Cloudflare Quick Tunnel

Open a **second PowerShell window**.

Navigate to the Cloudflare executable:

```powershell
cd D:\Software
```

Run:

```powershell
.\cloudflared.exe tunnel --url http://localhost:8501
```

Cloudflare will generate a temporary public URL similar to:

```text
https://random-name.trycloudflare.com
```

Example:

```text
https://example-name.trycloudflare.com
```

Copy the generated URL.

---

# Step 7 — Test the Public Application

Before sharing the link with another person, test it yourself.

For a proper internet test:

1. Open the link on your mobile phone.
2. Turn off Wi-Fi.
3. Use mobile data / 4G / 5G.
4. Open the generated `trycloudflare.com` URL.
5. Ask a Python-related question.

For example:

```text
What is inheritance in Python?
```

If the chatbot responds successfully, the complete system is working.

---

# 🔄 Complete Live Architecture

```text
             📱 Mobile Device
                    │
                    │ HTTPS
                    ▼
       https://xxxxx.trycloudflare.com
                    │
                    ▼
          ☁️ Cloudflare Tunnel
                    │
                    ▼
             💻 Your Laptop
                    │
                    ▼
          🌐 Streamlit :8501
                    │
                    ▼
       🐍 Python Chatbot Application
                    │
                    ▼
              🦙 Ollama
                    │
                    ▼
             Llama 3.2:1b
                    │
                    ▼
             🤖 AI Response
```

---

# 🖥️ Required Terminals for Live Demo

When running the application publicly, the following services need to remain active.

### Terminal 1 — Streamlit

```powershell
streamlit run marvellous_python_tutor.py
```

### Terminal 2 — Cloudflare Tunnel

```powershell
cd D:\Software
.\cloudflared.exe tunnel --url http://localhost:8501
```

### Ollama

Ollama must also be running locally with:

```text
llama3.2:1b
```

The laptop should remain:

```text
🔌 Connected to power
🌐 Connected to the internet
💻 Running
```

---

# ⚠️ Cloudflare Quick Tunnel Limitations

Cloudflare Quick Tunnels are designed for development and testing.

The generated:

```text
https://xxxxx.trycloudflare.com
```

URL is temporary.

Important points:

- The URL can change when a new Quick Tunnel is created.
- The tunnel stops when `cloudflared` is stopped.
- The laptop must remain running.
- Streamlit must remain running.
- Ollama must remain available.
- The laptop must have an active internet connection.
- There is no production uptime guarantee for Quick Tunnels.
- Anyone who has the public URL may be able to access the application.

Therefore, this setup is suitable for **learning, testing, demonstrations, and temporary sharing**, rather than production hosting.

---

# 🔐 Security Notes

This project runs the LLM locally using Ollama.

No paid LLM API key is required for the basic application.

Do not expose sensitive information through the public chatbot.

Do not commit the following to Git:

```text
.env
.env.*
.streamlit/secrets.toml
API keys
Passwords
Private credentials
```

The project `.gitignore` is included to help prevent accidental commits of common sensitive or temporary files.

---

# 💰 Cost

The basic project can be developed and demonstrated at **₹0 cost**.

```text
Python              → Free
Streamlit           → Free
Ollama              → Free
Llama 3.2:1b        → Local model
Cloudflare Quick
Tunnel              → Free for temporary testing
GitHub              → Free repository
```

The main requirement is a computer capable of running the Llama model and an internet connection when using the public tunnel.

---

# 🔮 Future Improvements

Possible future improvements include:

- 🐍 Python code execution
- 🎨 Improved syntax highlighting
- 💾 Conversation export
- 🤖 Support for multiple LLM models
- 💬 Persistent chat history
- 🔐 User authentication
- 📊 Chat analytics
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Python learning resources integration
- 🌐 Production deployment
- ☁️ Cloud-based LLM deployment
- 🎤 Voice input and output

---

# 👨‍💻 Author

**Suraj Gardi**

GitHub:  
https://github.com/SurajGardi

---

# ⭐ Acknowledgement

This project was developed as part of learning and experimenting with:

- Large Language Models
- Ollama
- Llama models
- Streamlit
- Python
- Generative AI
- Local AI application development

---

⭐ If you find this project useful, consider giving it a star!
```